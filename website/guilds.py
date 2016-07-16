from django.utils import timezone
from django.contrib.auth.models import User

from random import randrange

from website.models import Guilds, GuildMemberships

class GuildException(Exception):
    def __init__(self, *args, **kwargs):
        super(GuildException, self).__init__(*args, **kwargs)

class LastUserInGuildError(GuildException):
    def __init__(self, *args, **kwargs):
        super(LastUserInGuildError, self).__init__(*args, **kwargs)

class UserIsGuildLeaderError(GuildException):
    def __init__(self, *args, **kwargs):
        super(UserIsGuildLeaderError, self).__init__(*args, **kwargs)

class PermissionDeniedError(GuildException):
    def __init__(self, *args, **kwargs):
        super(PermissionDeniedError, self).__init__(*args, **kwargs)


def generate_guild_id():
    """Generate an 8-byte integer to be used as a guild's primary key."""
    gid = randrange(10**7, 10**8-1)

    return gid if len(Guilds.objects.filter(id=gid)) == 0 else generate_guild_id()

def create_guild(leader, name, description=""):
    """Creates a new guild and adds the leader as a member.
    Returns the new guild's ID if successful."""
    try:
        user = User.objects.get(username=leader)
        guild = Guilds(id=generate_guild_id(),
                leader=user,
                name=name,
                description=description,
                date=timezone.now()
                )
        guild.save()

        membership = GuildMemberships(user_id=user, guild_id=guild, date=timezone.now())
        membership.save()

        return guild.id
    except Exception as e:
        raise e

def list_guild_memberships(username):
    """List all guilds a given username belongs to."""
    try:
        user = User.objects.get(username=username)
        return GuildMemberships.objects.filter(user_id=user)
    except Exception as e:
        raise e

def list_guild_leaderships(username):
    """List all guilds led by the given username."""
    try:
        user = User.objects.get(username=username)
        return Guilds.objects.filter(leader=user)
    except Exception as e:
        raise e

def list_members(guild_id):
    """List all members of a given guild."""
    try:
        return GuildMemberships.objects.filter(guild_id=guild_id)
    except Exception as e:
        raise e

def guild_leader(gid):
    """Returns the leader of a given guild."""
    try:
        guild = Guilds.objects.get(id=gid)
        return guild.leader
    except Exception as e:
        raise e

def join_guild(user, guild_id):
    """Adds a user to a given guild ID. Returns the new membership instance if successful."""
    try:
        user = User.objects.get(username=user)
        guild = Guilds.objects.get(id=guild_id)
        membership = GuildMemberships(guild_id=guild, user_id=user, date=timezone.now())
        membership.save()

        return membership
    except Exception as e:
        raise e

def delete_user_from_guild(username, guild_id):
    """Deletes a user from a given guild."""
    try:
        user = User.objects.get(username=username)
        guild = Guilds.objects.get(id=guild_id)
        membership = GuildMemberships.objects.filter(guild_id=guild, user_id=user)
    except Exception as e:
        raise e

    if len(GuildMemberships.objects.filter(guild_id=guild)) == 1:
        raise LastUserInGuildError

    if guild_leader(guild_id) != username:
        membership.delete()
        return True
    else:
        raise UserIsGuildLeaderError

def promote_to_leader(user, guild_id):
    """Replaces the old guild leader with the given user.
    The old leader retains guild membership."""
    pass

def delete_guild(guild_id):
    """Disbands a guild."""
    try:
        guild = Guilds.objects.get(id=guild_id)
        members = GuildMemberships.objects.filter(guild_id=guild)

        for i in members:
            i.delete()

        guild.delete()

        return True
    except Exception as e:
        raise e
