from django.db import models

class Task(models.Model):
    Title=models.CharField(max_length=20)
    Description=models.TextField(blank=False)
    Due_Date=models.DateField(blank=False)
    Completed=models.BooleanField(default=False)


    def __str__(self):
        return self.Title 
