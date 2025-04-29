from django.db import models
from django.utils.timezone import now

# Define your models from here:
# User model 
class User (models.Model):
    first_name = models.CharField(null=False, max_length=30, default='john')
    last_name = models.CharField(null=False, max_length=30, default='doe')
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
                "Is Full time: " + str(self.full_time) + ", " + \
                "Total learners: " + str(self.total_learners)

# Learner model
class Learner(User):
    STUDENT = 'student'
    DEVELOPER = 'developer'
    DATA_SCIENTIST = 'data_scientist'
    DATABASE_ADMIN = 'dba'
    OCCUPATION_CHOICES = [
        (STUDENT, 'Student'),
        (DEVELOPER, 'Developer'),
        (DATA_SCIENTIST, 'Data Scientist'),
        (DATABASE_ADMIN, 'Database Admin')
    ]
    occupation = models.CharField(
        null=False,
        max_length=20,
        choices=OCCUPATION_CHOICES,
        default=STUDENT
    )
    social_link = models.URLField(max_length=200)
    
    #Create a __str__ method returning a string presentation
    def __str__(self):
        return "First name: " + self.first_name + ", " + \
                "Last name: " + self.last_name + ", " + \
                "Occupation: " + self.occupation + ", " + \
                "Social link: " + self.social_link

# create a Course model which has a Many-To-Many relationship to Instructor model, defined
# by the reference field instructors
# Course model
class Course (models.Model):
    name = models.CharField(null = False, max_length=30, default='online course')
    description = models.CharField(max_length=500)

    # Many-to-Many relationship to Instructor Model
    instructors = models.ManyToManyField(Instructor)

    # Many-To-Many relationship with Learner via Enrollment relationship
    learners = models.ManyToManyField(Learner, through='Enrollment')

    # Create a toString method for object string representation
    def __str__(self):
        return "Name: " + self.name + ", " + \
                "Description: " + self.description

# create a Lesson model which has a Many-To-One relationship to Course model, defined
# by course ForeignKey
# Lesson model
class Lesson (models.Model):
    title = models.CharField(null = False, max_length=200, default="title")
    course = models.ForeignKey(Course, null=True, on_delete=models.CASCADE)
    content = models.TimeField()

    # Create a toString method for object string representation
    def __str__(self):
        return "Title: " + self.title + "," + \
            "Content: " + self.content
    
# Enrollment Model
# Enrollment model as a lookup table with additional enrollment info
class Enrollment(models.Model):
    AUDIT = 'audit'
    HONOR = 'honor'
    COURSE_MODES = [
        (AUDIT, 'Audit'),
        (HONOR, 'Honor'),
    ]

    # One_to_Many  relationship to Learner & Course 
    # Add a learner foreign key
    learner = models.ForeignKey(Learner, on_delete=models.CASCADE)
    # Add a course foreign key
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    # Enrollment date
    date_enrolled = models.DateField(default=now)
    # Enrollment mode
    mode = models.CharField(max_length=5, choices=COURSE_MODES, default=AUDIT)