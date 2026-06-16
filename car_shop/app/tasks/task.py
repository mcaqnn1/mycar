from core.celery import celery
from email.message import EmailMessage
from core.settings import get_settings
import smtplib

settings = get_settings()

@celery.task
def send_email(to_email:str,subject:str,body:str):
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = settings.SMTP_USER
    msg["To"] = to_email

    msg.set_content(body)

    with smtplib.SMTP_SSL(settings.SMTP_HOST,settings.SMTP_PORT) as server:
        server.login(
            settings.SMTP_USER,
            settings.SMTP_PASS
        )
        server.send_message(msg=msg)