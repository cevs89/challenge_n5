from django.core.exceptions import ValidationError
from django.test import TestCase

from apps.api.models import PersonCitizen, Vehicle


class TestCreateVehicle(TestCase):
    """
    Probar funcionalidad del Modelo: Vehicle
    """

    def setUp(self):
        PersonCitizen.objects.create(
            name_person="carlos Velazquez",
            email_person="carlos.velazquez@example.com",
        )
        self.query_person = PersonCitizen.objects.get(
            email_person="carlos.velazquez@example.com"
        )

    def test_with_mandatory_fields(self):

        try:
            vehicle = Vehicle.objects.create(patent="KZY447", person=self.query_person)
            vehicle.full_clean()
            vehicle.save()
        except ValidationError:
            self.fail()

        else:
            self.assertIsInstance(vehicle, Vehicle)
            self.assertIsInstance(vehicle.person, PersonCitizen)
            self.assertEqual(vehicle.patent, "KZY447")
            self.assertEqual(vehicle.vehicle_type, "car")
            self.assertIsNone(vehicle.brand)
            self.assertIsNone(vehicle.color)

    def test_with_all_fields_specified(self):
        try:
            vehicle = Vehicle.objects.create(
                patent="KZY447",
                person=self.query_person,
                vehicle_type="car",
                brand="Volkswagen",
                color="Gris",
            )
            vehicle.full_clean()
            vehicle.save()
        except ValidationError:
            self.fail()
        else:
            self.assertIsInstance(vehicle, Vehicle)
            self.assertIsInstance(vehicle.person, PersonCitizen)
            self.assertEqual(vehicle.patent, "KZY447")
            self.assertEqual(vehicle.vehicle_type, "car")
            self.assertEqual(vehicle.brand, "Volkswagen")
            self.assertEqual(vehicle.color, "Gris")
