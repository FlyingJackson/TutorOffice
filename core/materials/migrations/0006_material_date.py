# Generated by Django 4.1.6 on 2023-05-12 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0005_alter_material_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='date',
            field=models.DateField(auto_now=True, verbose_name='дата'),
        ),
    ]
