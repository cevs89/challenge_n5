from pydantic import BaseModel, EmailStr, Extra


class ReportsInfractionValidator(BaseModel):
    """
    Simple validador, solo permite 1 campos:
    params:
        email: str -> Required: EmailStr con validaciones
        Se envia en la URL

    No Acepta campos que no esten declarados
    """

    email: EmailStr

    class Config:
        extra = Extra.forbid
