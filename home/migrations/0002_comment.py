# Generated by Django 5.0 on 2023-12-26 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField(default='username')),
                ('comment', models.TextField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
