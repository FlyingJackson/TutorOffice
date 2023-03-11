from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from smtplib import SMTPDataError
from rest_framework.response import Response
from rest_framework import status


class Email:
    @staticmethod
    def send_email(request, user, token):
        try:
            domain = get_current_site(request)
            email_subject = 'Подтвердите почту для активации вашего кабинета репетитора'
            message = render_to_string('clients/activate.html',
                                       {'full_name': f"{user.last_name} {user.first_name}",
                                        'domain': domain,
                                        'token': token})
            to_email = user.email
            email = EmailMessage(email_subject, message, to=[to_email],
                                 from_email=settings.EMAIL_HOST_USER)
            email.send()
            return Response({"SUCCESS": "Регистрация прошла успешно! "
                                        "Пожалуйста, подтвердите свою почту!"},
                            status=status.HTTP_200_OK)
        except SMTPDataError as error:
            return Response({"ERROR": "Почта не найдена! " 
                                      "Невозможно отправить сообщение для подтверждения!"},
                            status=status.HTTP_400_BAD_REQUEST)
