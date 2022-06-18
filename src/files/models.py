from statistics import mode
from django.db import models
from orgs.models import Org
from users.models import ApiUser
from django.conf import settings

# Create your models here.
class File(models.Model):
  org = models.ForeignKey(Org, on_delete=models.CASCADE)
  api_user = models.ForeignKey(ApiUser, on_delete=models.CASCADE)
  name = models.CharField(max_length=500)
  
  # TODO: Is this the best way to store file? If yes, remove this comment, otherwise refactor code as needed
  filepath= models.FileField(
        upload_to = settings.FILE_UPLOAD_FOLDER,
        null=True, 
        verbose_name="")

  uploaded       = models.DateTimeField()
  download_count = models.IntegerField()