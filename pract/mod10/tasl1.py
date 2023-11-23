import re

def check_password(password):
    """
    Проверяет, является ли переданный пароль корректным.

    >>> check_password('rtG3FG!Tr^e')
    True
    >>> check_password('aA1!*!1Aa')
    True
    >>> check_password('oF^a1D@y5e6')
    True
    >>> check_password('enroi#$rkdeR#$092uWedchf34tguv394h')
    True
    >>> check_password('пароль')
    False
    >>> check_password('password')
    False
    >>> check_password('qwerty')
    False
    >>> check_password('lOngPa$$$W0Rd')
    False
    """

    # Проверяем, что пароль содержит только латинские символы, цифры и специальные символы
    if not re.match(r'^[a-zA-Z0-9^$%@#&*!?]+$', password):
        return False

    # Проверяем, что пароль состоит из не менее чем шести символов
    if len(password) < 6:
        return False

    # Проверяем, что пароль содержит по крайней мере два латинских символа в верхнем регистре
    if not re.search(r'[A-Z].*[A-Z]', password):
        return False

    # Проверяем, что пароль содержит по крайней мере одну цифру
    if not re.search(r'\d', password):
        return False

    # Проверяем, что пароль содержит по крайней мере два различных специальных символа
    if not re.search(r'([^\w\s]|_){1,}', password):
        return False

    # Проверяем, что пароль не содержит трех одинаковых символов подряд
    if re.search(r'(.)\1\1', password):
        return False

    return True


