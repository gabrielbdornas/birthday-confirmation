import os
from dotenv import load_dotenv
import smtplib
from email.mime.text import MIMEText
from supabase_conection import get_total_confirmed_people

def send_email(total_people):
    # Email details
    subject = "Confirmações Aniversário 40 anos!"
    body = f"Total de pessoas confirmadas: {total_people}"
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = os.environ.get("EMAIL_USER")
    msg["To"] = os.environ.get("EMAIL_USER")

    # SMTP configuration
    smtp_server = os.environ.get("SMTP_SERVER")
    smtp_port = int(os.environ.get("SMTP_PORT"))
    email_user = os.environ.get("EMAIL_USER")
    email_password = os.environ.get("EMAIL_PASSWORD")

    with smtplib.SMTP_SSL(smtp_server, smtp_port) as smtp:
        smtp.login(email_user, email_password)
        smtp.sendmail(msg['From'], msg['To'], msg.as_string())

    print("Email sent successfully.")

if __name__ == "__main__":
    # Get total confirmed attendees
    total_people = get_total_confirmed_people()

    # Send email
    send_email(total_people)
