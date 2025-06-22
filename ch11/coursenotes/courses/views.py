from importlib.resources import read_text

from .models import Course, Note
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CourseForm

def course_list(request):
    courses = Course.objects.filter(user=request.user)
    return render(request, 'courses/course_list.html',{'courses': courses})

def course_add(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.user = request.user
            course.save()
            return redirect("course_list")
    else:
        form = CourseForm()
    return render(request, "courses/course_form.html", {'form':form})

def course_edit(request):
    pass

def course_delete(request):
    pass

def note_list(request):
    pass

def note_add(request):
    pass

def note_edit(request):
    pass

def note_delete(request):
    pass