from django.db import models

# Destination model
class Destination(models.Model):

    # category fields
    CATEGORY_CHOICES = [
        ('Beach', 'Beach'),  
        ('Mountain', 'Mountain'),   
        ('City', 'City'),   
        ('Historical', 'Historical'),   
    ]

    # Destination table fields
    name = models.CharField(max_length=100)   
    country = models.CharField(max_length=100)   
    description = models.TextField()   
    best_time_to_visit = models.CharField(max_length=100)   
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)   
    image_url = models.URLField()   
    created_at = models.DateTimeField(auto_now_add=True)   
    updated_at = models.DateTimeField(auto_now=True)  

    def __str__(self):
        return self.name
