from django.db import models
from django.contrib.auth.models import User

GENDER_CHOICE = (
    ('M','Man'),
    ('W','Woman')
)
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICE)
    age = models.IntegerField()


