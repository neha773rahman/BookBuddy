# Generated by Django 5.2.4 on 2025-07-03 19:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_remove_book_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='progress',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.book'),
        ),
        migrations.AlterField(
            model_name='progress',
            name='percent_completed',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='progress',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
