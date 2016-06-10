from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_http_methods
from django.utils import timezone

from django.contrib.auth.models import User
from users.forms import RegistrationForm

@require_http_methods(["GET", "POST"])
def new_registration(request):
    if request.method == "POST":
        regForm = RegistrationForm(request.POST)

        if not regForm.is_valid():
            return render(request, 'users/register.html', {'form': RegistrationForm().as_ul(), 'error': regForm.errors})

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

        #params['reg_date'] = timezone.now()
        User.objects.create(**params)

        return HttpResponse("User %s created." % params['username'])

    if request.method == "GET":
        return render(request, 'users/register.html', {'form': RegistrationForm().as_ul()})
