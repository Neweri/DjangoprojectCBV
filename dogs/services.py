from django.core.mail import send_mail
from django.conf import settings


def send_views_mail(dog_object, owner_email, views_count):
    send_mail(
        subject=f'{views_count} просмотров {dog_object}',
        message=f'Юхху! Уже {views_count}, просмотров у {dog_object}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[owner_email, ]
    )
