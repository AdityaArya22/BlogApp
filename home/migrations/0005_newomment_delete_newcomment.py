# Generated by Django 5.0 on 2023-12-27 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_newcomment_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='newomment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField(default='username')),
                ('comment', models.TextField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='newComment',
        ),
    ]
