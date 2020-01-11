
from django.contrib.auth.models import AbstractUser
from django.db import models

class CusetomUser(AbstractUser):
    # is_intern = models.BooleanField(default=True)
    is_student = models.BooleanField('student status', default=False)
    is_teacher = models.BooleanField('teacher status', default=False)
