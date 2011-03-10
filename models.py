from django.db import models

class SC2Replay(models.Model):
    filename = models.CharField(max_length=255)
