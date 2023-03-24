from rest_framework import serializers
from .models import User, Teacher, Student, Subject
from django.db.transaction import atomic
from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError


# Сериализатор для обработки формы регистрации
class RegisterSerializer(serializers.ModelSerializer):
    is_teacher = serializers.BooleanField(
        required=True,
        write_only=True,
    )
    password = serializers.CharField(
        required=True,
        write_only=True,
        validators=[
            validate_password,
        ]
    )
    password2 = serializers.CharField(
        required=True,
        write_only=True,
    )

    # Поля взяты из .models.User
    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'patronymic_name',
            'last_name',
            'email',
            'phone',
            'is_teacher',
            'password',
            'password2',
        ]

    # Проверка совпадающих паролей в форме регистрации
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise ValidationError({
                'password': 'Пароли не совпадают',
                'password2': 'Пароли не совпадают',
            })
        attrs.pop('password2')
        return attrs

    # Переопределение метода create.
    # В случае ошибочного ввода данных НЕ сохраняет строки в БД
    @atomic
    def create(self, validated_data):
        is_teacher = validated_data.pop('is_teacher')
        password = validated_data.pop('password')
        user = super().create(validated_data)
        user.password = make_password(password)
        user.save()
        if is_teacher:
            Teacher.objects.create(user=user)
        else:
            Student.objects.create(user=user)
        return user


class ChangePasswordSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(required=True, write_only=True)
    new_password = serializers.CharField(required=True, write_only=True)
    repeat_password = serializers.CharField(required=True, write_only=True)

    def update(self, instance, validated_data):

        instance.password = validated_data.get('password', instance.password)

        if not validated_data['new_password']:
            raise serializers.ValidationError({'new_password': 'Не найдено'})

        if not validated_data['old_password']:
            raise serializers.ValidationError({'old_password': 'Не найдено'})

        if not instance.check_password(validated_data['old_password']):
            raise serializers.ValidationError({'old_password': 'Неправильный пароль'})

        if validated_data['new_password'] != validated_data['repeat_password']:
            raise serializers.ValidationError({'passwords': 'Пароли не совпадают'})

        if validated_data['new_password'] == validated_data['repeat_password'] and instance.check_password(
                validated_data['old_password']):
            instance.set_password(validated_data['new_password'])
            instance.save()

            return instance

    class Meta:
        model = User
        fields = ['old_password', 'new_password', 'repeat_password']


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"
