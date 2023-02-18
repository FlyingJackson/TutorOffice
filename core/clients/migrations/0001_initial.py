# Generated by Django 4.1.6 on 2023-02-18 08:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Homework',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True, null=True)),
                ('text', models.TextField(blank=True, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.UUIDField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('first_name', models.TextField(max_length=20, verbose_name='Имя')),
                ('last_name', models.TextField(max_length=20, verbose_name='Фамилия')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Электронная почта')),
                ('phone', models.TextField(max_length=14, unique=True, verbose_name='Телефон')),
                ('email_verify', models.BooleanField(default=False, null=True, verbose_name='Подтвержден e-mail')),
                ('photo', models.ImageField(blank=True, upload_to='images/', verbose_name='Фотография')),
            ],
            options={
                'verbose_name': 'Студент',
                'verbose_name_plural': 'Студенты',
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(db_index=True, max_length=30, unique=True)),
            ],
            options={
                'verbose_name': 'Предмет',
                'verbose_name_plural': 'Предметы',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='teacher_profile', to='clients.student')),
            ],
            options={
                'verbose_name': 'Учитель',
                'verbose_name_plural': 'Учителя',
            },
        ),
        migrations.CreateModel(
            name='TeacherStudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.TextField(max_length=20, verbose_name='Имя ученика')),
                ('last_name', models.TextField(max_length=20, verbose_name='Фамилия ученика')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Электронная почта')),
                ('verify', models.BooleanField(default=False, null=True, verbose_name='Подтвержденный ученик')),
                ('comment', models.TextField()),
                ('student_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='teacherM2M', to='clients.student')),
                ('teacher_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='studentM2M', to='clients.teacher')),
            ],
        ),
        migrations.AddField(
            model_name='teacher',
            name='student',
            field=models.ManyToManyField(related_name='teachers', through='clients.TeacherStudent', to='clients.student'),
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, upload_to='')),
                ('text', models.TextField(blank=True)),
                ('type', models.CharField(choices=[('public', 'public'), ('private', 'private')], default='private', max_length=10)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='clients.subject')),
                ('teacher_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='clients.teacher')),
                ('teacher_student_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='clients.teacherstudent')),
            ],
            options={
                'verbose_name': 'Материал к уроку',
                'verbose_name_plural': 'Материалы',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True)),
                ('start_time', models.TimeField(blank=True)),
                ('end_time', models.TimeField(blank=True)),
                ('topic', models.TextField(max_length=40)),
                ('comment', models.TextField(blank=True)),
                ('homework_id', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='clients.homework')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='clients.subject')),
                ('teacher_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='clients.student')),
                ('teacher_student_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='clients.teacherstudent')),
            ],
            options={
                'verbose_name': 'Урок',
                'verbose_name_plural': 'Уроки',
            },
        ),
    ]
