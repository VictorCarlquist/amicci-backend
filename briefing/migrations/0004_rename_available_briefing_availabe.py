# Generated by Django 4.2.11 on 2024-04-25 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('briefing', '0003_rename_available_date_briefing_available'),
    ]

    operations = [
        migrations.RenameField(
            model_name='briefing',
            old_name='available',
            new_name='availabe',
        ),
    ]
