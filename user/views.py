
from django.shortcuts import render
from .decorators import admin_required, user_required

@admin_required
def admin_view(request):
    # Only admin can access this view

    context = {
        'title':'admin',
    }
    return render(request, 'user/admin.html', context)

@user_required
def user_view(request):
    # Regular users can access this view

    context = {
        'title':'page',
    }
    return render(request, 'user/page.html', context)
