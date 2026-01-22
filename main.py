def hisoblash(number1, number2, amal):
    if amal == 1:
        return qoshish(number1, number2)
    elif amal == 2:
        return ayirish(number1, number2)
    elif amal == 3:
        return kopaytirish(number1, number2)
    elif amal == 4:
        if number2 == 0:
            return "0 ga bolib bolmaydi"
        return bolish(number1, number2)
    else:
        return "Notogri amal"


def qoshish(a, b):
    return a + b

def ayirish(a, b):
    return a - b

def kopaytirish(a, b):
    return a * b

def bolish(a, b):
    return a // b


print("1-qoshish  2-ayirish  3-kopaytirish  4-bolish")
number1 = int(input('1-son: '))
number2 = int(input('2-son: '))
amal = int(input('amalni kiriting: '))

print(hisoblash(number1=number1, number2=number2, amal=amal))
