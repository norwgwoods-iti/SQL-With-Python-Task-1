

from function.authorization import Authorization
from function.reset_password import ResetPassword
from function.registration import Registration

print('Введите число:')
running = True
while running:
    try:
        select_function = int(input('1 - Регистрация\n2 - Авторизация\n3 - Сброс пароля\n0 - Выход из программы\n'))

        if select_function == 1:
            reg = Registration()
            reg.registration()

        elif select_function == 2:
            aut = Authorization()
            aut.authorization()

        elif select_function == 3:
            rp = ResetPassword()
            rp.reset_password()

        elif select_function == 0:
            print('Программа завершена')
            running = False

        else:
            print('Число, которое необходимо ввести содержит значения от 1 до 3')

    except ValueError:
        print('Необходимо ввести числовое значение от 1 - 3')


