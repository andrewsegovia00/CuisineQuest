# Generated by Django 4.2.3 on 2023-08-02 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_apilist'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='picture',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
    ]
