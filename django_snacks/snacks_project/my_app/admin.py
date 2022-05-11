from django.contrib import admin
from .models import Thing,CoolThing
from django.db import models
# Register your models here.

@admin.register(Thing)
class AdminThing(admin.ModelAdmin):

    pass

    
@admin.register(CoolThing)
class AdminCoolThing(admin.ModelAdmin):
    
    list_display=('name','price','is_cool')
    pass

