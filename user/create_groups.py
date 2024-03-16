
from django.contrib.auth.models import Group
from .models import CustomUser

# Create groups
admin_group, created = Group.objects.get_or_create(name='Admin')
user_group, created = Group.objects.get_or_create(name='User')

# Create users
admin_user = CustomUser.objects.create_user(username='admin', password='admin')
admin_user.is_admin = True
admin_user.save()
admin_user.groups.add(admin_group)

# Similarly, create other users and assign them to the 'User' group
