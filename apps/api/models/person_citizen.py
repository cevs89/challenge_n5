from django.db import models

from apps.api.models.base import BaseModel


class PersonCitizen(BaseModel):
    """
    Modelo Representa a una persona

    Person:
        name_person: str
        email_person: str
            EmailField: Tiene la validacion incluida EmailValidator

    """

    name_person = models.CharField(max_length=60, null=False)
    email_person = models.EmailField(max_length=255, null=False)

    class Meta:
        verbose_name = "Person"
        verbose_name_plural = "Person Citizen"

    def __str__(self):
        return self.email_person
