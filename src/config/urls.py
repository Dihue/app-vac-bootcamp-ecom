from django.contrib import admin
from django.contrib.auth import views as views_django
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from . import views


apis_urls = [
    path('vacunaciones/', include('apps.colocacion.routers')),
]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.mi_pagina_inicio, name='inicio'),

    # path('login/', views.login, name='login'),
    # *Uso de libreria django y vista basada en clase
    path('base', views.BaseTemplateView.as_view(), name='base'),

    path('login/', views_django.LoginView.as_view(template_name="login.html"), name='login'),
    path('logout/', views_django.logout_then_login, name="logout"),

    path('error-permisos', views.pagina_error_permisos, name='error_permisos'),

    path('api/v1/', include(apis_urls)),

    # path('usuarios/lista/', views.pagina_usuarios, name='lista_de_usuarios'),
    path('usuarios/', include("apps.usuarios.urls")),
    path("pacientes/", include("apps.pacientes.urls")),
    path("vacunas/", include("apps.vacunas.urls"))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)