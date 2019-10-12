from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Classes, Subject
from groups.models import StudyGroup
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

@login_required(login_url='/login/')
def index(request):
    classes = Classes.objects.all()
    subjects = Subject.objects.all().order_by('title')
    context = {'classes': classes, 'subjects': subjects}
    return render(request, "classes/index.html", context)

def class_detail(request, pk):
    classes = get_object_or_404(Classes, pk=pk)
    context = {'classes': classes}
    return render(request, 'classes/class_detail.html', context)

def join_group(request, pk):
    new_group = get_object_or_404(StudyGroup, pk=pk)
    if (new_group.current_size == new_group.max_size):
        return HttpResponseRedirect(reverse('classes:index'))
    groups_ = request.user.userinfo.groups.all()
    for group_ in groups_:
        if (group_ == new_group):
            return HttpResponseRedirect(reverse('groups:detail', args=[pk]))
    setattr(new_group, 'current_size', new_group.current_size+1)
    new_group.save()
    request.user.userinfo.groups.add(new_group)
    return redirect(f'/groups/{pk}')

class ClassesCreateView(LoginRequiredMixin, CreateView):
    model = Classes
    template_name = 'classes/classes_form.html'
    fields = ['title', 'subject', 'course_number']
    success_url = '/classes/'

    def form_valid(self, form):
        return super().form_valid(form)

class SubjectCreateView(LoginRequiredMixin, CreateView):
    model = Subject
    template_name = 'classes/subject_form.html'
    fields = ['title']
    success_url = '/classes/'

    def form_valid(self, form):
        return super().form_valid(form)

def filter_by_subject(request, pk):
    _subject = get_object_or_404(Subject, pk=pk)
    classes_in_subject = Classes.objects.filter(subject=_subject)
    subjects = Subject.objects.all().order_by('title')
    context = {'classes': classes_in_subject, 'subjects': subjects}
    return render(request, "classes/index.html", context)


