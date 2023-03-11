from django.db import models
from clients.models import User, TeacherStudent, Subject


# Create your models here.


class Homework(models.Model):
    """Модель, описывающая ДЗ к занятию"""
    title = models.TextField()
    text = models.TextField()
    comment = models.TextField(blank=True)

    def __str__(self):
        return {self.title}


class Lesson(models.Model):
    """Модель для занятий"""
    teacher = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
    )
    teacher_student = models.ForeignKey(
        TeacherStudent,
        on_delete=models.PROTECT,
    )
    date = models.DateTimeField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    subject = models.ForeignKey(
        Subject,
        on_delete=models.PROTECT,
    )
    topic = models.TextField(max_length=40, blank=True)
    comment = models.TextField(blank=True)
    homework = models.OneToOneField(
        Homework,
        related_name='lesson',
        on_delete=models.CASCADE,
        blank=True,
    )

    def __str__(self):
        return f'{self.pk} {self.date} {self.start_time}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
        ordering = ('subject', 'teacher_id', 'date', 'start_time')
