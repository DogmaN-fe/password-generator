import string
import random
from colorama import Fore, Style


def generate_password(length: int) -> str:
    """
    Функция генерации пароля
    :param length: Длина пароля
    :return: Сгенерированый пароль
    """

    password = ""

    for _ in range(length):
        # Переменная для выбора числа или буквы
        letter_or_number = random.randint(1, 10)
        # Если letter_or_number меньше 7, то выбираем букву для пороля, иначе цифру
        if letter_or_number < 7:
            password += random.choice(string.ascii_letters)
        elif letter_or_number >= 7:
            password += random.choice(string.digits)

    # Возвращаем строку с паролем
    return password


if __name__ == '__main__':
    # Зацикливаем программу для того, чтобы пользователь ввел именно число
    while True:
        print("Генератор пароля v1.0")
        length_of_password = input("Введите длину пароля: ")

        if length_of_password.isdigit():
            length_of_password = int(length_of_password)
            break
        print(Fore.RED + "!!!Ошибка, введено не число!!!" + Style.RESET_ALL)

    print(f"Ваш пароль: {generate_password(length_of_password)}")
