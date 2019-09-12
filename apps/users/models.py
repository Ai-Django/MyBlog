from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.


class UserPro(AbstractUser):
    GENDER = {
        ("male", "男"),
        ("female", "女"),
    }
    name = models.CharField(max_length=10, default="", verbose_name="昵称")
    birthday = models.DateTimeField(default=datetime.now, verbose_name="出生年月")
    gender = models.CharField(max_length=5, choices=GENDER, default="男")
    mobile = models.CharField(max_length=11, default="", verbose_name="电话")
    image = models.ImageField(max_length=100, default="", upload_to="users/%Y/%m", blank=True, verbose_name="用户图像")

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20, verbose_name="验证码")
    email = models.EmailField(max_length=50, verbose_name="邮箱")
    send_type = models.CharField(verbose_name="验证码类型", choices=(("register", "注册"), ("forget", "找回密码"),
                                                                ("update_email", "修改邮箱")), max_length=20)
    send_time = models.DateTimeField(verbose_name="发送时间", default=datetime.now)

    class Meta:
        verbose_name = "邮箱验证码"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{0}({1})'.format(self.code, self.email)