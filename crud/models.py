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
# Adding User Model's Childs
# Instructor model
class Instructor (User):
    full_time = models.BooleanField(default=True)
    total_learners = models.IntegerField()

    # Create a toString method for object string representation
    def __str__(self):
        return "First name: " + self.first_name + ", " + \
                "Last name: " + self.last_name + ", " + \
                "Is Full time: " + str(self.self.full_time) + ", " + \
                "Total learners: " + str(self.total_learners)
        
# create a Course model which has a Many-To-Many relationship to Instructor model, defined
# by the reference field instructors
# Course model
class Course (models.Model):
    name = models.CharField(null = False, max_length=30, default='online course')
    description = models.CharField(max_length=500)

    # Many-to-Many relationship to Instructor Model
    instructors = models.ManyToManyField(Instructor)

    # Create a toString method for object string representation
    def __str__(self):
        return "Name: " + self.name + ", " + \
                "Description: " + self.description