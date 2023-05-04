from django.db import models

class Status(models.TextChoices):
    DRAFT = 'draft','DRAFT',
    PUBLIC = 'public','PUBLIC',

class ListModel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length = 100,choices = Status.choices,default=Status.DRAFT)
    
    def __str__(self):
        return self.name
    