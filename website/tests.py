from django.test import TestCase
from django.utils import timezone
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.db.models.query import QuerySet

from website.models import Articles, Guilds, GuildMemberships
from website.views import format_urlname
from website.guilds import *

class ModelTests(TestCase):
    def setUp(self):
        self.uid = 'testuser'
        User.objects.create_user(self.uid, password='testpass')
        User.objects.create_user('testuser2', password='testpass')
        self.user = User.objects.get(username=self.uid)
        Articles.objects.create(
                user_id         = self.user,
                date            = timezone.now(),
                article_text    = "Lorem ipsum",
                subject         = "Test Subject 01",
                urlname         = format_urlname("Test Subject 01")
                )
        create_guild(self.user, "Test Guild", "A test guild for the rest of us")
        self.guild = Guilds.objects.get(name="Test Guild")

    def test_can_view_article(self):
        article = Articles.objects.get(id=1)
        user2 = User.objects.get(username='testuser2')

        self.assertTrue(article.can_view_article(self.user))
        self.assertFalse(article.can_view_article(user2))
        
        article.allowed_users.add(user2)
        self.assertTrue(article.can_view_article(user2))

        article.allowed_users.remove(user2)
        self.assertFalse(article.can_view_article(user2))
        join_guild(user2, self.guild.id)
        article.allowed_guilds.add(self.guild)
        self.assertTrue(article.can_view_article(user2))


class GuildModuleTests(TestCase):
    def setUp(self):
        self.uid = 'testuser'
        User.objects.create_user(self.uid, password='testpass')
        User.objects.create_user('testuser2', password='testpass')
        self.gid = create_guild(self.uid, 'Test', "A test guild")

    def getUser(self):
        return User.objects.get(username=self.uid)

    def test_id_generator_length(self):
        """Generate guild IDs and check their length."""
        for i in xrange(1, 50):
            gid = generate_guild_id()
            self.assertEqual(len(str(gid)), 8)
            self.assertIsInstance(gid, int)

    def test_create_guild(self):
        self.assertIsInstance(self.gid, int)

    def test_guild_duplicate_names(self):
        self.assertRaises(IntegrityError, create_guild, self.uid, 'Test')

    def test_guild_memberships(self):
        user = User.objects.get(username=self.uid)
        self.assertIsInstance(list_guild_memberships(self.uid), QuerySet)

    def test_guild_leaderships(self):
        user = self.getUser()
        self.assertIsInstance(list_guild_leaderships(self.uid), QuerySet)

    def test_list_members(self):
        self.assertIsInstance(list_members(self.gid), QuerySet)

    def test_join_guild(self):
        membership = join_guild('testuser2', self.gid)
        self.assertIsInstance(membership, GuildMemberships)

    def test_leave_guild(self):
        membership = join_guild('testuser2', self.gid)
        self.assertTrue(delete_user_from_guild('testuser2', self.gid))

    def test_last_user_leaving_guild(self):
        self.assertRaises(LastUserInGuildError, delete_user_from_guild, self.uid, self.gid)

    def test_leader_leaving_guild(self):
        join_guild('testuser2', self.gid)
        self.assertRaises(UserIsGuildLeaderError, delete_user_from_guild, self.uid, self.gid)

    def test_disbanding_guild(self):
        gid = create_guild(self.uid, 'Test, Inc.', "")
        self.assertTrue(disband_guild(gid))
