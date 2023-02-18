from django.db import models
from django.contrib.auth.models import AbstractUser


class Student(models.Model):
    id = models.UUIDField(
        primary_key=True,
        unique=True,
        editable=False,
    )
    first_name = models.TextField(
        "Имя",
        max_length=20,
    )
    last_name = models.TextField(
        "Фамилия",
        max_length=20,
    )
    email = models.EmailField(
        "Электронная почта",
        max_length=254,
        unique=True,
    )
    phone = models.TextField(
        "Телефон",
        max_length=14,
        unique=True,
    )
    email_verify = models.BooleanField(
        "Подтвержден e-mail",
        null=True,
        default=False,
    )
    photo = models.ImageField(
        "Фотография",
        upload_to='images/',
        blank=True,
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'
        ordering = ('last_name', 'first_name')


class Teacher(models.Model):
    profile = models.OneToOneField(Student,
                                   related_name='teacher_profile',
                                   on_delete=models.PROTECT)
    student = models.ManyToManyField(Student,
                                     related_name='teachers',
                                     through="TeacherStudent")

    class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учителя'


class TeacherStudent(models.Model):
    """Таблица для ManyToMany связи учитель Teacher и студент Student"""
    teacher_id = models.ForeignKey(
        Teacher,
        related_name='studentM2M',
        on_delete=models.PROTECT,
    )
    student_id = models.ForeignKey(
        Student,
        related_name='teacherM2M',
        null=True,
        on_delete=models.PROTECT,
    )
    first_name = models.TextField(
        "Имя ученика",
        max_length=20,
    )
    last_name = models.TextField(
        "Фамилия ученика",
        max_length=20,
    )
    email = models.EmailField(
        "Электронная почта",
        max_length=254,
        unique=True,
    )
    verify = models.BooleanField(
        "Подтвержденный ученик",
        null=True,
        default=False,
    )
    comment = models.TextField()


class Homework(models.Model):
    """Модель для домашнего задания Homework"""
    title = models.TextField(blank=True,
                             null=True)
    text = models.TextField(blank=True,
                            null=True)
    comment = models.TextField(blank=True,
                               null=True)

    def __str__(self):
        return {self.title}


class Subject(models.Model):
    """Модель для материалов Homework"""
    title = models.TextField(max_length=30,
                             unique=True,
                             db_index=True)

    def __str__(self):
        return {self.title}

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'
        ordering = ('title',)


class Lesson(models.Model):
    """Модель для урока Lesson"""
    teacher_id = models.ForeignKey(
        Student,
        on_delete=models.PROTECT,
    )
    teacher_student_id = models.ForeignKey(
        TeacherStudent,
        on_delete=models.PROTECT,
    )
    date = models.DateTimeField(blank=True)
    start_time = models.TimeField(blank=True)
    end_time = models.TimeField(blank=True)
    subject = models.ForeignKey(
        Subject,
        on_delete=models.PROTECT,
    )
    topic = models.TextField(max_length=40)
    comment = models.TextField(blank=True)
    homework_id = models.ForeignKey(
        Homework,
        on_delete=models.CASCADE,
        blank=True,
    )

    def __str__(self):
        return f'{self.pk} {self.date} {self.start_time}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
        ordering = ('subject', 'teacher_id', 'date', 'start_time')


PUBLIC = 'public'
PRIVATE = 'private'


class Material(models.Model):
    """Модель для материалов Material"""

    TYPECHOICE = [
        (PUBLIC, 'public'),
        (PRIVATE, 'private'),
                  ]

    teacher_id = models.ForeignKey(Teacher,
                                   on_delete=models.PROTECT)
    teacher_student_id = models.ForeignKey(TeacherStudent,
                                           on_delete=models.PROTECT)
    subject = models.ForeignKey(Subject,
                                on_delete=models.PROTECT)
    file = models.FileField(blank=True)
    text = models.TextField(blank=True)
    type = models.CharField(
        max_length=10,
        choices=TYPECHOICE,
        default=PRIVATE,
    )

    def __str__(self):
        return f'{self.subject} {self.text}'

    class Meta:
        verbose_name = 'Материал к уроку'
        verbose_name_plural = 'Материалы'
        ordering = ('subject', 'teacher_id')
