# Generated by Django 3.2 on 2024-05-21 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0003_auto_20240521_1514'),
    ]

    operations = [
        migrations.RenameField(
            model_name='achievementcat',
            old_name='achievements',
            new_name='achievement',
        ),
    ]
