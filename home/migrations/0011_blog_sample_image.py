# Generated by Django 5.0.4 on 2024-05-12 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0010_rename_title_blog_name_remove_blog_created_at_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="blog",
            name="sample_image",
            field=models.ImageField(
                default=1, help_text="This is just for sample usage", upload_to="blog/"
            ),
            preserve_default=False,
        ),
    ]