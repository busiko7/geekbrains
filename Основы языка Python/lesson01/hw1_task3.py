# 3. Создайте программу “Медицинская анкета”, где вы запросите у пользователя следующие данные: имя, фамилия,
# возраст и вес.
# Выведите результат согласно которому:
# Пациент в хорошем состоянии, если ему до 30 лет и вес от 50 и до 120 кг,
# Пациенту требуется заняться собой, если ему более 30 и вес меньше 50 или больше 120 кг
# Пациенту требуется врачебный осмотр, если ему более 40 и вес менее 50 или больше 120 кг.
# Все остальные варианты вы можете обработать на ваш вкус и полет фантазии.
#
# (Формула не соответствует реальной действительности и здесь используется только ради примера)
# Примечание: при написание программы обратите внимание на условия в задаче и в вашем коде.  Протестируйте программу
# несколько раз и убедитесь, что проверки срабатывают верно. В случае ошибок, уточните условия для той или иной
# ситуации.
#
# Пример: Вася Пупкин, 29 год, вес 90 - хорошее состояние
# Пример: Вася Пупкин, 31 год, вес 121 - следует заняться собой
# Пример: Вася Пупкин, 31 год, вес 49 - следует заняться собой
# Пример: Вася Пупкин, 41 год, вес 121 - следует обратится к врачу!
# Пример: Вася Пупкин, 41 год, вес 49 - следует обратится к врачу!

print('Добро пожаловать в программу "Калькулятор индекса массы тела"')
print('***********************************************************************************************************'
      '*************')

first_name = input('Введите Ваше имя: ')
last_name = input('Введите Вашу фамилию: ')
height = int(input('Введите Ваш рост: '))
weight = int(input('Введите Ваш вес: '))
age = int(input('Введите Ваш возраст: '))

health_result = ''

index_ketle = weight / ((height / 100)**2)

print('Индекс массы тела(формула Кетле): ', round(index_ketle, 1))

if 18 <= age <= 30 and index_ketle < 15.9 or age >= 30 and index_ketle < 17:
    health_result += 'У Вас выраженный дефицит массы тела. Необходима срочная консультация специалиста.'
elif 18 <= age <= 30 and 16 <= index_ketle <= 19.4 or age >= 30 and 17.1 <= index_ketle <= 19.9:
    health_result += 'У Вас дефицит массы тела. Вам рекомендуется немного поправиться... Если не получается – ' \
                     'обратитесь к специалисту.'
elif 18 <= age <= 30 and 19.5 <= index_ketle <= 22.9 or age >= 30 and 20 <= index_ketle <= 25.9:
    health_result += 'У Вас нормальный вес. Так держать!'
elif 18 <= age <= 30 and 23 <= index_ketle <= 27.4 or age >= 30 and 26 <= index_ketle <= 27.9:
    health_result += 'У Вас избыточный вес. Рекомендуется некоторое снижение массы тела. Повышен риск неинфекционных ' \
                     'и системных заболеваний.'
elif 18 <= age <= 30 and 27.5 <= index_ketle <= 29.9 or age >= 30 and 28 <= index_ketle <= 30.9:
    health_result += 'У Вас ожирение I степени. Рекомендуется снижение массы тела. Повышен риск неинфекционных и ' \
                     'системных заболеваний. Необходима консультация специалиста.'
elif 18 <= age <= 30 and 30 <= index_ketle <= 34.9 or age >= 30 and 31 <= index_ketle <= 35.9:
    health_result += 'У Вас ожирение II степени. Настоятельно рекомендуется снижение массы тела. Высокий риск для ' \
                     'Здоровья!\nВысока вероятность заболеть неинфекционными или системными заболеваниями. Необходима ' \
                     'консультация специалиста.'
elif 18 <= age <= 30 and 35 <= index_ketle <= 39.9 or age >= 30 and 36 <= index_ketle <= 40.9:
    health_result += 'У Вас ожирение III степени. Настоятельно рекомендуется снижение массы тела. Очень высокий риск ' \
                     'для Здоровья! Необходима срочная консультация специалиста.'
elif 18 <= age <= 30 and 40 <= index_ketle or age >= 30 and 41 <= index_ketle:
    health_result += 'У Вас ожирение IV степени. Необходимо немедленное снижение массы тела. Чрезвычайно высокий ' \
                     'риск для Здоровья!\nВозможно, Вы уже болеете каким-либо хроническим заболеванием и при такой ' \
                     'массе тела выздоровление будет осложнено. Необходима срочная консультация специалиста.'
else:
    health_result += 'Вы ввели неккоректные значения. Попробуйте ещё раз!'

answer = first_name + ' ' + last_name + '. ' + health_result + '\n'

print(answer)
print('***********************************************************************************************************'
      '*************')
print(f'Индекс массы тела является показателем отношения веса и роста человека. Данный параметр помогает определить'
      f' отклонения от нормальной \nмассы тела в ту или иную сторону. Лишний вес опасен для человеческого здоровья, '
      f'поскольку часто приводят к сердечным заболеваниям. \nP.S. ИМТ нельзя применять непосредственно к Спортсменам, '
      f'так как Мышечная Масса обычно выходит за пределы Массы обычного человека.')
