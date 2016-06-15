from django.utils import timezone

def default(request):
    return {
            current_date    = timezone.now(),
            username        = request.user()
            }

