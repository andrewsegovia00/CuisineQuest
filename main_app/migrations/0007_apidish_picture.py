# Generated by Django 4.2.3 on 2023-08-02 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_dish_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='apidish',
            name='picture',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
    ]
