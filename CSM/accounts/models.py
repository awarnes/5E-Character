from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Member(AbstractUser):
    """
    Includes ability to ask about communication for a member and whether there are front-end admin privilages.
    """

    is_admin = models.BooleanField(default=False)
    ok_to_contact = models.BooleanField(default=False)


