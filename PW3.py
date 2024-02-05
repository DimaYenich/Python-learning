#1
def convert_to_miles():
    kilometrs = input('Введіть кілометри для конвертації в милі:')
    print(f"{kilometrs}км в милях дорівнює {round(int(kilometrs)*0.621371,2)}")

#2    
def exponentiation():
    number = int(input("Введіть число:"))
    power_of_number = int(input("Введіть степінь:"))
    result = 1
    for _ in range(power_of_number):
        result*=number
    print(f"Число піднесене до степення за допомогою циклу: {result}")

#3
def factorial_loop():
    n = int(input("Введіть число для факторіала: "))
    number = 1
    while n>=1:
        number*=n
        n -= 1
    print(number)

#4
def factorial_recurs(n):
    if (n==1 or n==0): 
        return 1 
    else: 
        return n * factorial_recurs(n - 1)
    
#5
def capitalize():
    words = input('Введіть рядок для заміни перших літер на великі: ').split()
    result = ''
    for word in words:
        result += word.capitalize()+' '
    print("Рядок з верхнім регістром кожної першої літери окремого слова: " + result)


#6
def find_max_lenght():
    print("Найдовше слово: ", max(input("Введіть рядок для пошуку найдовшого слова: ").split(), key=len))

#7
def count_words():
    print("Кількість слів в рядку: ", len(input("Введіть рядок для підрахунку кількості слів: ").split()))

#convert_to_miles()
#exponentiation()
#factorial_loop()
#print(factorial_recurs(int(input("Введіть число для факторіала: "))))
#capitalize()
#find_max_lenght()
#count_words()
    