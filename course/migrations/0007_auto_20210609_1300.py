# Generated by Django 3.2.4 on 2021-06-09 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0006_student_group'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='branch',
            options={'verbose_name': 'филиал', 'verbose_name_plural': 'филиалы'},
        ),
        migrations.AlterModelOptions(
            name='group',
            options={'verbose_name': 'группа', 'verbose_name_plural': 'группы'},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name': 'студент', 'verbose_name_plural': 'студенты'},
        ),
    ]