from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
# Create your models here.

class CustomUser(AbstractUser):
    dob = models.DateField(null=True, blank=True)
    student_id = models.CharField(max_length=15, null=True, blank=True)
    course_name = models.CharField(max_length=255, null=True, blank=True)
    department = models.CharField(max_length=255, null=True, blank=True)
    year_of_admission = models.CharField(max_length=4, null=True, blank=True)
    year_of_passing = models.CharField(max_length=4, null=True, blank=True)

    objects = UserManager()
    search_fields = ("student_id",)
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.email
    