# Generated by Django 2.2.1 on 2019-05-09 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_auto_20190509_1600'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name': 'Book', 'verbose_name_plural': 'Books'},
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'verbose_name': 'Review', 'verbose_name_plural': 'Reviews'},
        ),
    ]
