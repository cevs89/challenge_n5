from django.core.exceptions import ValidationError
from django.test import TestCase

from apps.api.models import PersonCitizen


class TestCreatePerson(TestCase):
    """
    Probar funcionalidad del Modelo: PersonCitizen
    """

    def test_with_mandatory_fields(self):
        try:
            person = PersonCitizen.objects.create(
                name_person="carlos Velazquez",
                email_person="carlos.velazquez@example.com",
            )
            person.full_clean()
            person.save()
        except ValidationError:
            self.fail()

        else:
            self.assertIsInstance(person, PersonCitizen)
            self.assertEqual(person.name_person, "carlos Velazquez")
            self.assertEqual(person.email_person, "carlos.velazquez@example.com")

    def test_with_failed_email(self):
        with self.assertRaises(ValidationError):
            person = PersonCitizen.objects.create(
                name_person="carlos Velazquez",
                email_person="carlos.velazquez#example/com",
            )
            person.full_clean()

    def test_limint_max_length_in_name_person(self):
        with self.assertRaises(ValidationError):
            _fake_name = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur condimentum aliquam arcu volutpat lobortis. Pellentesque sit amet lobortis elit, id sodales nulla. Nam id placerat sapien, et placerat metus. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus."
            person = PersonCitizen.objects.create(
                name_person=_fake_name,
                email_person="carlos.velazquez@example.com",
            )
            person.full_clean()
