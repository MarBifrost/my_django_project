from django.contrib import admin

# Register your models here.
from .models import CustomUser
from order.models import UserCart

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff')
    list_filter = ('is_staff', "is_active")
    search_fields = ('username', 'email')


class UserCartAdmin(admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ('user_username',)


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(UserCart, UserCartAdmin)