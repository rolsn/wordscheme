from django.utils import timezone
from django.contrib.auth.models import User

from random import randrange

from website.models import Guilds, GuildMemberships

def generate_guild_id():
    """Generate an 8-byte hex id to be used as a guild's primary key."""
    gid = '%0x' % randrange(16**8)

    return gid if len(Guilds.objects.filter(guild_id=gid)) == 0 else generate_guild_id()

def create_guild(guild_leader, guild_name):
    """Creates a new guild and adds the leader as a member."""
    try:
        user = User.objects.get(username=guild_leader)
        guild = Guilds(guild_id=generate_guild_id(), guild_leader=user, guild_name=guild_name, date=timezone.now())
        guild.save()

        membership = GuildMemberships(user_id=user, guild_id=guild, date=timezone.now())
        membership.save()

        return True
    except Exception as e:
        raise e

def list_guild_memberships(username):
    """List all guilds a given username belongs to."""
    try:
        user = User.objects.get(username=username)
        return GuildMemberships.objects.filter(user_id=user)
    except Exception as e:
        raise e


def list_members(guild):
    """List all members of a given guild."""
    try:
        guild = Guilds.objects.get(guild_name=guild)
        return GuildMemberships.objects.filter(guild_id=guild)
    except Exception as e:
        raise e

def guild_leader(guild_id):
    """Returns the leader of a given guild."""
    try:
        guild = Guilds.objects.get(guild_id=guild_id)
        return guild.guild_leader
    except Exception as e:
        raise e

def add_user_to_guild(user, guild):
    """Adds a user to a given guild."""
    pass

def delete_user_from_guild(user, guild):
    """Deletes a user from a given guild."""
    pass

def delete_guild(guild):
    """Deletes a guild."""
    pass
