suma = 0 
firstNumber = 0.5
count = 0
while suma < 1:
    suma = suma + firstNumber
    firstNumber = firstNumber / 2
    count = count + 1
    print(suma)
print(count)