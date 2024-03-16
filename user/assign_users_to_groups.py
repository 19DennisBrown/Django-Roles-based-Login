
from django.contrib.auth.models import Group
from .models import CustomUser

# Get the Users group
users_group = Group.objects.get(name='Users')

# Assign users to the Users group
users = CustomUser.objects.filter(is_admin=False)
users_group.user_set.add(*users)
