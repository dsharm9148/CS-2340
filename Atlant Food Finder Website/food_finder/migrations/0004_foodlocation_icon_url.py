# Generated by Django 5.1.1 on 2024-09-30 20:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("food_finder", "0003_alter_foodlocation_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="foodlocation",
            name="icon_url",
            field=models.URLField(blank=True, null=True),
        ),
    ]