from django.db import models
from django.contrib import admin

class carinventory (models. Model):
    cid=models.CharField(max_length=20, help_text="Card ID")
    name=models.CharField(max_length=100)
    car_number = models.IntegerField()
    contact=models.IntegerField()
    email = models.EmailField()

class carAdmin(admin.ModelAdmin):
    list_display=('cid', 'name', 'car_number', 'contact', 'email')

