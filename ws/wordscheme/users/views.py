from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_http_methods
from django.utils import timezone

from users.models import Users

@require_http_methods(["GET", "POST"])
def new_registration(request):
    method = request.method
    
    if method == "POST":
        try:
            params = {
                    "username": request.POST['username'],
                    "password": request.POST['password'],
                    "email": request.POST['email']
                }
        except KeyError:
            return HttpResponse("Invalid input.")

        userExists = True if len(Users.objects.filter(username=params['username'])) == 1 else False
        emailExists = True if len(Users.objects.filter(email=params['email'])) == 1 else False

        if userExists:
            return HttpResponse("Username already taken.")
        if emailExists:
            return HttpResponse("Email already registered.")

        params['reg_date'] = timezone.now()
        Users.objects.create(**params)

    return render(request, 'users/register.html', {})
