suma = 0 
firstNumber = 0.5
count = 0
while suma < 1:
    suma = suma + firstNumber
    firstNumber = firstNumber / 2
    count = count + 1
    print(suma)
print(count)

#Вторая часть
suma = 0 
firstNumber = 100
count = 0
RAM = int(input('Сока у тя опративки в мегабайтах'))
while suma < RAM:
    suma = suma + firstNumber
    count = count + 1
if count > 199:
    print('Чего-чего?!')
elif RAM < 0:
    print('Ti durachok')
else:
    print('Ну ок...')
