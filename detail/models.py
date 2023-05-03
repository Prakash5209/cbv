from django.db import models

class Books(models.Model):
    title = models.CharField(max_length = 255)
    slug = models.SlugField(null=True)
    description = models.TextField()
    
    def __str__(self):
        return self.title