# Generated by Django 3.2.4 on 2021-06-24 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0012_group_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='courses',
            field=models.ManyToManyField(to='course.Course'),
        ),
    ]
