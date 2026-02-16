from django.contrib import admin
from .models import Cuisine
from .models import User
# Register your models here.
class CuisineAdmin(admin.ModelAdmin):
    list_display=('name','type','catg')
    search_fields=['name']
    list_filter=['catg']
class UserAdmin(admin.ModelAdmin):
    list_display = ('name','email')
admin.site.register(Cuisine,CuisineAdmin)
admin.site.register(User,UserAdmin)
