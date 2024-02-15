#1
class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
    

    def is_correct(self):
        return self.numerator < self.denominator

#2
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    #додавання
    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)

    #віднімання
    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
    
    #виведення
    def __str__(self):
        return "({}, {})".format(self.x, self.y)

#3 - animal
class Animal:
    def __init__(self, species, name):
        self.species = species
        self.name = name

    def __str__(self):
        return "{}: {}".format(self.species, self.name)

#3 - zoo
class Zoo:
    def __init__(self):
        self.animals = []


    def add_animal(self, animal):
        if isinstance(animal, Animal):
            self.animals.append(animal)
        else:
            raise TypeError("Тільки об'кти класу 'Animals' можуть бути додані до класу 'Zoo'")


    def remove_animal(self, animal):
        if animal in self.animals:
            self.animals.remove(animal)
        else:
            print("{} не в зоопарку.".format(animal))


    def __str__(self):
        zoo_info = "Тварини в зоопарку:\n"
        for animal in self.animals:
            zoo_info += "{}\n".format(animal)
        return zoo_info

#4    
class FibonacciContainer:
    def __init__(self, n):
        self.fibonacci_list = self.generate_fibonacci(n)

    def generate_fibonacci(self, n):
        fibonacci_list = [0, 1]
        for _ in range(2, n):
            next_fibonacci = fibonacci_list[-1] + fibonacci_list[-2]
            fibonacci_list.append(next_fibonacci)
        return fibonacci_list

    def __len__(self):
        return len(self.fibonacci_list)

    def __getitem__(self, index):
        return self.fibonacci_list[index]

    
if __name__ == "__main__":
    #1
    fraction1 = Fraction(2, 3)
    fraction2 = Fraction(5, 2)
    print("Дріб 1 є правильним:", fraction1.is_correct())
    print("Дріб 2 є правильним:", fraction2.is_correct())

    #2
    v1 = Vector(3, 4)
    v2 = Vector(1, 2)
    print("Сума векторів v1 та v2:", v1 + v2)
    print("Різниця векторів v1 та v2:", v1 - v2)

    #3
    lion = Animal("Лев", "Сімба")
    elephant = Animal("Мавпа", "Віталій")
    tiger = Animal("Риба", "Немо")
    zoo = Zoo()
    zoo.add_animal(lion)
    zoo.add_animal(elephant)
    zoo.add_animal(tiger)
    print(zoo)
    zoo.remove_animal(elephant)
    print(zoo)

    #4
    fib_container = FibonacciContainer(10)
    print("Кількість чисел в контейнері:", len(fib_container))
    print("Перші 5 чисел:", fib_container[:5])