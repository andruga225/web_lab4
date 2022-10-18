import datetime
import os

prevInputs=[]

def intTryParse(value):
    try:
        return int(value), True
    except ValueError:
        return value, False

def floatTryParse(value):
    try:
        return float(value), True
    except ValueError:
        return value, False


def deleteLogs():
    if os.path.exists("logs/logfile.txt"):
        os.remove("logs/logfile.txt")
        print("Логи очищены")
    else:
        print("Логи не найдены")


def checkForErrors(x):
    if(floatTryParse(x)[1]):
        val=float(x)
        return int(val)
    if x == "q":
        print("Всего хорошего!")
        exit()
    elif x == "rm logs":
        deleteLogs()
        exit()
    else:
        print("Ошибка ввода числа", x, "введите число: ")
        x = input()
    return x

def checkInPrev(x, y):
    for elem in prevInputs:
        if (elem[0]==x and elem[1]==y) or (elem[0]==x and elem[1]==y):
            return True, elem[2]
    return False, 0

def NOD(x, y):
    while x!=0 and y!=0:
        if x>y:
            x=x%y
        else:
            y=y%x

    return x+y

def logs(x,y,res):
    if not os.path.exists("logs"):
        os.mkdir("logs")
    if not os.path.exists("logs/logfile.txt"):
        with open("logs/logfile.txt", "w") as f:
            f.write(str(x) + " ")
            f.write(str(y) + " ")
            f.write(str(res) + " ")
            f.write(str(datetime.datetime.now()) + "\n")
    else:
        with open("logs/logfile.txt", "a") as f:
            f.write(str(x) + " ")
            f.write(str(y) + " ")
            f.write(str(res) + " ")
            f.write(str(datetime.datetime.now()) + "\n")

def main():
    print("Поиск НОД двух чисел\nВведите первое число ")
    x=input()
    print("Введите второе число ")
    y=input()

    while(not intTryParse(x)[1] or not intTryParse(y)[1]):
        x = checkForErrors(x)
        y = checkForErrors(y)

    x=intTryParse(x)[0]
    y=intTryParse(y)[0]

    if x==0 or y==0:
        print("Одно из чисел 0")
        logs(x, y, "Одно из чисел 0")
        exit()

    check=checkInPrev(x,y)
    if check[0]:
        print(check[1], "Результат возвращен из кеша")
        logs(x, y, str(check[1]) + "Результат возвращен из кеша")
        main()
    else:
        res=NOD(x,y)
        prevInputs.append((x,y,res))
        logs(x,y,res)
        print(res)
        main()

if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
