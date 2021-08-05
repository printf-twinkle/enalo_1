from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.utils import timezone
from rest_framework_simplejwt.tokens import AccessToken
from django.conf import settings
# Create your models here.

class CustomUser(AbstractUser):
    dob = models.DateField(null=True)
    student_id = models.CharField(max_length=15, null=True, blank=True)
    course_name = models.CharField(max_length=255, null=True, blank=True)
    department = models.CharField(max_length=255, null=True, blank=True)
    year_of_admission = models.CharField(max_length=4, null=True, blank=True)
    year_of_passing = models.CharField(max_length=4, null=True, blank=True)
    last_login = models.DateTimeField(default=timezone.now)

    objects = UserManager()
    search_fields = ("student_id",)
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.email

    @property
    def token(self):
        return self._generate_jwt_token()

    def _generate_jwt_token(self):
        return str(AccessToken.for_user(self))
    