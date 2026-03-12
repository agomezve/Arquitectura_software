from django.http import HttpResponse, JsonResponse
import json
import re
import uuid
from django.views.decorators.csrf import csrf_exempt



# Create your views here.
def vista_ejemplo(request):
    return HttpResponse("Hola Mundo")

def vista_ejemplo2(request):
    return HttpResponse("hola victor")

def saludo(request, nombre):
    return HttpResponse(f"Hola, {nombre}!")

def obtener_usuario(request, id):
    return HttpResponse(f"Mostrando información del usuario con ID: {id}")

def string_view(request, valor):
    return HttpResponse(f"String recibido: {valor}")
def integer_view(request, valor):
    return HttpResponse(f"Integer recibido: {valor}")
def slug_view(request, valor):
    return HttpResponse(f"Slug recibido: {valor}")
def uuid_view(request, valor):
    return HttpResponse(f"UUID recibido: {valor}")
def path_view(request, valor):
    return HttpResponse(f"Path recibido: {valor}")

def validar_datos(request):
    try:
        data = request.GET  # También podrías usar json.loads(request.body) si los datos vienen en POST (JSON)

        # Obtener parámetros desde GET o POST
        string_valor = data.get('string')
        integer_valor = data.get('integer')
        slug_valor = data.get('slug')
        uuid_valor = data.get('uuid')
        path_valor = data.get('path')
        email_valor = data.get('email')

        errores = {}

        # Validar String (solo letras y espacios)
        if string_valor and not re.fullmatch(r'^[A-Za-zÁÉÍÓÚáéíóúÑñ ]+$', string_valor):
            errores['string'] = 'El valor debe contener solo letras y espacios'

        # Validar Integer
        if integer_valor and not integer_valor.isdigit():
            errores['integer'] = 'El valor debe ser un número entero'

        # Validar Slug (letras, números, guiones y guiones bajos)
        if slug_valor and not re.fullmatch(r'^[a-zA-Z0-9_-]+$', slug_valor):
            errores['slug'] = 'El slug solo puede contener letras, números, guiones y guiones bajos'

        # Validar UUID
        try:
            if uuid_valor:
                uuid.UUID(uuid_valor, version=4)  # Verifica si es un UUID válido
        except ValueError:
            errores['uuid'] = 'UUID inválido'

        # Validar Path (permite / en la cadena)
        if path_valor and not re.fullmatch(r'^[\w\-/]+$', path_valor):
            errores['path'] = 'El path solo puede contener letras, números, guiones y barras'

        # Validar Email
        if email_valor and not re.fullmatch(r'^[\w\.-]+@[\w\.-]+\.\w{2,4}$', email_valor):
            errores['email'] = 'Correo electrónico inválido'

        # Si hay errores, devolver una respuesta con los detalles
        if errores:
            return JsonResponse({'error': errores}, status=400)

        return JsonResponse({'mensaje': 'Todos los datos son válidos'})

    except json.JSONDecodeError:
        return JsonResponse({'error': 'Formato JSON inválido'}, status=400)
    
@csrf_exempt
def solo_post(request):
    if request.method == 'POST':
        return JsonResponse({'mensaje': 'Solicitud POST recibida correctamente'})
    return JsonResponse({'error': 'Método no permitido'}, status=405)


def solo_get(request):
    if request.method == 'GET':
        return JsonResponse({'mensaje': 'Solicitud GET recibida correctamente'})
    return JsonResponse({'error': 'Método no permitido'}, status=405)

@csrf_exempt
def solo_put(request):
    if request.method == 'PUT':
        return JsonResponse({'mensaje': 'Solicitud PUT recibida correctamente'})
    return JsonResponse({'error': 'Método no permitido'}, status=405)

@csrf_exempt
def solo_patch(request):
    if request.method == 'PATCH':
        return JsonResponse({'mensaje': 'Solicitud PATCH recibida correctamente'})
    return JsonResponse({'error': 'Método no permitido'}, status=405)

@csrf_exempt
def solo_delete(request):
    if request.method == 'DELETE':
        return JsonResponse({'mensaje': 'Solicitud DELETE recibida correctamente'})
    return JsonResponse({'error': 'Método no permitido'}, status=405)