# -*- coding:utf-8 -*-
# @Author : dengzhi
# @Time : 2020/8/7 10:55
from django.db import models


class BaseModel(models.Model):
    """模型抽象基类"""
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now_add=True, verbose_name='更新时间')
    delflag = models.BooleanField(default=False, verbose_name='删除标识')

    class Meta:
        abstract = True  # 设置为抽象类
