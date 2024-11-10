from django.contrib import admin

from .models import Vacuna, Dosis

# Register your models here.
admin.site.register(Vacuna)
admin.site.register(Dosis)