from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    APP_NAME: str = "fastapi-tortoise-skeleton"
    DB_URL: str = Field(default="")
    TOKEN_KEY: str = Field(default="")
    AES_KEY: str = Field(default="")

    class Config:
        env_file = ".env"


settings = Settings()

TORTOISE_ORM = {
    "connections": {"default": f"{settings.DB_URL}/BackendDB"},
    "apps": {
        "models": {
            "models": [
                "aerich.models",
                "models.event",
                "models.user_order",
                "models.user",
                "models.admin_user",
            ],
            "default_connection": "default",
        },
    },
    "use_tz": False,
    "timezone": "Asia/Seoul",
}
