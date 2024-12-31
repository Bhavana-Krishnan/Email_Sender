import os
from pathlib import Path
import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path  # os.path

# Load HTML template


def load_email_template(template_path: str, placeholders: dict) -> str:
    """Load and substitute placeholders in an HTML email template."""
    try:
        html_template = Template(Path(template_path).read_text())
        return html_template.substitute(placeholders)
    except FileNotFoundError:
        print(f"Error: Template file not found at {template_path}")
        raise
    except KeyError as e:
        print(f"Error: Missing placeholder key - {e}")
        raise

# Send email


def send_email(
    sender_email: str, sender_name: str, recipients: list, subject: str, template_path: str, smtp_server: str, smtp_port: int, app_password: str
):
    """Send emails with unique content to multiple recipients."""
    try:
        for recipient in recipients:
            recipient_email = recipient.get('email')
            placeholders = recipient.get('placeholders')

            # Load and customize the email template for this recipient
            content = load_email_template(template_path, placeholders)

            email = EmailMessage()
            email['from'] = sender_name
            email['to'] = recipient_email
            email['subject'] = subject
            email.set_content(content, 'html')

            with smtplib.SMTP(host=smtp_server, port=smtp_port) as smtp:
                smtp.ehlo()
                smtp.starttls()
                smtp.login(sender_email, app_password)
                smtp.send_message(email)
                print(f"Email sent successfully to {recipient_email}!")

    except smtplib.SMTPAuthenticationError:
        print(
            "Error: Authentication failed. Please check your email address or app password.")
    except smtplib.SMTPException as e:
        print(f"SMTP error occurred: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    # Email configuration
    TEMPLATE_PATH = 'index.html'  # Path to your HTML template
    SMTP_SERVER = 'smtp.gmail.com'
    SMTP_PORT = 587

    # Sender details
    SENDER_EMAIL = os.getenv('EMAIL_ADDRESS', 'sender@gmail.com')
    SENDER_NAME = 'Bhavana Krishnan'
    APP_PASSWORD = os.getenv('EMAIL_APP_PASSWORD', 'your_app_password')

    # Recipients and placeholders
    RECIPIENTS = [
        {'email': 'receiver1@gmail.com', 'placeholders': {'name': 'TinTin'}},
        {'email': 'receiver2@gmail.com', 'placeholders': {'name': 'Snowy'}}
    ]
    SUBJECT = 'Sending email through script'

    try:
        send_email(
            sender_email=SENDER_EMAIL,
            sender_name=SENDER_NAME,
            recipients=RECIPIENTS,
            subject=SUBJECT,
            template_path=TEMPLATE_PATH,
            smtp_server=SMTP_SERVER,
            smtp_port=SMTP_PORT,
            app_password=APP_PASSWORD,
        )
    except Exception as e:
        print(f"Failed to send emails: {e}")
