# Generated by Django 2.2.1 on 2019-05-13 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0027_auto_20190513_1903'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='book',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='book',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.Book'),
        ),
    ]
