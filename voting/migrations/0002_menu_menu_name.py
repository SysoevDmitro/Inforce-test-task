# Generated by Django 5.0.6 on 2024-08-12 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("voting", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="menu",
            name="menu_name",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
