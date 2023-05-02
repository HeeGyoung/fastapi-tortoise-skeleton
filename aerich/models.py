from tortoise import Model, fields

from aerich.coder import decoder, encoder

MAX_VERSION_LENGTH = 255
MAX_APP_LENGTH = 100


class Aerich(Model):
    id: int = fields.IntField(pk=True)
    version: str = fields.CharField(max_length=MAX_VERSION_LENGTH)
    app: str = fields.CharField(max_length=MAX_APP_LENGTH)
    content: object = fields.JSONField(encoder=encoder, decoder=decoder)

    class Meta:
        ordering = ["-id"]
