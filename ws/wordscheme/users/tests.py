from django.test import TestCase
from django.utils import timezone

from users.models import Users

create_user_defaults = {
        "username": "lola",
        "password": "7f3bee1ab3d",
        "reg_date": timezone.now(),
        "email": "lola@example.com"
        }

def create_user(username, password, reg_date, email):
    Users.objects.create(username=username, password=password, reg_date=reg_date, email=email)


class UsersTestCase(TestCase):
    def test_user_made(self):
        create_user(**create_user_defaults)
        user = Users.objects.get(username="lola")
        self.assertEqual(user.username, "lola")
