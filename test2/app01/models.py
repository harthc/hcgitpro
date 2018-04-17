from django.db import models
from datetime import date
from tinymce.models import HTMLField

# Create your models here.

class BookInfo(models.Model):
    title = models.CharField(max_length=20)
    pub_time = models.DateField()
    read = models.IntegerField(default=0)
    comment = models.IntegerField(default=0)
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class HeroInfo(models.Model):
    name = models.CharField(max_length=20)
    gender = models.BooleanField(default=False)
    comment = models.CharField(max_length=20)
    book = models.ForeignKey('BookInfo')
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.name


# 用来给这个字段提供选择项。如果设置了 choices ，默认表格样式就会显示选择框，而不是标准的文本框
class Goods(models.Model):
    title = models.CharField(max_length=40, verbose_name='商品名称')
    comment = HTMLField(max_length=256, blank=True, verbose_name='商品描述')
    SHOW_CHOICES = (
        (1, '上架'),
        (0, '下架'),
        (2, '看心情')
    )
    show = models.SmallIntegerField(default=1, choices=SHOW_CHOICES, verbose_name='商品状态')

    class Meta(object):
        verbose_name = '商品上架详情'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
