from django.db import models
from django.contrib.auth.models import User, UserManager
from orgs.models import Org

# Create your models here.
class ApiUser(User):
    org = models.ForeignKey(Org, on_delete=models.CASCADE)

    objects = UserManager()