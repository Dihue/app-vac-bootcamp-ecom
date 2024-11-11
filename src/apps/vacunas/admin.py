from django.contrib import admin

from .models import Vacuna, Dosis


class DosisInline(admin.StackedInline):
    model = Dosis
    extra = 0


class VacunaAdmin(admin.ModelAdmin):
    list_display = ['id', 'codigo', 'nombre', 'cant_dosis']
    inlines = [DosisInline]
    search_fields = ('codigo', 'nombre')


admin.site.register(Vacuna, VacunaAdmin)


class DosisAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_vacuna_codigo', 'get_vacuna_nombre', 'nombre', 'orden']
    search_fields = ('vacuna__codigo', 'vacuna__nombre', 'nombre')

    def get_vacuna_codigo(self, obj):
        return obj.vacuna.codigo
    
    get_vacuna_codigo.short_description = "Código Vacuna"

    def get_vacuna_nombre(self, obj):
        return obj.vacuna.nombre
    
    get_vacuna_nombre.short_description = "Nombre Vacuna"


admin.site.register(Dosis, DosisAdmin)