# Generated by Django 2.2.2 on 2019-07-04 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('memslab', '0043_project_people'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='Person1',
        ),
        migrations.RemoveField(
            model_name='project',
            name='Person2',
        ),
        migrations.RemoveField(
            model_name='project',
            name='Person3',
        ),
        migrations.RemoveField(
            model_name='project',
            name='Person4',
        ),
        migrations.RemoveField(
            model_name='project',
            name='Person5',
        ),
    ]