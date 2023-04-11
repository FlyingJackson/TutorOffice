from rest_framework.permissions import BasePermission


class IsTeacher(BasePermission):
    """
    Кастомное ограничение прав доступа, проверяющее
    является ли пользователь учителем (имеет профиль)
    """
    def has_permission(self, request, view):
        try:
            return request.user.teacher_profile is not None
        except AttributeError:
            return False
