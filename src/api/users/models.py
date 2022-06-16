from django.db import models
from django.contrib.auth.models import User
from api.orgs.models import Org

"""
  Represents the user in the API.
"""
class ApiUser(User):
  org = models.ForeignKey(Org)