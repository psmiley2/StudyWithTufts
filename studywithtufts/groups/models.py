from django.db import models
from django.conf import settings
from django.urls import reverse
from classes.models import Classes
from django.urls import reverse
from datetime import datetime
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, Transpose, SmartResize

class StudyGroup(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    teacher = models.CharField(max_length=100, default='')
    classes = models.ForeignKey(Classes, on_delete=models.CASCADE, blank=True)
    max_size = models.IntegerField(default=10)
    current_size = models.IntegerField(default=0)
    mon = models.TimeField(default='00:00')
    tue = models.TimeField(default='00:00')
    wed = models.TimeField(default='00:00')
    thur = models.TimeField(default='00:00')
    fri = models.TimeField(default='00:00')
    sat = models.TimeField(default='00:00')
    sun = models.TimeField(default='00:00')
    monday = models.BooleanField(default=False)
    tuesday = models.BooleanField(default=False)
    wednesday = models.BooleanField(default=False)
    thursday = models.BooleanField(default=False)
    friday = models.BooleanField(default=False)
    saturday = models.BooleanField(default=False)
    sunday = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    group = models.ForeignKey(StudyGroup, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    time_posted = models.DateTimeField(auto_now_add=True, blank=True)
    image = models.ImageField(blank=True, null=True, upload_to='images/')
    image_thumbnail = ImageSpecField(
        source='image',
        processors = [Transpose(),SmartResize(200, 200)],
        format = 'JPEG',
    )
    image_fullsize = ImageSpecField(
        source='image',
        processors = [Transpose()],
    )

    def __str__(self):
        return self.title



class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField(blank=True)
    time_posted = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return str(self.user) + '\'s Comment' + str(self.pk)
