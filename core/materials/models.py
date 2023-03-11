from django.db import models
from clients.models import Teacher, TeacherStudent, Subject

# Create your models here.

PUBLIC = 'public'
PRIVATE = 'private'


class Material(models.Model):
    """
    Модель для материалов как публичных, так и
    между преподавателем и студентом. При этом есть
    возможность рассылки.
    """

    TYPECHOICE = [
        (PUBLIC, 'public'),
        (PRIVATE, 'private'),
    ]

    teacher = models.ForeignKey(Teacher,
                                related_name='materials',
                                on_delete=models.PROTECT)
    teacher_student = models.ManyToManyField(TeacherStudent,
                                             related_name='materials')
    subject = models.ForeignKey(Subject,
                                on_delete=models.PROTECT)
    file = models.FileField()
    text = models.TextField()
    type = models.CharField(
        max_length=10,
        choices=TYPECHOICE,
        default=PRIVATE,
    )

    def __str__(self):
        return f'{self.subject} {self.text}'

    class Meta:
        verbose_name = 'Материал'
        verbose_name_plural = 'Материалы'
        ordering = ('subject', 'teacher_id')
