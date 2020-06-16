# Generated by Django 3.0 on 2020-06-16 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('multiply', '0010_auto_20200531_0416'),
    ]

    operations = [
        migrations.RenameField(
            model_name='genericfile',
            old_name='csv',
            new_name='csv_active',
        ),
        migrations.RemoveField(
            model_name='genericfile',
            name='file',
        ),
        migrations.AddField(
            model_name='genericfile',
            name='csv_sold',
            field=models.BooleanField(default=False),
        ),
    ]