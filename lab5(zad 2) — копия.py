n = int(input("Введите число 1 -4: "))
a = 1#Лето
b = 2#Осень
c = 3#Зима
d = 4#Весна
x = 4.1#Левое число
if 1<n and n<3 and 3<4:
    print("Осень")
elif n<b and b<c and c<d:
    print("Лето")
elif n<d and n>b and b>a:
    print("Зима")
elif n>c and c>b and b>a and x>n:
    print("Весна")
elif n>x and x>d and x>c and x>b and x>a:
    print("Число не верное, введите от 1 до 4")
else:
    print("")

