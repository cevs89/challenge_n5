from django.db import models

from apps.api.models.base import BaseModel


class TypeVehicle(models.TextChoices):
    """
    User TextChoices by models:

    Comentarios:
        Tres tipos de vehiculo, pero pueden haber muchos mas (Sin duda alguna),
        Para esto se recomienda usar una tabla de base de datos,
        para su correcta administacion.

        Por ahora no vi necesario crear una tabla para manejar los tipos de autos
    """

    CAR = "car", "Car"
    MOTO = "moto", "Motorcycle"
    BIG_CAR = "cargo", "Cargo truck"


class Vehicle(BaseModel):
    """
    Modelo Representa a un Vehiculo relacionado a una Persona

    Campos requerdos:
        patent: str
        person: Foreign

    Comentarios:
        Campos que debe ser un tabla de base de datos
            brand
            color

        Estos campos deberia ser una tabla de base de datos, para su mejor administacion,
        Por ahora no vi necesario crear una tabla para ello.
    """

    patent = models.CharField(max_length=60, null=False)
    brand = models.CharField(max_length=60, null=True, blank=True)
    color = models.CharField(max_length=60, null=True, blank=True)
    vehicle_type = models.CharField(
        max_length=50, choices=TypeVehicle.choices, default=TypeVehicle.CAR
    )
    person = models.ForeignKey(
        "apps_api.PersonCitizen",
        on_delete=models.CASCADE,
        related_name="person_vehicle_related",
    )

    class Meta:
        verbose_name = "Vehicle"
        verbose_name_plural = "Vehicles"

    def __str__(self):
        return self.patent
