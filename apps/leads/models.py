from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # Custom user model can have additional fields if needed
    pass

class Agent(models.Model):
    """Model representing an agent who can be assigned to leads"""
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=10, blank=True)
    is_default_unassigned = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Lead(models.Model):
    SOURCE_CHOICES = [
        ('web', 'Web'),
        ('phone', 'Phone'),
        ('email', 'Email'),
        ('social_media', 'Social Media'),
        ('referral', 'Referral'),
        ('Property24', 'property24'),
        ('privateproperty', 'privateproperty'),
        ('gumtree', 'gumtree'),
        ('facebook', 'Facebook'),
        ('instagram', 'Instagram'),
        ('twitter', 'Twitter'),
        ('linkedin', 'LinkedIn'),
        ('google_ads', 'Google Ads'),
        ('seo', 'SEO'),
        ('print_media', 'Print Media'),
        ('event', 'Event'),
        ('networking', 'Networking'),
        ('other', 'Other')
    ]
    
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.PositiveIntegerField(default=0)
    address = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    phoned = models.BooleanField(default=False)
    agent = models.ForeignKey(
        Agent, on_delete=models.SET_DEFAULT, default="unassigned")
    source = models.CharField(max_length=100, choices=SOURCE_CHOICES, default='Property24')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"