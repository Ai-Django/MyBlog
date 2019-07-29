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
