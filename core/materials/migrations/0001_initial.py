# Generated by Django 4.1.6 on 2023-02-21 12:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
                ('text', models.TextField()),
                ('type', models.CharField(choices=[('public', 'public'), ('private', 'private')], default='private', max_length=10)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='clients.subject')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='materials', to='clients.teacher')),
                ('teacher_student', models.ManyToManyField(related_name='materials', to='clients.teacherstudent')),
            ],
            options={
                'verbose_name': 'Материал',
                'verbose_name_plural': 'Материалы',
                'ordering': ('subject', 'teacher_id'),
            },
        ),
    ]
