from django.db import models

PRIORITY=[('Low','LOW'),('Medium','MEDIUM'),('High','HIGH'),]
STATUS=[('pending','PENDING'),('completed','COMPLETED'),]

class Task(models.Model):
    title=models.CharField(max_length=20)
    description=models.TextField()
    duedate=models.DateField()
    priority=models.CharField(max_length=10, choices=PRIORITY, default='Low')
    status=models.CharField(max_length=10, choices=STATUS, default='pending')

    def __str__(self):
        return self.title
