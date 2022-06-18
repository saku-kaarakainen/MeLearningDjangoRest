from django.db import models

# As you can see, logs are stored in the database in this application.
# The logs are stored in the database in a custom model, 
# because they are planned to be viewed in the app UI.
class Log(models.Model):
  
  # Reference to the related database model
  # The value can be for example "user", "org", "file" or "log"
  db_model = models.CharField(max_length=500)

  # Tells what kind of event is the log row about.
  # It can be for example "upload", "download", "login" or "logoff"
  event = models.CharField(max_length=500)

  timestamp = models.DateTimeField(auto_now_add=True, editable=False, null=False, blank=False)
  