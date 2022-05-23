from django.db import models

# Create your models here.


class Fizzbuzz(models.Model):
    num_input = models.IntegerField()

    def __str__(self):
        return str(self.id)


