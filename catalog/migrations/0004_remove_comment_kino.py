# Generated by Django 4.2.5 on 2023-10-18 21:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='kino',
        ),
    ]
