# Generated by Django 4.2.3 on 2023-09-03 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deal', '0004_opportunity_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='opportunity',
            name='title',
        ),
    ]
