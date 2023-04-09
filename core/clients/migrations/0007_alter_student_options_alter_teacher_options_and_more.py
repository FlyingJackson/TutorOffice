# Generated by Django 4.1.6 on 2023-04-09 12:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0006_alter_teacherstudent_bind'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ('user',), 'verbose_name': 'Студент', 'verbose_name_plural': 'Студенты'},
        ),
        migrations.AlterModelOptions(
            name='teacher',
            options={'ordering': ('user',), 'verbose_name': 'Учитель', 'verbose_name_plural': 'Учителя'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ('last_name', 'first_name'), 'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
        migrations.AlterField(
            model_name='student',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='student_profile', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='teacher_profile', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
