import math

#1
def years_to_days():
    years = int(input('Введіть ваший вік:'))
    print(f"Ви прожили {years*365} днів." )

#2
def force_to_body():
    mass_of_object = float(input('Введіть масу тіла:'))
    acceleration = float(input('Введіть прикорення:'))
    print(f"Значення сили, яку приклали до тіла дорівюнє {mass_of_object*acceleration}")

#3
def quadratic_equation():
    print("Введіть коефіцієнти для рівняння ax^2 + bx + c = 0: ")   
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))
    D = b ** 2 - 4 * a * c                                 
    if D > 0:                                              
        x1 = (-b + math.sqrt(D)) / (2 * a)                 
        x2 = (-b - math.sqrt(D)) / (2 * a)
        print('x1 = %s \nx2 = %s' % (x1, x2))              
    elif D == 0:                                           
        x = -b / (2 * a)                                   
        print('x = %s' % x)                                
    else:
        print("Корені відсутні")

#4
class TriangleAreaCalculator:
    def choise():
        number = int(input("\n1 - Формула герона"
                            "\n2 - За висотою та основою"
                            "\n3 - За Двома сторонами та кутом між ними"
                            "\nОберіть варіант розрахунку:"))
        match number:
            case 1:
                TriangleAreaCalculator.calculate_area_by_heron()
            case 2:
                TriangleAreaCalculator.calculate_area_by_height()
            case 3:
                TriangleAreaCalculator.calculate_area_by_sides_and_angle()
            case _:
                print("Невірний вибір!")


    def calculate_area_by_heron():
        side_a, side_b, side_c = map(float, input("Введіть три сторони трикутника через пробіл: ").split())
        s = (side_a + side_b + side_c) / 2
        print(s)
        area = math.sqrt(s * (s - side_a) * (s - side_b) * (s - side_c))
        print(f"Площа трикутника {area}")


    def calculate_area_by_height():
        base = float(input("Введіть довжину основи:"))
        height = float(input("Введітиь висоту:"))
        area = 0.5 * base * height
        print(f"Площа трикутника {area}")


    def calculate_area_by_sides_and_angle(side1, side2, angle): 
        side1 = float(input("Введіть довжину першої сторони: "))
        side2 = float(input("Введіть довжину другої сторони: "))
        angle = float(input("Введіть величину кута між сторонами (в градусах): "))
        area = 0.5 * side1 * side2 * math.sin(math.radians(angle))
        print(f"Площа трикутника {area}")

#5
def print_max_and_min():
    array = input("Введіть три числа через пробіл: ").split()
    print(f"Найбільше число: {max(array)}"
          f"Найменше число: {min(array)}")

#6
def sum_of_natural_numbers():
    N = int(input("Введіть натуральне число N (1 ≤ N ≤ 100): "))
    if 1 <= N <= 100:
        total_sum = sum(range(1, N + 1))
        print(f"Сума перших {N} натуральних чисел: {total_sum}")
    else:
        print("Введіть коректне число N (1 ≤ N ≤ 100).")

#7
def print_prime_numbers_in_range():
    start_range = int(input("Введіть початок діапазону: "))
    end_range = int(input("Введіть кінець діапазону: "))

    print(f"Прості числа в діапазоні від {start_range} до {end_range}:")
    for number in range(start_range, end_range + 1):
        if number > 1:
            is_prime = True
            for i in range(2, int(number**0.5) + 1):
                if number % i == 0:
                    is_prime = False
                    break
            if is_prime:
                print(number, end=" ")

#8
def find_previous_prime_and_print():
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    number = int(input("Введіть ціле число: "))
    
    if number <= 1:
        print("Немає простого числа, яке передує введеному")
    else:
        previous_prime = number - 1
        while not is_prime(previous_prime):
            previous_prime -= 1
        print(f"Перше просте число, яке передує {number}: {previous_prime}")


#years_to_days()
#force_to_body()
#quadratic_equation()
#TriangleAreaCalculator.choise()
#print_max_and_min()
#sum_of_natural_numbers()
#print_prime_numbers_in_range()
#find_previous_prime_and_print()