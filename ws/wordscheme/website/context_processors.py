from django.utils import timezone

def default(request):
    return {
            "current_datetime"      : timezone.now(),
            "current_user"          : request.user
            }

