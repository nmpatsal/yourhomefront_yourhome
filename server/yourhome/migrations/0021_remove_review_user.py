# Generated by Django 2.0.1 on 2018-02-12 02:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yourhome', '0020_auto_20180212_0425'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='user',
        ),
    ]