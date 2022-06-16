from django.db import models


"""
  Represents the organization in the API.
"""
class Org(models.Model):
  name = models.CharField(max_length=255)

