from django.db import models

# Create your models here.

class HealthProblem(models.Model):
    name = models.CharField(max_length=200)
    grade = models.IntegerField(choices=((1, 1), (2, 2)))

    def __str__(self):
        return '%s, %d' % (self.name, self.grade)

class Client(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other')
    )

    name = models.CharField(max_length=200)
    birth_date = models.DateField()
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default='Other')
    health_problem = models.ManyToManyField(HealthProblem)
    created_at = models.DateTimeField(auto_now_add=True)
    att_at = models.DateTimeField(auto_now=True)
