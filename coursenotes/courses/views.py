from django.shortcuts import render, redirect, get_object_or_404
from .models import Course, Note
from django.contrib.auth.decorators import login_required
from .forms import CourseForm
from .forms import NoteForm
from django.db.models import Q

@login_required
def course_list(request):
    courses = Course.objects.filter(user=request.user)
    return render(request, 'courses/course_list.html', {'courses': courses})

@login_required
def course_add(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.user = request.user
            course.save()
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, 'courses/course_form.html', {'form': form})

@login_required
def course_edit(request, pk):
    course = get_object_or_404(Course, pk=pk, user=request.user)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm(instance=course)
    return render(request, 'courses/course_form.html', {'form': form})

@login_required
def course_delete(request, pk):
    course = get_object_or_404(Course, pk=pk, user=request.user)
    if request.method == 'POST':
        course.delete()
        return redirect('course_list')
    return render(request, 'courses/course_confirm_delete.html', {'course': course})


# @login_required
# def note_list(request, course_id):
#     course = get_object_or_404(Course, id=course_id, user=request.user)
#     notes = Note.objects.filter(course=course)
#     return render(request, 'courses/note_list.html', {'course': course, 'notes': notes})

# @login_required
# def note_list(request, course_id):
#     course = get_object_or_404(Course, id=course_id, user=request.user)
#     notes = Note.objects.filter(course=course)
#     all_courses = Course.objects.filter(user=request.user)
#     return render(request, 'courses/note_list.html', {
#         'course': course,
#         'notes': notes,
#         'all_courses': all_courses,
#     })

@login_required
def note_list(request, course_id):
    course = get_object_or_404(Course, id=course_id, user=request.user)
    all_courses = Course.objects.filter(user=request.user)

    query = request.GET.get('q', '')
    if query:
        notes = Note.objects.filter(
            Q(course=course),
            Q(title__icontains=query) | Q(content__icontains=query)
        )
    else:
        notes = Note.objects.filter(course=course)

    return render(request, 'courses/note_list.html', {
        'course': course,
        'notes': notes,
        'all_courses': all_courses,
        'query': query,
    })

@login_required
def note_add(request, course_id):
    course = get_object_or_404(Course, id=course_id, user=request.user)
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.course = course
            note.save()
            return redirect('note_list', course_id=course.id)
    else:
        form = NoteForm()
    return render(request, 'courses/note_form.html', {'form': form, 'course': course})

@login_required
def note_edit(request, course_id, note_id):
    note = get_object_or_404(Note, id=note_id, course__user=request.user)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('note_list', course_id=note.course.id)
    else:
        form = NoteForm(instance=note)
    return render(request, 'courses/note_form.html', {'form': form, 'course': note.course})

@login_required
def note_delete(request, course_id, note_id):
    note = get_object_or_404(Note, id=note_id, course__id=course_id, course__user=request.user)
    if request.method == 'POST':
        note.delete()
        return redirect('note_list', course_id=course_id)
    return render(request, 'courses/note_confirm_delete.html', {'note': note})

# def note_delete(request, note_id):
#     note = get_object_or_404(Note, id=note_id, course__user=request.user)
#     if request.method == 'POST':
#         course_id = note.course.id
#         note.delete()
#         return redirect('note_list', course_id=course_id)
#     return render(request, 'courses/note_confirm_delete.html', {'note': note})
