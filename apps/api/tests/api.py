import json

from django.core.exceptions import ValidationError
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from apps.api.models import Infractions, PersonCitizen, PersonOfficer, Vehicle


class TestInfractionAPI(TestCase):
    """
    Probar funcionalidad de endpoint: /api/v1/infraction/

    Enviamos peticiones y validamos que todo este segun lo esperado
    """

    def setUp(self):
        _person = PersonCitizen.objects.create(
            name_person="carlos Velazquez",
            email_person="carlos.velazquez@example.com",
        )
        Vehicle.objects.create(patent="KZY447", person=_person)

        _officer = PersonOfficer.objects.create(
            name_officer="Officer Charles", personal_id=18398451
        )
        _data_body = {
            "patent": "KZY447",
            "comment": "Exceso de velocidad Otra vez",
            "timestamp": "2023-02-22 20:30",
        }

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f"Bearer {_officer.token_officer}")
        response = client.post(
            "/api/v1/infraction/",
            json.dumps(_data_body),
            content_type="application/json",
        )

        self.response = response
        self.email_person = _person.email_person
        self.officer = _officer

    def test_request_mandatory_fields(self):
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        self.assertEqual(type(self.response.data), dict)
        self.assertEqual(self.response.data["person"], self.email_person)

    def test_properties_fields(self):
        self.assertTrue("id" in self.response.data)
        self.assertTrue("brand" in self.response.data)
        self.assertTrue("color" in self.response.data)
        self.assertTrue("vehicle_type" in self.response.data)
        self.assertTrue("person" in self.response.data)
        self.assertTrue("officer" in self.response.data)
        self.assertTrue("timestamp" in self.response.data)
        self.assertTrue("comment" in self.response.data)

    def test_save_officer_models(self):
        _queryset = Infractions.objects.get(pk=self.response.data["id"])
        self.assertIsInstance(_queryset.officer_allowed, PersonOfficer)
        self.assertEqual(_queryset.officer_allowed, self.officer)


class TestReportsInfractionAPI(TestCase):
    """
    Probar funcionalidad de endpoint: /api/v1/report/infraction/<email>/

    Enviamos peticiones y validamos que todo este segun lo esperado
    """

    def setUp(self):
        _person = PersonCitizen.objects.create(
            name_person="carlos Velazquez",
            email_person="carlos.velazquez@example.com",
        )

        client = APIClient()
        response = client.get(
            f"/api/v1/report/infraction/{_person.email_person}",
            content_type="application/json",
        )

        self.response = response

    def test_request_mandatory_fields(self):
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        self.assertEqual(type(self.response.data), list)

    def test_invalid_email_send(self):
        with self.assertRaises(ValidationError):
            client = APIClient()
            client.get(
                "/api/v1/report/infraction/dddd", content_type="application/json"
            )

    def test_does_not_exit_email_send(self):
        with self.assertRaises(ValidationError):
            client = APIClient()
            client.get(
                "/api/v1/report/infraction/ramon@example.com",
                content_type="application/json",
            )
