# Generated by Django 2.0.1 on 2018-02-10 23:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('yourhome', '0016_auto_20180210_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='review_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='review date'),
        ),
    ]