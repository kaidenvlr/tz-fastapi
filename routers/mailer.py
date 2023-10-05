import logging
import re
import smtplib
from email.mime.text import MIMEText
from functools import lru_cache
from typing import Annotated

from fastapi import APIRouter, HTTPException, Depends

from config import Settings
from models.models import Email

router = APIRouter()


@lru_cache()
def get_settings():
    return Settings()


@router.post('/send_email')
async def send_email(email: Email, settings: Annotated[Settings, Depends(get_settings)]):
    email_regex_pattern = r'^[\w+\.]+@([\w+]+\.)+[\w+]{2,4}$'
    message = MIMEText(email.message, "plain")
    message["Subject"] = email.subject
    message["From"] = settings.sender_email
    if re.match(email_regex_pattern, email.to):
        with smtplib.SMTP_SSL('smtp.mail.ru', 465) as server:
            server.login(settings.sender_email, settings.sender_password)
            server.sendmail(settings.sender_email, email.to, message.as_string())
            logging.info(
                "Sent email to %s with subject '%s' and message: '%s'" % (email.to, email.subject, email.message)
            )
            return {'status': 'success'}
    logging.error("Incorrect email: %s" % email.to)
    raise HTTPException(status_code=400, detail='Incorrect email')
