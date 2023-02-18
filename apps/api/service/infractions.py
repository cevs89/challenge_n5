from typing import Type, TypeVar

from django.db import IntegrityError, transaction
from django.db.models import Model

from apps.api.models import Infractions, Vehicle

T = TypeVar("T", bound=Model)


class InfractionService:
    """
    Esta clase representa la logica

    params:
        _data: models by pydantic
        _requests_user: requests user class
    """

    def save(self, _data: Type[T], _requests_user: Type[T]) -> Type[Model]:
        # find the vehicle with the patent
        try:
            quiery_vehicle = Vehicle.objects.get(patent=_data.patent)
        except Vehicle.DoesNotExist:
            raise ValueError("Vehicle Doesn't exists")

        # Try to save data with transaction.atomic
        try:
            with transaction.atomic():
                save_infraction = Infractions()
                save_infraction.comment = _data.comment
                save_infraction.timestamp = _data.timestamp
                save_infraction.vehicle = quiery_vehicle
                save_infraction.officer_allowed = _requests_user
                save_infraction.save()
        except IntegrityError:
            raise ValueError(
                "Somethings went wrong, when we'd try to save infractions, please try again"
            )

        return save_infraction
