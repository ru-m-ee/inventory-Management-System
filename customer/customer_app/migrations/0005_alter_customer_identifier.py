# Generated by Django 5.0.1 on 2024-02-18 06:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("customer_app", "0004_customer_identifier"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customer",
            name="identifier",
            field=models.IntegerField(),
        ),
    ]