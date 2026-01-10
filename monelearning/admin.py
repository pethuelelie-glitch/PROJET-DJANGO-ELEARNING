from django.contrib import admin
# Register your models here.

from .models import Module, Inscription, Cours


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ('titre',)
    search_fields = ('titre',)
    ordering = ('titre',)


@admin.register(Inscription)
class InscriptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'module', 'date')
    list_filter = ('module', 'date')
    search_fields = ('user__username', 'module__titre')
    ordering = ('-date',)


@admin.register(Cours)
class CoursAdmin(admin.ModelAdmin):
    list_display = ('titre', 'module')
    list_filter = ('module',)
    search_fields = ('titre', 'module__titre')
    ordering = ('titre',)
