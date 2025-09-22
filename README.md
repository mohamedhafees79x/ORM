# Ex02 Django ORM Web Application
# Date:22/09/2025
# AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).


## DESIGN STEPS
## STEP 1:
Clone the problem from GitHub

## STEP 2:
Create a new app in Django project

## STEP 3:
Enter the code for admin.py and models.py

## STEP 4:
Ececute Django admin and create 10 cars in car inventory

# PROGRAM
```
admin.py

from django.contrib import admin
from .models import carinventory, carAdmin
admin.site.register(carinventory, carAdmin)

models.py

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

```


# OUTPUT
![alt text](<Screenshot 2025-09-22 094324.png>)

# RESULT
Thus the program for creating a database using ORM hass been executed successfully
