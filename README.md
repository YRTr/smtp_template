# Python SMTP Email Sender

A robust, secure Python script for sending automated emails using an SMTP relay. This template uses environment variables to keep credentials and configuration secure and separate from the source code.

## Prerequisites

*   Python 3.6 or higher
*   An SMTP server/relay account (e.g., SendGrid, Mailgun, AWS SES, or a Gmail/Workspace App Password)
*   `python-dotenv` library installed

## Installation

1.  **Clone or download** this repository.
2.  **Install the required dependency:**
    ```bash
    pip install python-dotenv
    ```
3.  **Create your environment file:**
    Create a file named `.env` in the same directory as the script. Add your credentials and routing information:
    ```env
    SMTP_SERVER=smtp.your-email-provider.com
    SMTP_PORT=587
    SMTP_USERNAME=your_smtp_username
    SMTP_PASSWORD=your_super_secret_api_key
    SENDER_EMAIL=alerts@yourcustomdomain.com
    RECIPIENT_EMAIL=your.personal.id@gmail.com
    ```
    *Note: Ensure `.env` is added to your `.gitignore` file so it is never uploaded to a repository.*
