# Generated by Django 3.2.9 on 2022-01-02 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_auto_20220102_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voted',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]
