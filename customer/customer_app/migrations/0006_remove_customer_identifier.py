# Generated by Django 5.0.1 on 2024-02-18 06:48

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("customer_app", "0005_alter_customer_identifier"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customer",
            name="identifier",
        ),
    ]
