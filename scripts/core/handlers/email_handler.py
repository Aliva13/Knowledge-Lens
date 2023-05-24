import os
import smtplib
from scripts.core.schema.model import Email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from scripts.logging.logger import logger
from scripts.exceptions.exceptions_code import Email_HandlerException

def send_email(body, email: Email):
    sender_email = os.environ.get("sender_email")
    sender_password = os.environ.get("sender_password")
    receiver_email = email.rec_email
    print(sender_email)
    print(sender_password)
    print(receiver_email)

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = email.subject

    message.attach(MIMEText(body, "html"))

    try:
        logger.info("Handlers:send_email")
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)

        server.send_message(message)

        server.quit()
        logger.info("send_email:email sent !!!!!!")
        return {"message": "Email sent"}
    except Exception as e:
        logger.error(Email_HandlerException.EX006.format(error=str(e)))
        return {"message": str(e)}
