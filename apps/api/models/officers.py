from typing import Type

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.api.authentication import CreateToken
from apps.api.models.base import BaseModel


class PersonOfficer(BaseModel):
    """
    Modelo Representa a un oficial
    Officer:
        campos requeridas:
            name_officer: str
            personal_id: int

        Campo token_officer:
            token_officer: text: str
            Se guardar el token al momento de crear el usuario.
            El token se creara con un servicio personalizado llamado:

            Y este creara un token tipo JWT, y tambien se creara un servicio
            para verificar su validez a la hora de las peticiones

    """

    name_officer = models.CharField(max_length=60, null=False)
    personal_id = models.IntegerField(default=0)
    token_officer = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Officer"
        verbose_name_plural = "Person Officer"

    def __str__(self):
        return self.name_officer


@receiver(post_save, sender=PersonOfficer)
def create_token_access(
    sender: Type[PersonOfficer], instance: PersonOfficer, created=False, **kwargs
) -> None:
    if created:
        _created_token = CreateToken(instance).execute
        instance.token_officer = _created_token
        instance.save()
