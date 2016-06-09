from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_http_methods

from users.models import Users

@require_http_methods(["GET", "POST"])
def new_registration(request):
    method = request.method
    
    if method == "POST":
        print "POST!"
        try:
            username = request.POST['username']
            password = request.POST['password']
            email = request.POST['email']
        except KeyError:
            HttpResponse("Invalid input.")

        userExists = True if len(Users.objects.filter(username=username)) == 1 else False

        if userExists:
            HttpResponse("Username already taken.")

    return render(request, 'users/register.html', {})
