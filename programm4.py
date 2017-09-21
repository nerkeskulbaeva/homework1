a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

list=[]

for i in range(a, b+1):
    if i % 5 == 0:
        list.append(i)
		
print(list)