#1
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def engine_start(self):
        print("Engine started")


class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def engine_start(self):
        print("Car engine started")


class Motorcycle(Vehicle):
    def __init__(self, brand, type):
        super().__init__(brand)
        self.type = type

    def engine_start(self):
        print("Motorcycle engine started")


class ElectricCar(Car):
    def __init__(self, brand, model):
        super().__init__(brand, model)
    
    def charge_battery(self):
        print("Battery charging")


class Garage:
    def __init__(self):
        self.vehicles = []

    def start_all_engines(self):
        for vehicle in self.vehicles:
            vehicle.engine_start()


#2
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def introduce(self):
        print(f"Name: {self.name}, age: {self.age}")


class Employee(Person):
    def __init__(self, name, age, position):
        super().__init__(name, age)
        self.position = position

    def work(self):
        print(self.position)


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id


    def study(self):
        print('Студент')


class University:
    def __init__(self):
        self.employees = []
        self.students = []


    def add_employee(self, employee):
        if isinstance(employee, Employee):
            self.employees.append(employee)
        else:
            raise TypeError("Тільки об'кти класу 'Employee' можуть бути додані до класу 'University'")


    def add_student(self, student):
        if isinstance(student, Student):
            self.students.append(student)
        else:
            raise TypeError("Тільки об'кти класу 'Student' можуть бути додані до класу 'University'")

    
    def show_info(self):
            print("Employees:")
            for employee in self.employees:
                employee.introduce()
                employee.work()
            print("\nStudents:")
            for student in self.students:
                student.introduce()
                student.study()

    def remove_employee(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)
        else:
            print("Такий робітник відсутній в списку.")
    
    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)
        else:
            print("Такий студент відсутній в списку.")
    

    def search_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                print(f"\nСтудент з id {student_id}")
                student.introduce()
                student.study()
                break

    
    def search_employee(self, name):
        for employee in self.employees:
            print(f"\nРобітники з ім'ям {name}")
            if employee.name == name:
                employee.introduce()
                employee.work()
                


#1
garage = Garage()
lada = Car('Lada', 'VAZ21099')
viper = Motorcycle('Vioer', 'R1')
tesla = ElectricCar('Tesla','Cybertruck')
garage.vehicles.append(lada)
garage.vehicles.append(viper)
garage.vehicles.append(tesla)
garage.start_all_engines()

#2
university = University()
Boyko = Employee('Михайло', 29, "Викладач")
Boychuk = Employee('Михайло', 22, "Викладач")
Yenich = Student('Дмитро', 20, 1)
university.add_employee(Boyko)
university.add_employee(Boychuk)
university.add_student(Yenich)
university.show_info()
university.search_employee('Михайло')
university.search_student(1)
university.remove_student(Yenich)
university.remove_employee(Boyko)
university.show_info()