# Generated by Django 5.0 on 2023-12-27 09:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_newomment_delete_newcomment'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='newomment',
            new_name='newComment',
        ),
    ]