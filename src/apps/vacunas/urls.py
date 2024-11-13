from django.urls import path

from . import views

app_name = "vacunas"

urlpatterns = [
    # Lista de Vacunas
    path('lista/', views.Listar.as_view(), name='lista'),
    # Crear nueva Vacuna
    path('nuevo/', views.Nuevo.as_view(), name='nuevo'),
    # Editar una Vacuna
    path('vacuna/<int:pk>/editar/', views.VacunaUpdate.as_view(), name='editar'),
    # Detalle Vacuna
    path('vacuna/<int:pk>/', views.VacunaDetail.as_view(), name='detalle'),
    # Eliminar Vacuna
    path('vacuna/<int:pk>/eliminar', views.VacunaDeleteView.as_view(), name='eliminar')
    # Búsqueda Vacuna
    #TODO: hacer funcionar la búsqueda de vacunas por el nombre al menos
]
