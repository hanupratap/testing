# Generated by Django 2.2.2 on 2019-06-24 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memslab', '0023_auto_20190624_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='experience_in_years',
            field=models.PositiveIntegerField(default=0),
        ),
    ]