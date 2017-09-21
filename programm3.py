number_default = 0
users_number = int(input("Введите число: "))
  #проверяем число на правильность
def isPrime(number):
  if number > 1:
    for i in range(2, number):
    	#если число делится без остатка - оно составное
      if(number % i) == 0:
        return False
    #иначе простое
    else:
      return True
  else:
    return False

#создаем диапазон чисел от 0 до числа пользователям 
for i in range(1, users_number):
  all_prime = isPrime(i)
  if all_prime == True:
    print(i, "- это простое число")