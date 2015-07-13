from django.conf import settings


def connect():
    if settings.DEBUG:
        return False

    return True
