# Generated by Django 3.2.23 on 2024-01-26 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('financenews', '0002_rename_update_on_post_updated_on'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='updated_on',
            new_name='update_on',
        ),
    ]
