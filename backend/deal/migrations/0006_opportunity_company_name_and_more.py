# Generated by Django 4.2.3 on 2023-10-07 19:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('deal', '0005_remove_opportunity_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='opportunity',
            name='company_name',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='opportunitydocument',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='documents', to=settings.AUTH_USER_MODEL),
        ),
    ]
