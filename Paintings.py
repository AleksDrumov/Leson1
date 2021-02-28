print('Вы можете посчитать сколько картин вы нарисуете за определённое количество лет')
target = int(input('Сколько лет вы собираетесь рисовать картины?'))
paintings_per_year = int(input('Сколько картин в год?'))
all_paintings = target * paintings_per_year
if paintings_per_year < 1:
    print('Ты дурачок?')
else:
    print(all_paintings,"картин за",target,"лет вы нарисуете(Может вы передумаете?)")



