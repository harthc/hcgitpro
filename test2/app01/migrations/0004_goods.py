# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_auto_20180407_2146'),
    ]

    operations = [
        migrations.CreateModel(
            name='goods',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('title', models.CharField(verbose_name='商品名称', max_length=40)),
                ('comment', models.CharField(verbose_name='商品描述', max_length=256, blank=True)),
                ('show', models.SmallIntegerField(choices=[(1, '上架'), (0, '下架')], default=1, verbose_name='商品状态')),
            ],
        ),
    ]
