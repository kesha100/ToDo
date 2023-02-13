import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from django.core.mail import send_mail


def send_task_notification(email):
    message = f"""
    Hi, {email}! Make sure to not forget to accomplish this task
    """
    send_mail(
        subject='Accomplish your task',
        message=message,
        from_email='qwertyqazqwerty123456789@gmail.com',
        recipient_list=[email, ]
    )
