from django.db import models

from django.db import models
from django.core.validators import MinValueValidator

# Models for the Little Lemon restaurant application

class Menu(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID')
    title = models.CharField(max_length=255, db_column='Title')
    price = models.DecimalField(max_digits=10, decimal_places=2, db_column='Price',
                                validators=[MinValueValidator(0)])
    inventory = models.IntegerField(db_column='Inventory',
                                    validators=[MinValueValidator(0)])

    class Meta:
        db_table = 'Menu'  # nombre de tabla tal cual

    def __str__(self):
        return f"{self.title} (${self.price})"


class Booking(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID')
    name = models.CharField(max_length=255, db_column='Name')
    no_of_guests = models.IntegerField(db_column='No_of_guests',
                                       validators=[MinValueValidator(1)])
    booking_date = models.DateTimeField(db_column='BookingDate')

    class Meta:
        db_table = 'Booking'

    def __str__(self):
        return f"{self.name} @ {self.booking_date:%Y-%m-%d %H:%M}"