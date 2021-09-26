from django.db import models

# Create your models here.
class myTodos(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField(max_length=300)
    

    def __str__(self):
        return self.name
    