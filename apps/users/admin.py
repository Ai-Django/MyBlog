from django.contrib import admin


# Register your models here.
from .models import UserPro


class UserProAdmin(admin.ModelAdmin):
    list_display = ('name', 'gender', "mobile", 'birthday')


admin.site.register(UserPro, UserProAdmin)
