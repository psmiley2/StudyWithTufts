from django.shortcuts import render, redirect, get_object_or_404
from .models import StudyGroup, Post, Comment
from users.models import UserInfo
from classes.models import Classes
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.db.models import F
from django.http import HttpResponseRedirect

@login_required(login_url='/login/')
def index(request):
    return render(request, "groups/index.html")

def detail(request, pk):
    group = get_object_or_404(StudyGroup, pk=pk)
    context = {'group': group}
    return render(request, 'groups/detail.html', context)

def post_detail(request, pk, pk_2):
    post = get_object_or_404(Post, pk=pk_2)
    context = {'post': post}
    return render(request, 'groups/post_detail.html', context)

class StudyGroupCreateView(LoginRequiredMixin, CreateView):
    model = StudyGroup
    template_name = 'groups/study_group_form.html'
    fields = ['title',
            'teacher',
            'max_size',
            'monday',
            'mon',
            'tuesday',
            'tue',
            'wednesday',
            'wed',
            'thursday',
            'thur',
            'friday',
            'fri',
            'saturday',
            'sat',
            'sunday',
            'sun',]

    success_url = '/classes/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.classes = get_object_or_404(Classes, pk=self.kwargs['pk'])
        self.user.userinfo.add(request.user.userinfo)
        return super().form_valid(form)

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'groups/post_form.html'
    fields = ['title', 'content',
            ]
    success_url = '/groups/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.group = get_object_or_404(StudyGroup, pk=self.kwargs['pk'])
        return super().form_valid(form)

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = 'groups/comment_form.html'
    fields = ['content', ]
    success_url = '/groups/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post = get_object_or_404(Post, pk=self.kwargs['pk'])
        return super().form_valid(form)

def remove_from_group(request, student_pk, group_pk):
    group = get_object_or_404(StudyGroup, pk=group_pk)
    student = get_object_or_404(UserInfo, pk=student_pk)
    StudyGroup.objects.filter(pk=group.pk).update(current_size=F('current_size')-1)
    student.groups.remove(group)
    return HttpResponseRedirect(reverse('groups:index'))
