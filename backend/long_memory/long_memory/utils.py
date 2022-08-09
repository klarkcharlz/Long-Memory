from rest_framework.views import exception_handler
# from django.utils.translation import gettext as _


def custom_exception_handler(exc, context):
    """ Ф-я обрабатывает исключения, если какая-либо из 'вьюшек' отработала с ошибкой, то этот handler отлавливает
        это исключение. Обязательно нужно в settings.py добавить:
            REST_FRAMEWORK = {
                ...,
                'EXCEPTION_HANDLER': 'long_memory.utils.custom_exception_handler',
                ...
            }
    """
    response = exception_handler(exc, context)

    if response is not None:
        # поумолчанию на фронт можно отправлять статус-код
        response.data['status_code'] = response.data.status_code
        # но впринципе к response можно добавлять ключи с значениями, как показано ниже
        response.data['error'] = 'Все поля должны быть заполненными'

    return response
