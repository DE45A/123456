# Generated by Django 3.2.7 on 2021-10-30 08:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('haato', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='miku',
            name='y',
        ),
    ]
