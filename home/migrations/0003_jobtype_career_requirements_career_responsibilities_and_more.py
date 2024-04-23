# Generated by Django 5.0.4 on 2024-04-20 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0002_carousel_client"),
    ]

    operations = [
        migrations.CreateModel(
            name="JobType",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=125)),
            ],
        ),
        migrations.AddField(
            model_name="career",
            name="requirements",
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="career",
            name="responsibilities",
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="career",
            name="job_type",
            field=models.ManyToManyField(to="home.jobtype"),
        ),
    ]