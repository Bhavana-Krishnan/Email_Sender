# Email Sender Script

This script allows you to send emails using a Gmail account via the SMTP protocol. It supports dynamic content substitution using an HTML template with placeholders and now includes functionality for sending personalized emails to multiple recipients.

## Features

- Sends emails using Gmail's SMTP server.
- Supports dynamic HTML content using placeholders.
- Allows sending personalized emails to multiple recipients.
- Includes error handling for common issues like missing files or authentication errors.
- Secures sensitive information (e.g., email credentials) using environment variables.

---

## Prerequisites

### Python Installation

Ensure you have Python 3.7 or later installed on your machine. You can verify by running:

```bash
python --version
```

### Required Libraries

The script uses the following Python libraries:

- `os` (built-in)
- `pathlib` (built-in)
- `smtplib` (built-in)
- `email` (built-in)
- `string` (built-in)

### Gmail Configuration

Before running the script, make sure:

1. Two-Factor Authentication (2FA) is enabled for your Google account.
2. An **App Password** is generated for use in this script. To generate an App Password:
    - Go to [Google Account Security Settings](https://myaccount.google.com/security).
    - Under **"Signing in to Google"**, enable **2-Step Verification**.
    - Go to the **App Passwords** section and generate a password for the "Mail" app.

---

## Environment Variables

To enhance security, store sensitive details as environment variables:

- `EMAIL_ADDRESS`: Your Gmail address.
- `EMAIL_APP_PASSWORD`: The App Password generated from Gmail settings.

### Setting Environment Variables

#### Linux/MacOS

Add the following lines to your `.bashrc` or `.zshrc` file:

```bash
export EMAIL_ADDRESS="your_email@gmail.com"
export EMAIL_APP_PASSWORD="your_app_password"
```

Apply the changes by running:

```bash
source ~/.bashrc
```

#### Windows

Set the environment variables in the command prompt:

```cmd
set EMAIL_ADDRESS=your_email@gmail.com
set EMAIL_APP_PASSWORD=your_app_password
```

Or, set them permanently via **System Properties > Environment Variables**.

---

## How to Use

### Step 1: Prepare Your HTML Template

Create an `index.html` file with placeholders for dynamic content. For example:

```html
<html>
<body>
    <h1>Hello, ${name}!</h1>
    <p>This is a test email sent via a Python script.</p>
</body>
</html>
```

### Step 2: Configure the Recipients

Define a list of recipients, including their email addresses and placeholder values. For example:

```python
RECIPIENTS = [
    {'email': 'receiver1@gmail.com', 'placeholders': {'name': 'TinTin'}},
    {'email': 'receiver2@gmail.com', 'placeholders': {'name': 'Snowy'}}
]
```

### Step 3: Run the Script

Execute the script using:

```bash
python email_sender.py
```

### Step 4: Verify Output

If successful, the script prints:

```
Email sent successfully to receiver1@gmail.com!
Email sent successfully to receiver2@gmail.com!
```

---

## Script Structure

### Function: `load_email_template`

- **Purpose**: Loads an HTML file and substitutes placeholders.
- **Parameters**:
    - `template_path` (str): Path to the HTML template.
    - `placeholders` (dict): Key-value pairs for substitution.

### Function: `send_email`

- **Purpose**: Sends emails to multiple recipients, customizing content for each.
- **Parameters**:
    - `sender_email` (str): Sender's email address.
    - `sender_name` (str): Name of the sender.
    - `recipients` (list): List of dictionaries, each containing `email` and `placeholders`.
    - `subject` (str): Email subject.
    - `template_path` (str): Path to the HTML template.
    - `smtp_server` (str): SMTP server address.
    - `smtp_port` (int): SMTP server port.
    - `app_password` (str): App password for authentication.

---

## Error Handling

The script includes robust error handling for various scenarios:

- **FileNotFoundError**: Triggered if the HTML template file is missing.
- **KeyError**: Triggered if a required placeholder is missing.
- **SMTPAuthenticationError**: Triggered if Gmail authentication fails (e.g., incorrect credentials).
- **SMTPException**: Triggered for general SMTP issues.
