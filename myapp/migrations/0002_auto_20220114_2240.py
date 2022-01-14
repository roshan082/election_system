# Generated by Django 3.2.9 on 2022-01-14 16:55

import autoslug.fields
from django.db import migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='voted',
            old_name='user',
            new_name='voting_user',
        ),
        migrations.AddField(
            model_name='event',
            name='slug',
            field=autoslug.fields.AutoSlugField(default=django.utils.timezone.now, editable=False, populate_from='title'),
            preserve_default=False,
        ),
    ]
