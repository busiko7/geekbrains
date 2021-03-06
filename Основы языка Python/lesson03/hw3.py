# Тема 3. Практикум «Угадай число».
#
# 1. В этой игре человек загадывает число, а компьютер пытается его угадать.
#
# В начале игры человек загадывает число от 1 до 100 в уме или записывает его на листок бумаги. Компьютер начинает
# его отгадывать предлагая игроку варианты чисел. Если компьютер угадал число, игрок выбирает “победа”. Если компьютер
# назвал число меньше загаданного, игрок должен выбрать “загаданное число больше”. Если компьютер назвал число больше,
# игрок должен выбрать “загаданное число меньше”. Игра продолжается до тех пор пока компьютер не отгадает число.
import random

print('Игра - "Угадай число"')
print('Загадайте число от 1 до 100')

# Вариант 1
count = 0
START = 1
END = 100
answer = ''
number = random.randint(START, END)

while answer != '=':
    print(f'Вы загадали число - {number}?')
    print(f'Введите знак "=" - если компьютер угадал Ваше число, ">" - если число больше, "<" - если число меньше')
    answer = input('Введите Ваш знак: ')
    count += 1
    if answer == '=':
        print(f'Компьютер угадал число - {number} с {count}-й попытки!')
        exit()
    elif START == END:
        print(f'Единственное возможное число: {number}')
        print(f'Компьютер угадал число с {count}-й попытки!')
        exit()
    elif answer == '>':
        START = number + 1
        number = random.randint(START, END)
    elif answer == '<':
        END = number - 1
        number = random.randint(START, END)
    else:
        print('Введите корректное значение - ">", "<" или "="')
else:
    print(f'Вы вышли из заданного диапазона чисел')
    exit()

# Вариант 2
# count = 0
# START = 0
# END = 101
#
# number = int((END - START) / 2)
# answer = None
# while answer != '=':
#     count += 1
#     print(f'Вы загадали число - {number}?')
#     print(f'Введите знак "=" - если компьютер угадал Ваше число, ">" - если число больше, "<" - если число меньше')
#     answer = input('Введите Ваш знак: ')
#     if answer == '<':
#         END = number
#         number -= int((END - START) / 2)
#     elif answer == '>':
#         START = number
#         number += int((END - START) / 2)
#     elif answer == '=':
#         continue
#     else:
#         print('Введите корректное значение - ">", "<" или "="')
# else:
#     print(f'Компьютер угадал число с {count}-й попытки!')
