from django.core.exceptions import ValidationError
from django.test import TestCase

from apps.api.authentication.validate_token import ValidationsToken
from apps.api.models import PersonOfficer


class TestCreateOfficer(TestCase):
    """
    Probar funcionalidad del Modelo: PersonOfficer
    """

    def test_with_mandatory_fields(self):
        try:
            officer = PersonOfficer.objects.create(
                name_officer="Officer Charles", personal_id=18398451
            )
            officer.full_clean()
            officer.save()
        except ValidationError:
            self.fail()

        else:
            _validate_token = ValidationsToken(officer.token_officer).validate

            self.assertIsInstance(officer, PersonOfficer)
            self.assertEqual(officer.name_officer, "Officer Charles")
            self.assertEqual(type(officer.personal_id), int)
            self.assertEqual(officer.personal_id, 18398451)
            self.assertEqual(str(officer.uuid), _validate_token)
            self.assertIsNotNone(officer.token_officer)

    def test_limint_max_length_in_name_officer(self):
        with self.assertRaises(ValidationError):
            _fake_name = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur condimentum aliquam arcu volutpat lobortis. Pellentesque sit amet lobortis elit, id sodales nulla. Nam id placerat sapien, et placerat metus. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus."
            officer = PersonOfficer.objects.create(
                name_officer=_fake_name, personal_id=18398451
            )
            officer.full_clean()


class TestOfficerProperty(TestCase):
    def setUp(self):
        PersonOfficer.objects.create(
            name_officer="Officer Charles", personal_id=18398451
        )

    def test_Officer_property(self):
        officer = PersonOfficer.objects.get(personal_id=18398451)
        self.assertTrue(hasattr(officer, "is_authenticated"))
        self.assertTrue(officer.is_authenticated)
