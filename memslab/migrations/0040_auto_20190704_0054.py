# Generated by Django 2.2.2 on 2019-07-03 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memslab', '0039_auto_20190704_0051'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='person_1',
            new_name='Person1',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='person_2',
            new_name='Person2',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='person_3',
            new_name='Person3',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='Person_4',
            new_name='Person4',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='Person_5',
            new_name='Person5',
        ),
        migrations.AlterField(
            model_name='project',
            name='sponsoring_agency',
            field=models.CharField(default='', max_length=200),
        ),
    ]