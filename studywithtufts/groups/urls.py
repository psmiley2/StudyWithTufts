from django.urls import path, include
from . import views

app_name = 'groups'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/<int:pk>', views.StudyGroupCreateView.as_view(), name='add_group'),
    path('add_post/<int:pk>', views.PostCreateView.as_view(), name='add_post'),
    path('add_comment/<int:pk>', views.CommentCreateView.as_view(), name='add_comment'),
    path('leave_group/<int:student_pk>/<int:group_pk>', views.remove_from_group, name='leave_group'),



    path('<int:pk>/post/<int:pk_2>', views.post_detail, name="post_detail"),
    path('<int:pk>', views.detail, name='detail'),
]
