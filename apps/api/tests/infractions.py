from datetime import datetime

from django.core.exceptions import ValidationError
from django.test import TestCase

from apps.api.models import Infractions, PersonCitizen, PersonOfficer, Vehicle


class TestCreateInfractions(TestCase):
    """
    Probar funcionalidad del Modelo: Infractions
    """

    def setUp(self):
        _person = PersonCitizen.objects.create(
            name_person="carlos Velazquez",
            email_person="carlos.velazquez@example.com",
        )
        _vehicle = Vehicle.objects.create(patent="KZY447", person=_person)
        _officer = PersonOfficer.objects.create(
            name_officer="Officer Charles", personal_id=18398451
        )

        self.vehicle = _vehicle
        self.officer = _officer

    def test_with_mandatory_fields(self):
        try:
            infraction = Infractions.objects.create(
                comment="Motivo de la infraccion, es requerido",
                timestamp="2023-01-01 15:30",
                vehicle=self.vehicle,
                officer_allowed=self.officer,
            )
            infraction.full_clean()
            infraction.save()
        except ValidationError:
            self.fail()

        else:
            self.assertIsInstance(infraction, Infractions)
            self.assertIsInstance(infraction.vehicle, Vehicle)
            self.assertIsInstance(infraction.officer_allowed, PersonOfficer)
            self.assertEqual(type(infraction.timestamp), datetime)

    def test_date_wrong_format_timestamp(self):
        with self.assertRaises(ValidationError):
            infraction = Infractions.objects.create(
                comment="Motivo de la infraccion, es requerido",
                timestamp="2023$01",
                vehicle=self.vehicle,
                officer_allowed=self.officer,
            )
            infraction.full_clean()
