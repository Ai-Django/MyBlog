from django.contrib import admin


# Register your models here.
from .models import UserPro, EmailVerifyRecord


class UserProAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'name', 'gender', "mobile", 'birthday')


class EmailVerifyRecordAdmin(admin.ModelAdmin):
    list_display = ('code', 'email', 'send_type', 'send_time')


admin.site.register(UserPro, UserProAdmin)
admin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
