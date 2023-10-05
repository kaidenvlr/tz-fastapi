from pydantic import BaseModel


class Email(BaseModel):
    to: str
    subject: str
    message: str
