# Generated by Django 5.0.4 on 2024-05-16 02:03

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0013_remove_carousel_sub_title_carousel_description_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="blog",
            name="created_at",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
