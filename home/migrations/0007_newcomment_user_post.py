# Generated by Django 5.0 on 2023-12-27 09:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_rename_newomment_newcomment'),
    ]

    operations = [
        migrations.AddField(
            model_name='newcomment',
            name='user_post',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.userdata'),
        ),
    ]