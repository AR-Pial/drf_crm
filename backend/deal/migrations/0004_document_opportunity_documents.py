# Generated by Django 4.2.3 on 2023-08-21 15:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('deal', '0003_alter_opportunity_agent_alter_opportunity_manager'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(null=True, upload_to='project_docs/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='documents', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'documents',
            },
        ),
        migrations.AddField(
            model_name='opportunity',
            name='documents',
            field=models.ManyToManyField(blank=True, to='deal.document'),
        ),
    ]
