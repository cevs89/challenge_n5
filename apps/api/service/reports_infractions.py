from typing import Type, TypeVar

from django.db.models import Model

from apps.api.models import Infractions, PersonCitizen

T = TypeVar("T", bound=Model)


class ReportsInfractionService:
    """
    Esta clase representa la logica

    params:
        _data: models by pydantic
    """

    def find(self, _data: Type[T]) -> Type[Model]:
        # find person with this email _data.email
        try:
            query_person = PersonCitizen.objects.get(email_person=_data.email)
        except query_person.MultipleObjectsReturned:
            raise ValueError(
                f"Email: {_data.email} exists several times in the models, you need to fix it"
            )
        except PersonCitizen.DoesNotExist:
            raise ValueError(f"Email: {_data.email} Doesn't exists")

        # Find all infractions for this person query_person
        query_report = Infractions.objects.filter(
            vehicle__person=query_person, is_active=True
        )
        return query_report
