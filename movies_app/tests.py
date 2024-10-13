from django.test import TestCase
from django.urls import reverse
from rest_framework import status

# Create your tests here.

class RequestCounterTest(TestCase):
  def test_get_request_count(self):
    response=self.client.get(reverse('request-count'))
    self.assertEqual(response.status_code,status.HTTP_200_OK)
  
  def test_reset_request_count(self):
    self.client.post(reverse('request-count/reset'))
    response=self.client.get(reverse('request-count'))
    self.assertEqual(response.data['requests'],0)