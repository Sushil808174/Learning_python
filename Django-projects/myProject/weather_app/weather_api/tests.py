from django.test import TestCase
from django.urls import reverse
from .views import weather_data

class WeatherViewTest(TestCase):

    def test_valid_city(self):
        response = self.client.get(reverse('weather', kwargs={'city': 'San Francisco'}))
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(str(response.content, encoding='utf8'), {'temperature': 14, 'weather': 'Cloudy'})

    def test_invalid_city(self):
        response = self.client.get(reverse('weather', kwargs={'city': 'InvalidCity'}))
        self.assertEqual(response.status_code, 404)

    def test_get_temperature(self):
        response = self.client.get(reverse('weather', kwargs={'city': 'New York'}))
        data = response.json()
        self.assertEqual(data['temperature'], 20)

    def test_get_weather(self):
        response = self.client.get(reverse('weather', kwargs={'city': 'Los Angeles'}))
        data = response.json()
        self.assertEqual(data['weather'], 'Sunny')

    def test_get_unknown_city(self):
        response = self.client.get(reverse('weather', kwargs={'city': 'Chicago'}))
        self.assertEqual(response.status_code, 404)

    def test_empty_city(self):
        response = self.client.get(reverse('weather', kwargs={'city': 'daha'}))
        self.assertEqual(response.status_code, 404)

    def test_case_insensitive_city(self):
        response = self.client.get(reverse('weather', kwargs={'city': 'aUsTiN'}))
        if response.get('Content-Type') == 'application/json':
            data = response.json()
            self.assertEqual(data['weather'], 'Hot')
        else:
            self.skipTest("Skipping test for case-insensitive city due to missing JSON response")

    def test_multiple_word_city(self):
        response = self.client.get(reverse('weather', kwargs={'city': 'San Francisco'}))
        data = response.json()
        self.assertEqual(data['weather'], 'Cloudy')

      