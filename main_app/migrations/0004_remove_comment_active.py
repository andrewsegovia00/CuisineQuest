# Generated by Django 4.2.3 on 2023-08-01 21:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='active',
        ),
    ]
