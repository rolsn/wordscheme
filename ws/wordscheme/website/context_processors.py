from django.utils import timezone

def default(request):
    print "wtf", request.user.is_authenticated()
    return {
            "current_datetime"      : timezone.now(),
            "current_user"          : request.user
            }

