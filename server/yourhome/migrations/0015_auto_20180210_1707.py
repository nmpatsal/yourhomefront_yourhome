# Generated by Django 2.0.1 on 2018-02-10 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yourhome', '0014_auto_20180210_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='photos',
            field=models.FileField(upload_to='static/assets/img/'),
        ),
    ]
