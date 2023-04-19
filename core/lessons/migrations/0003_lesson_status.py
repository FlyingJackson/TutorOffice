# Generated by Django 4.1.6 on 2023-04-19 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0002_alter_homework_lesson'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='status',
            field=models.CharField(choices=[('planned', 'public'), ('canceled', 'private'), ('done', 'done')], default='planned', max_length=10, verbose_name='Статус'),
        ),
    ]