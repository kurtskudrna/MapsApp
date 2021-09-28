from django.db import models

# Create your models here.


class Distance(models.Model):
    start_point = models.CharField(max_length=250)
    end_point = models.CharField(max_length=250)
    trip = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.start_point} to {self.end_point} is {self.trip} KM'
