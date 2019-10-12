from django import forms
from .models import StudyGroup
from django.contrib.admin import widgets

class ClassForm(forms.ModelForm):

    class Meta:
        model = StudyGroup
        fields = [
            'title',
            'teacher',
            'max_size',
            'mon',
            'tue',
            'wed',
            'thur',
            'fri',
            'sat',
            'sun',
            'monday',
            'tuesday',
            'wednesday',
            'thursday',
            'friday',
            'saturday',
            'sunday',
        ]

class PostForm(forms.ModelForm):

    class Meta:
        model = StudyGroup
        fields = [
            'title',
            'content',
        ]
