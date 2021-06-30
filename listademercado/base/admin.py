from django.contrib import admin

# Register your models here.
from base.models import Marca, Item

admin.site.register(Marca)
admin.site.register(Item)
