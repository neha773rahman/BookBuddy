# Generated by Django 5.2.4 on 2025-07-04 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_alter_progress_percent_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='total_pages',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
