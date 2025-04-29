from django.db import models
from django.utils.timezone import now

# Define your models from here:
# User model 
class User (models.Model):
    first_name = models.CharField(null=False, max_length=30, default='john')
    last_name = models.CharField(null=false, max_length=30, default='doe')
    dob = models.DateField(null=True)

# Create a toString method for object string representation
def __str__(self):
    return self.first_name + " " + self.last_name

