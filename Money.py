def code():
    views = int(input('Сколько просмотров'))
    money = subscribers * 0.1 * views
    if money > 99:
        print(money / 100, 'ГРИВН')
    else:
        print(money, 'Копеек')

print('\'Калькулятор денег за видео\'')
subscribers = int(input('Сколько подписчиков'))
if subscribers > 9:
    code()
else:
    print("Надо хотя бы 10(а в реальности хотя 1000(но это всё-равно))")

