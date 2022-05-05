from django.contrib import admin
from .models import Pizza

#personnaliser l'interface d'aministration
class PizzaAdmin(admin.ModelAdmin):
    list_display = ('nom', 'ingredients', 'vegetarienne', 'prix')
    search_fields = ['nom']

# Register your models here.
admin.site.register(Pizza, PizzaAdmin)
