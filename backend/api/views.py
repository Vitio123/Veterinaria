# api/views.py
from django.http import JsonResponse


def prueba_api(request):
    return JsonResponse({"mensaje": "¡Hola desde Django REST!"})
