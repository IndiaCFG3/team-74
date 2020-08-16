from django.db import models
from django.utils import timezone
# Create your models here.

class Student(models.Model):
    id = models.AutoField(primary_key=True)

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

    section = models.CharField(max_length=10,null = True)
    school = models.CharField(max_length = 10, null = True)
    organization = models.CharField(max_length = 200,null = True)

    name=models.CharField(max_length=200)
    gender=models.CharField(max_length=200,choices=GENDER)
    academic=models.CharField(max_length=200,choices=ACADEMIC)
    observed=models.CharField(max_length=200,choices=OBSERVE)
    assess=models.CharField(max_length=10)
    
    def __str__(self):
        return self.name


class Entry(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    B11 = models.BooleanField(default = False)
    B12 = models.BooleanField(default = False)
    B13 = models.BooleanField(default = False)
    B14 = models.BooleanField(default = False)
    
    T11 = models.BooleanField(default = False)
    T12 = models.BooleanField(default = False)
    T13 = models.BooleanField(default = False)
    T14 = models.BooleanField(default = False)
    
    V11 = models.BooleanField(default = False)
    V12 = models.BooleanField(default = False)
    
    BT11 = models.TextField(max_length = 200, null = True)
    BT12 = models.TextField(max_length = 200, null = True)
    BT13 = models.TextField(max_length = 200, null = True)
    BT14 = models.TextField(max_length = 200, null = True)
    
    TT11 = models.TextField(max_length = 200, null = True)
    TT12 = models.TextField(max_length = 200, null = True)
    TT13 = models.TextField(max_length = 200, null = True)
    TT14 = models.TextField(max_length = 200, null = True)
    
    VT11 = models.TextField(max_length = 200, null = True)
    VT12 = models.TextField(max_length = 200, null = True)
    
    date_posted = models.DateTimeField(default = timezone.now)
