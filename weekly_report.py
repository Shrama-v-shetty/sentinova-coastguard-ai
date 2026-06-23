import smtplib
from email.mime.text import MIMEText
import os

def send_weekly_report():

    sender_email = os.getenv("EMAIL_ID")
    receiver_email = os.getenv("EMAIL_ID")
    password = os.getenv("EMAIL_PASSWORD")
    try:
        with open("reports.txt", "r") as f:
            lines = f.readlines()
    except:
        lines = []

    if not lines:
        body = "No reports available for this week."
    else:
        body = "📊 Weekly Dam Crack Report\n\n"

        for i, line in enumerate(lines, start=1):
            body += f"{i}. {line}"

    subject = "📊 Weekly Dam Crack Summary"

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, password)
    server.send_message(msg)
    server.quit()

    # Clear file after sending
    open("reports.txt", "w").close()