# Задание №6
# В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число,
# чем то, что загадано. Если за 10 попыток число не отгадано, то вывести загаданное число.
import random

print('Угадаете число от 0 до 100, у Вас всего 10 попыток')

rounds = 10
number = random.randint(0, 100)

while rounds > 0:
    answer = int(input('Введите Ваш вариант ответа: '))
    rounds -= 1

    if 100 >= answer >= 0:

        if answer == number:
            print(f'Поздравляем, Вы угадали число! Количество оставшихся попыток: {rounds}.')
            break
        elif answer > number:
            print(f'Вы не угадали, Ваше число больше. Осталось {rounds} попыток.')
        else:
            print(f'Вы не угадали, Ваше число меньше. Осталось {rounds} попыток.')

    else:
        print(f'Вы ввели число не из диапазона возможных. Осталось попыток: {rounds}')

else:
    print(f'Вы проиграли! Случайное число: {number}')
