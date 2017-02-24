from django.db import models


# Create your models here.

class Dreamreal(models.Model):
    website = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    phone_number = models.IntegerField()
    online = models.ForeignKey('Online')

    class Meta:
        db_table = "dreamreal"


class Online(models.Model):
    domain = models.CharField(max_length=50)

    class Meta:
        db_table = "online"
