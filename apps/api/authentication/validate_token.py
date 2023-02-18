import jwt
from django.conf import settings


class ValidationsToken:
    """
    Params:
        decode_value: str django
        algorithms: str -> ALGORITHM, default values
        secret: str -> SECRET_NAME, default values
        token: str -> Token Construido

    Funcciones:
        No accesibles:
            __decode_token: Decodifica el token y valida que su firma uuid sea correcta

        Accesibles:
            validate: llama a los metodos y retorna el token:str

    """

    def __init__(self, _token: str):
        super(ValidationsToken, self).__init__()
        self.decode_value: str = None
        self.algorithms: str = settings.ALGORITHM
        self.secret: str = settings.APP_NAME
        self.token: str = _token

    def __decode_token(self) -> None:
        # Decode Jwt
        try:
            _token = jwt.decode(self.token, self.secret, algorithms=self.algorithms)
        except Exception as e:
            raise ValueError("JWT does not have a valid Key ID: " + str(e))

        # Validate sign with uuid
        if "uuid" in _token:
            self.decode_value = _token["uuid"]

    @property
    def validate(self) -> str:
        self.__decode_token()
        return self.decode_value
