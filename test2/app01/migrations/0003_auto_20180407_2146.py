# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_auto_20180407_2129'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookinfo',
            old_name='coment',
            new_name='comment',
        ),
        migrations.RenameField(
            model_name='bookinfo',
            old_name='resd',
            new_name='read',
        ),
    ]
