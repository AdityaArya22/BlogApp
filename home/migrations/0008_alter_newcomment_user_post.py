# Generated by Django 5.0 on 2023-12-27 10:04

import builtins
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_newcomment_user_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newcomment',
            name='user_post',
            field=models.ForeignKey(default=builtins.id, on_delete=django.db.models.deletion.CASCADE, to='home.userdata'),
        ),
    ]
