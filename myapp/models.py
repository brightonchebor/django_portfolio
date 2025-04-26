from django.db import models

# Create your models here.
class ContactMe(models.Model):

    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    subject = models.CharField(max_length=500)

    def __str__(self):
        return self.name
