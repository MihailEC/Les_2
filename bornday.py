year = int(input('Введите год рождения А.С. Пушкина: '))
if year == 1799:
    day = int(input('Введите день рождения: '))
    if day == 6:
        print('Верно')
    else:
        print('Неверный день рождения')
else:
    print('Неверный год рождения')