import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

# Load the variables from the .env file into the script's environment
load_dotenv()

# 1. Fetch configuration securely using os.getenv()
SMTP_SERVER = os.getenv("SMTP_SERVER")

# Cast port to integer, with a default fallback to 587
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))
SMTP_USERNAME = os.getenv("SMTP_USERNAME")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")

SENDER_EMAIL = os.getenv("SENDER_EMAIL")
RECIPENT_EMAIL = os.getenv("RECIPIENT_EMAIL")

# 2. Construct the email
msg = EmailMessage()
msg['Subject'] = "Alerts"
msg["From"] = SENDER_EMAIL
msg["To"] = RECIPENT_EMAIL

# You can also pass variables into the email body using f-strings
dynamic_message = f"This automated alert was sent from {SENDER_EMAIL}."
msg.set_content(dynamic_message)

# 3. Send the email securely
try:
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        server.send_message(msg)

    print(f"Email successfully sent to {RECIPENT_EMAIL}!")

except smtplib.SMTPAuthenticationError:
    print("Authentication failed. Check your SMTP_USERNAME and SMTP_PASSWORD.")
except Exception as e:
    print(f"Failed to send email: {e}")

