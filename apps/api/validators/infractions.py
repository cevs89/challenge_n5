from datetime import datetime

from pydantic import BaseModel, Extra


class InfractionValidator(BaseModel):
    """
    Simple validador, solo permite 3 campos:
    params:
        patent: str -> Required
            AAA333
        timestamp: datetime -> Required
            "2023-02-15 15:30"

        comment: str -> Required
            "texto libre, para comentarios"

    No Acepta campos que no esten declarados
    """

    patent: str
    timestamp: datetime
    comment: str

    class Config:
        extra = Extra.forbid
