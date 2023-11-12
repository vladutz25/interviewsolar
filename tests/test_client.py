from unittest import TestCase

import responses

from geolocator.client import Client


class TestClient(TestCase):
    def setUp(self):
        self.client = Client("55ed295c61dc67819348c27739e6b597")

    def test_gets_the_geolocation_information(self):
        expected_url = f"{self.base_url}?q=51.5128,-0.0918&limit=10&appid=55ed295c61dc67819348c27739e6b597"

        response_body = [
            {
                "name": "City of London",
                "lat": 51.5128,
                "lon": -0.0918,
                "country": "GB"
            }
        ]

        responses.add(responses.GET, expected_url, json=response_body, status=200)

        response = self.client.get(51.5128, -0.0918)

        self.assertEqual(len(responses.calls), 1)
        self.assertEqual(response, response_body)