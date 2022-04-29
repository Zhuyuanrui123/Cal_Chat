from profile.models import Profile, NICKNAME_CHOICES
import random


def create_profile_with_random_nick(user):
    random_name = random.choice(NICKNAME_CHOICES)
    profile = Profile(user=user, nickname=random_name[0])
    profile.save()
    return profile
