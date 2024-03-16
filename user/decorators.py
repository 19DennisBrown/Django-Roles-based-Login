
from django.http import HttpResponseForbidden

def admin_required(view_func):
    """
    Decorator for views that checks whether the user is an admin.
    """
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_admin:
            return HttpResponseForbidden("You are not authorized to access this page.")
        return view_func(request, *args, **kwargs)
    return _wrapped_view

def user_required(view_func):
    """
    Decorator for views that checks whether the user is a regular user.
    """
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated or request.user.is_admin:
            return HttpResponseForbidden("You are not authorized to access this page.")
        return view_func(request, *args, **kwargs)
    return _wrapped_view
