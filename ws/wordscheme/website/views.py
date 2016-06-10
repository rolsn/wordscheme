from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_http_methods
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as _login
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

from website.forms import RegistrationForm, LoginForm
from website.models import Articles

def index(request):
    return render(request, 'website/index.html', {})


@require_http_methods(["GET", "POST"])
def new_registration(request):
    if request.method == "POST":
        regForm = RegistrationForm(request.POST)

        if not regForm.is_valid():
            return render(request, 'website/register.html', {'form': RegistrationForm().as_ul(), 'error': regForm.errors})

        try:
            params = {
                    "username": request.POST['username'],
                    "password": request.POST['password'],
                    "email": request.POST['email']
                }
        except KeyError:
            return HttpResponse("Invalid input.")

        userExists = True if len(User.objects.filter(username=params['username'])) == 1 else False
        emailExists = True if len(User.objects.filter(email=params['email'])) == 1 else False

        if userExists:
            return HttpResponse("Username already taken.")
        if emailExists:
            return HttpResponse("Email already registered.")

        User.objects.create_user(params['username'], params['email'], params['password'])

        return HttpResponseRedirect('/main/')

    if request.method == "GET":
        return render(request, 'website/register.html', {'form': RegistrationForm().as_ul()})


@require_http_methods(["GET", "POST"])
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                _login(request, user)
                return HttpResponseRedirect('/main', {'username': username})
            else:
                return HttpResponse("User %s is disabled." % user.username)
        else:
            return HttpResponse("Invalid username or password.")
    
    if request.method == "GET":
        return render(request, 'website/login.html', {'form': LoginForm().as_ul()})


@login_required
def main(request):
    username = request.user
    uid = User.objects.get(username=username).id
    latest_articles = Articles.objects.filter(user_id=uid).order_by('-date')[:5]

    return render(request, 'website/main.html', {
        "username"  : username,
        "articles"  : latest_articles
        })

def article(request, id):
    article = Articles.objects.get(id=id)

    return HttpResponse("This will eventually show you article #%s." % id)
