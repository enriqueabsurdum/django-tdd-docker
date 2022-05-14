"""Common views."""

# Django
from django.http import JsonResponse


def ping_pong(request):
    """Ping pong function based views."""

    data = {"ping": "pong!"}
    return JsonResponse(data)
