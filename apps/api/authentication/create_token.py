from typing import Type

import jwt
from django.db import models

from apps.api.authentication.utils import ALGORITHM, SECRET_NAME


class CreateToken:
    """
    Params:
        object: models django
        algorithms: str -> ALGORITHM, default values
        secret: str -> SECRET_NAME, default values
        payload_user: dict -> Payload contructor para construir el token
        token: str -> Token Construido

    Funcciones:
        No accesibles:
            __generate_payload: Genera un diccionario con lo necesario para crear el token
            __create_token: Crear el token con la informacion disponible

        Accesibles:
            execute: llama a los metodos y retorna el token:str

    """

    def __init__(self, object):
        super(CreateToken, self).__init__()
        self.obj: Type[models.Model] = object
        self.algorithms: str = ALGORITHM
        self.secret: str = SECRET_NAME
        self.payload_user: dict = dict()
        self.token: str = ""

    def __generate_payload(self) -> None:
        _array = {"identification": self.obj.personal_id, "uuid": str(self.obj.uuid)}
        self.payload_user = _array

    def __create_token(self) -> None:
        _token = jwt.encode(self.payload_user, self.secret, algorithm=self.algorithms)
        self.token = _token

    @property
    def execute(self) -> str:
        try:
            self.__generate_payload()
        except Exception as e:
            raise ValueError(e)

        try:
            self.__create_token()
        except Exception as e:
            raise ValueError(e)

        return self.token
