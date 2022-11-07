# Generated by Django 4.1.2 on 2022-10-28 06:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("categories", "0001_initial"),
        ("rooms", "0002_alter_amenity_options_room_name_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="room",
            name="categories",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="categories.category",
            ),
        ),
    ]
