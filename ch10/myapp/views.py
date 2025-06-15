from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import get_user_model

# Create your views here.
def index(request):
    return render(request, "index.html", {'name':'jack'})

def hello(request, name):
    return render(request, "hello.html", {'name':name})

def question(request, id):
    return render(request, "question.html", {'id':id})

def about(request):
    return HttpResponse("about page")

def admin_user_list(request):
    User = get_user_model()
    admin_users = User.objects.filter(is_superuser=True)

    return render(request, 'admin_user_list.html', {
        'admin_users': admin_users
    })


