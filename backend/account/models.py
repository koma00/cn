from django.db import models
from django.conf import settings


class Profile(models.Model):
    SEX_CHOICES = (
        ('none', 'none'),
        ('male', 'male'),
        ('female', 'female')
    )

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    sex = models.CharField(max_length=20, choices=SEX_CHOICES, default='none')
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)
