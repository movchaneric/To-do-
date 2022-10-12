from django.db import models
#To use User inside Task model with one (User) to Many(Tasks) relationship
from django.contrib.auth.models import User


# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank = True)
    title = models.CharField(max_length=100) 
    description = models.TextField(null = True, blank = True)
    complete = models.BooleanField(default=False,null = True)
    date_created  = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title
    class Meta:
        #explained in geeksforgeeks in meta class django
        ordering = ['complete']