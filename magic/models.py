from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    # extends Django's built-in AbstractUser class
    # adding optional fields for additional user info
    bio = models.TextField(max_length=500, blank=True, null=True)
    location = models.CharField(max_length=30, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.username


class Collection(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Card(models.Model):
    NEAR_MINT = 'NM'
    POOR = 'PR'
    MINT = 'MT'
    GOOD = 'GD'

    CONDITION_CHOICES = [
        (NEAR_MINT, 'Near Mint'),
        (POOR, 'Poor'),
        (MINT, 'Mint'),
        (GOOD, 'Good')
    ]

    name = models.CharField(max_length=200)
    edition = models.CharField(max_length=3)
    condition = models.CharField(
        max_length=2,          
        choices=CONDITION_CHOICES
    )
    language = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    # automatically time stamp when a record is created
    date_updated = models.DateTimeField(auto_now=True)
    # automatically time stamp when a record is saved (updated) 
    release_date = models.DateField(blank=True, null=True)
    # fields are required unless we explicitly make them 
    # optional with blank=True, null=True
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null=True)
    # this article is helpful for implementing image fields https://ordinarycoders.com/blog/article/django-file-image-uploads
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, related_name='cards', blank=True, null=True)

    def __str__(self):
        return f'{self.name} held by {self.owner}'
