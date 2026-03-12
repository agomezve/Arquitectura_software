
from django.urls import path
from . import views

urlpatterns = [
    path('ejemplo/', views.vista_ejemplo, name='HolaMundo'),
    path('ejemplo2/', views.vista_ejemplo2, name='hola victor'),

    path('saludo/<str:nombre>/', views.saludo, name='saludo'), # Acceder con /saludo/Juan/

    path('usuario/<int:id>/', views.obtener_usuario, name='obtener_usuario'), #Acceder con /usuario/5/

    path('usuario/<str:valor>/', views.string_view, name='string_view'), # Accedercon /string/HolaMundo/
    
    path('integer/<int:valor>/', views.integer_view, name='integer_view'), #Acceder con /integer/42/

    path('slug/<slug:valor>/', views.slug_view, name='slug_view'), # Acceder con /slug/hola-mundo-123/

    path('uuid/<uuid:valor>/', views.uuid_view, name='uuid_view'), # Acceder con /uuid/123e4567-e89b-12d3-a456-426614174000/

    path('path/<path:valor>/', views.path_view, name='path_view'), # Acceder con /path/mi/carpeta/archivo/

    path('validar/', views.validar_datos, name='validar_datos'),


    path('solo-post/', views.solo_post, name='solo_post'),  # Solo acepta POST
    path('solo-get/', views.solo_get, name='solo_get'),  # Solo acepta GET
    path('solo-put/', views.solo_put, name='solo_put'),  # Solo acepta PUT
    path('solo-patch/', views.solo_patch, name='solo_patch'),  # Solo acepta PATCH
    path('solo-delete/', views.solo_delete, name='solo_delete'),  # Solo acepta DELETE
]

