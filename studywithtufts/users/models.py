from django.db import models
from django.conf import settings
from classes.models import Classes
from groups.models import StudyGroup

class UserInfo(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    groups = models.ManyToManyField(StudyGroup, blank=True)
    classes = models.ManyToManyField(Classes, blank=True)

    def __str__(self):
        return self.user.username
