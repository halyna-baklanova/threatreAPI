# Generated by Django 5.1.4 on 2025-01-13 07:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("theatre", "0004_rename_rows_theatrehall_row_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="theatrehall",
            old_name="row",
            new_name="rows",
        ),
    ]
