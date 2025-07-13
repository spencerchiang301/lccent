from django.contrib.auth.decorators import login_required
from courses.models import Course, Note
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.utils.http import url_has_allowed_host_and_scheme
from django.conf import settings

def login_view(request):
    form = AuthenticationForm(request, data=request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.get_user()
        login(request, user)
        next_url = request.GET.get('next')
        if next_url and url_has_allowed_host_and_scheme(next_url, request.get_host()):
            return redirect(next_url)
        return redirect('dashboard')
    return render(request, 'accounts/login.html', {'form': form})

def register_view(request):
    form = UserCreationForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('dashboard')
    return render(request, 'accounts/register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect("login")

# @login_required
# def dashboard(request):
#     return render(request, "accounts/dashboard.html", {"user": request.user})


@login_required
def dashboard(request):
    # Session 中紀錄登入次數
    count = request.session.get('visit_count', 0)
    request.session['visit_count'] = count + 1

    course_count = Course.objects.filter(user=request.user).count()
    note_count = Note.objects.filter(course__user=request.user).count()
    latest_note = Note.objects.filter(course__user=request.user).order_by('-created_at').first()

    return render(request, 'accounts/dashboard.html', {
        'user': request.user,
        'visit_count': count + 1,
        'course_count': course_count,
        'note_count': note_count,
        'latest_note': latest_note
    })