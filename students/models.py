from django.db import models

class Student(models.Model):
    COURSE_CHOICES = [
        ('CS', 'Computer Science'),
        ('ENG', 'Engineering'),
        ('BUS', 'Business'),
    ]
    
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    course = models.CharField(max_length=3, choices=COURSE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name