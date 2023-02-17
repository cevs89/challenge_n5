import re
from typing import Tuple, Type

from django.db import models
from rest_framework import authentication, exceptions

import apps.api.models as model
from apps.api.authentication.validate_token import ValidationsToken


class TokenAuthOfficer(authentication.BaseAuthentication):
    """
    Custom Class
        Quise personalizar la autenticación del usuario officer, ya que no utilice
        el modelo User, me pareció innecesario, ya que debía hacer registros en la tabla User
        los cuales no tendrían uso, eso seria data basura.

        Personalice la autenticación siguiendo la documentación oficial:
        https://www.django-rest-framework.org/api-guide/authentication/#example
    """

    def __init__(self, *args, **kwargs):
        self.regex_bearer: Type[re] = re.compile(r"^[Bb]earer (.*)$")
        self.queryset: Type[models.Model] = model.PersonOfficer
        self.value_decode: str = ""

    def authenticate(self, request) -> Tuple[Type[models.Model], None]:
        _secret_token = request.META.get("HTTP_AUTHORIZATION")

        if not _secret_token:
            return None

        # Match Bearer into the token and validate
        _match_bearer = self.regex_bearer.match(_secret_token)

        if not _match_bearer:
            raise exceptions.AuthenticationFailed(
                "Authorization header must start with Bearer followed by its token"
            )

        # Split token and get just the jwt token and validations sign with uuid
        _raw_jwt = _match_bearer.groups()[-1]

        _validations = ValidationsToken(_raw_jwt).validate
        if _validations is None:
            raise exceptions.AuthenticationFailed("JWT does not have a valid Key ID")

        # get officer and if everything it's ok, got to is_authenticated
        try:
            queryset = self.queryset.objects.get(uuid=_validations)
        except self.queryset.DoesNotExist:
            raise exceptions.AuthenticationFailed("Unauthorized")

        return (queryset, None)
