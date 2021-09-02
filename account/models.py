from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    SEX_CHOICES = (
        ('male', 'Мужской'),
        ('female', 'Женский'),
        ('other', 'Другое')
    )
    email = models.EmailField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=80, blank=True)
    activation_code = models.CharField(max_length=8, blank=True)
    sex = models.CharField(max_length=20, choices=SEX_CHOICES, blank=True)
    image = models.ImageField(upload_to='profile_photo', blank=True, null=True)
    birthdate = models.DateField(null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        if User.username:
            return self.username
        else:
            return f'{self.name} {self.last_name}'

    def create_activation_code(self):
        from django.utils.crypto import get_random_string
        code = get_random_string(6, '0123456789')
        self.activation_code = code
        self.save()

