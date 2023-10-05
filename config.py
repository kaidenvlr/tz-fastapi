from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    sender_email: str
    sender_password: str

    model_config = SettingsConfigDict(env_file=".env")
