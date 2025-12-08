from django.db import models
class Teacherinfo(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    date_of_joining = models.DateField()
    
    def __str__(self):
        return self.name



