from django.db import models
class TeacherInfo(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    date_of_joining = models.DateField()
    
    def __str__(self):
        return self.name


# Create your models here.
class Teacherinfo(models.Model):
    name = models.TextField(max_length=100)
    email = models.EmailField(unique=True)
    date_of_joining = models.DateField()

    def __str__(self):
        return self.name
