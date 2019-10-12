from django.db import models
from django.conf import settings
from django.urls import reverse

class Subject(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Classes(models.Model):
    title = models.CharField(max_length=100)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    course_number = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('to_do:to_do_create')
