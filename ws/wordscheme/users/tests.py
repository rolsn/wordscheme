from django.test import TestCase
from django.utils import timezone

from users.models import Users

def create_user():
    now = timezone.now()

    Users.objects.create(
        username="lola", 
        password="764efa883ddc1e",
        reg_date=now,
        email="lola@example.com"
        )

class UsersTestCase(TestCase):
    def test_user_made(self):
        create_user()
        user = Users.objects.get(username="lola")
        self.assertEqual(user.username, "lola")
