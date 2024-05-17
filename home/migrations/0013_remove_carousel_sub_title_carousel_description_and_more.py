# Generated by Django 5.0.4 on 2024-05-16 01:56

import home.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0012_remove_carousel_item_count_remove_carousel_video_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="carousel",
            name="sub_title",
        ),
        migrations.AddField(
            model_name="carousel",
            name="description",
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="carousel",
            name="title",
            field=models.CharField(
                max_length=40, validators=[home.models.validate_title]
            ),
        ),
    ]