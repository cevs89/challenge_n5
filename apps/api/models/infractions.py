from django.db import models

from apps.api.models.base import BaseModel


class Infractions(BaseModel):
    """
    Modelo Representa el registro de una infraccion
    Field Required:
        timestamp: datetime
        comment: str -> Free Text
        vehicle: Foreign
        officer_allowed: Foreign

    Comentarios:
        Quiza este modelo debe manejar status de la infraccion,
        Si esta pagada, no pagada, si fue apelada o cualquier otro status.

        Para la tarea solo se pidio registrar infracciones
    """

    comment = models.TextField(null=True)
    timestamp = models.DateTimeField()
    vehicle = models.ForeignKey(
        "apps_api.Vehicle",
        on_delete=models.CASCADE,
        related_name="infractions_vehicle_related",
    )
    officer_allowed = models.ForeignKey(
        "apps_api.PersonOfficer",
        on_delete=models.CASCADE,
        related_name="infractions_officer_related",
    )

    class Meta:
        verbose_name = "Infractions"
        verbose_name_plural = "Infractions"

    def __str__(self):
        return f"{self.vehicle.person.name_person} | {self.vehicle.patent}"
