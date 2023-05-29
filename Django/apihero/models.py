from django.db import models
import uuid
# Create your models here.
class Hero(models.Model):
    id = uuid.uuid4().hex
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)

    def __str__(self):
        return self.name
