from django import forms
from .models import Classes
from django.contrib.admin import widgets

class ClassForm(forms.ModelForm):

    class Meta:
        model = Classes
        fields = [
            'title',
            'subject',
            'course_number',
        ]
