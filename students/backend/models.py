from django.db import models

# Create your models here.

class students(models.Model):
    name = models.CharField(max_length=100)
    rollno = models.CharField(max_length=10)
    email = models.EmailField()
    exam = models.CharField(max_length=50)
    marks = models.CharField(max_length=10)
    phone = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.name} - {self.rollno} - {self.email} - {self.exam}'