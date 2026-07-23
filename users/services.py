from django.conf import settings
from django.core.mail import send_mail


def send_register_email(email):
    send_mail(
        subject='Поздравляем с регистрацией на нашем сервисе',
        message='Вы успешно зарегистрировались на платформе Shelter513СBV',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email]
    )


def send_new_password_email(email, new_password):
    send_mail(
        subject='Сброс пароля',
        message=f'Ваш новый пароль: {new_password}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email]
    )


def send_dog_creation(email, dog_obj):
    send_mail(
        subject='Вы добавили нового питомца',
        message=f'Вы успешно добавили: {dog_obj}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email]
    )