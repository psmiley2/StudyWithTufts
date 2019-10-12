from django.urls import path, include
from . import views

app_name = 'classes'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.ClassesCreateView.as_view(), name='add_class'),
    path('add_subject/', views.SubjectCreateView.as_view(), name='add_subject'),
    path('filter/<int:pk>', views.filter_by_subject, name='filter'),

    path('join/<int:pk>', views.join_group, name='join_group'),
    #add other URLS above
    path('<int:pk>', views.class_detail, name='class_detail'),
]
