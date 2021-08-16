from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    phone = models.IntegerField(max_length=12)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name