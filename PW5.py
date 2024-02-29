import math

#1
class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0])


    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.matrix])


    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Розміри матриць не збігаються")
        result = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        
        for i in range(self.rows):
            for j in range(self.cols):
                result[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return Matrix(result)


    def __sub__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Розміри матриць не збігаються")
        result = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        
        for i in range(self.rows):
            for j in range(self.cols):
                result[i][j] = self.matrix[i][j] - other.matrix[i][j]
        return Matrix(result)


    def __mul__(self, other):
        if self.cols != other.rows:
            raise ValueError("Неможливо помножити матриці")
        result = [[0 for _ in range(other.cols)] for _ in range(self.rows)]
        
        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    result[i][j] += self.matrix[i][k] * other.matrix[k][j]
        return Matrix(result)

#2
#Точка
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

#Лінія
class Line(Point):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.point1 = x
        self.point2 = y
    
    
    def length(self):
        return math.sqrt((self.point2.x - self.point1.x)**2 + (self.point2.y - self.point1.y)**2)

#Трикутник
class Triangle(Line):
    def __init__(self, line1, line2, line3):
        self.line1 = line1
        self.line2 = line2
        self.line3 = line3
        
    def perimeter(self):
        return self.line1.length() + self.line2.length() + self.line3.length()


#3
#Людина 
class Human():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def change_name(self, new_name):
        self.name = new_name

#Студент
class Student(Human):
    def __init__(self, name, age, university):
        super().__init__(name, age)
        self.university = university
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def calculate_average_grade(self):
        if not self.grades:
            return "Оцінок немає!"
        return sum(self.grades) / len(self.grades)

#4
class Order:
    def __init__(self):
        self._products = []

    def add_product(self, product_name, quantity, price):
        self._products.append({"name": product_name, "quantity": quantity, "price": price})

    def calculate_total_cost(self):
        total_cost = sum(product['quantity'] * product['price'] for product in self._products)
        return total_cost


class Customer:
    def __init__(self, name):
        self.name = name

    def add_product(self, order, product_name, quantity, price):
        order.add_product(product_name, quantity, price)


class OrderProcessor:
    def process_order(self, order):
        total_cost = order.calculate_total_cost()
        print("Загальна вартість замовлення:", total_cost)

#Створення об'єктів
#1
matrix1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix2 = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

print("Матриця 1:")
print(matrix1)

print("\nМатриця 2:")
print(matrix2)

print("\nДодавання:")
print(matrix1 + matrix2)

print("\nВіднімання:")
print(matrix1 - matrix2)

print("\nМноження:")
print(matrix1 * matrix2)


#2
point1 = Point(0, 0)
point2 = Point(3, 4)
point3 = Point(6, 0)
line = Line(point1, point2)
print("Довжина лінії:", line.length())

line1 = Line(point1, point2)
line2 = Line(point2, point3)
line3 = Line(point3, point1)
triangle = Triangle(line1, line2, line3)
print("Периметр трикутника:", triangle.perimeter())

#3
student = Student("Василь", 20, "КНУ")
print("\nІм'я студента:", student.name,
        "\nВік студента:", student.age,
        "\nВНЗ студента:", student.university)

student.change_name("Петро")
print("Нове ім'я студента:", student.name)

student.add_grade(4)
student.add_grade(5)
student.add_grade(3)
print("Список оцінок студента:", student.grades)
print("Середня оцінка студента:", student.calculate_average_grade())


#4
order_processor = OrderProcessor()
customer = Customer("Дмитро")
order = Order()
customer.add_product(order, "Шкарпетки", 2, 20)
customer.add_product(order, "Хліб", 1, 15)
order_processor.process_order(order)


# Приклад використання:
order_processor = OrderProcessor()
customer = Customer("Дмитро")
order = Order()
customer.add_product(order, "Молоко", 2, 20)
customer.add_product(order, "Хліб", 1, 15)
order_processor.process_order(order)
