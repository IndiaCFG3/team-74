from django.db import models
from django.utils import timezone
# Create your models here.

class Student(models.Model):
    
    GENDER=[
    ('male','male'),
    ('female','female'),
    ]
    ACADEMIC=[
    ('higher','higher'),
    ('average','average'),
    ('lower','lower'),
    ]
    OBSERVE=[
    ('high','high'),
    ('low','low'),
    ]
    name=models.CharField(max_length=200)
    gender=models.CharField(max_length=200,choices=GENDER)
    academic=models.CharField(max_length=200,choices=ACADEMIC)
    observed=models.CharField(max_length=200,choices=OBSERVE)
    assess=models.CharField(max_length=10)
    def __str__(self):
        return self.name


class Entry(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    B11 = models.BooleanField(default = True)
    BT1 = models.TextField()
    B12 = models.BooleanField(default = True)
    B13 = models.BooleanField(default = True)
    B14 = models.BooleanField(default = True)
    T11 = models.BooleanField(default = True)
    T13 = models.BooleanField(default = True)
    T14 = models.BooleanField(default = True)
    V11 = models.BooleanField(default = True)
    V12 = models.BooleanField(default = True)

    date_posted = models.DateTimeField(default = timezone.now)
    