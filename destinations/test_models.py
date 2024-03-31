from django.test import TestCase

# Importing the Destination model from models.py
from .models import Destination  

class DestinationModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Destination object for testing purposes
        Destination.objects.create(
            name='Goa',
            country='India', 
            description='testing',
            best_time_to_visit='summer',
            category='Beach',
            image_url='https://t4.ftcdn.net/jpg/05/68/63/11/360_F_568631153_ygTLlsjLeVtMrGDSUbqia6VD2GsdbHJx.jpg'
        )

    def test_name_label(self):
        # Destination object with id=1
        destination = Destination.objects.get(id=1)

        # name field
        field_label = destination._meta.get_field('name').verbose_name

        # the name is 'name'
        self.assertEqual(field_label, 'name')

    def test_country_label(self):
        destination = Destination.objects.get(id=1)
        field_label = destination._meta.get_field('country').verbose_name
        self.assertEqual(field_label, 'country')

    def test_category_choices(self):
        destination = Destination.objects.get(id=1)
        valid_categories = ['Beach', 'Mountain', 'City', 'Historical']

        # category of the Destination object is within valid categories
        self.assertIn(destination.category, valid_categories)

    def test_image_url(self):
        destination = Destination.objects.get(id=1)

        # image URL starts with 'http'
        self.assertTrue(destination.image_url.startswith('http'))

    def test_created_at_auto_now_add(self):
        destination = Destination.objects.get(id=1)

        # created_at field is not None
        self.assertIsNotNone(destination.created_at)

    def test_updated_at_auto_now(self):
        destination = Destination.objects.get(id=1)
        
        # updated_at field is not None
        self.assertIsNotNone(destination.updated_at)
