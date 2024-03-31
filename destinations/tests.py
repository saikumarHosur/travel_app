from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import Destination

class DestinationAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_destination_list_create(self):
        url = reverse('destination-list-create')
        data = {'name': 'Test Destination', 'location': 'Test Location'}
        
        # Test unauthenticated access
        self.client.force_authenticate(user=None)
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        # Test authenticated access
        self.api_authentication()
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Destination.objects.count(), 1)
        self.assertEqual(Destination.objects.get().name, 'Test Destination')

        # Test validation error
        # Name is required
        data.pop('name')  
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_destination_retrieve_update_destroy(self):
        destination = Destination.objects.create(name='Test Destination', location='Test Location')
        url = reverse('destination-detail', args=[destination.id])
        updated_data = {'name': 'Updated Destination', 'location': 'Updated Location'}

        # Test unauthenticated access
        self.client.force_authenticate(user=None)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        # Test authenticated access
        self.api_authentication()
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test Destination')

        # Test update
        response = self.client.put(url, updated_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Destination.objects.get().name, 'Updated Destination')

        # Test partial update
        response = self.client.patch(url, {'name': 'Patched Destination'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Destination.objects.get().name, 'Patched Destination')

        # Test delete
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Destination.objects.count(), 0)

    def test_exception_handling(self):
        non_existent_url = reverse('destination-detail', args=[1000])  # Non-existent ID
        response = self.client.get(non_existent_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        unauthorized_url = reverse('destination-list-create')
        self.client.credentials()  # Clear authentication
        response = self.client.get(unauthorized_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
