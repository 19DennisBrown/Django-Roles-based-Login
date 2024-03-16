
from .models import CustomUser

# Get the user who will be the admin
admin_user = CustomUser.objects.get(username='admin')

# Set the user as admin
admin_user.is_admin = True
admin_user.save()
