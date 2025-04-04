##############################
# Домашняя работа №28
# 04.04.2025
# Aндрей Дьякончук
##############################

# Task 1 ---------------------
print("# 1. Task ------")

class Circle:
    def __init__(self, name, rad, color):
        self.name = name
        self.rad = rad
        self.color = color

    def circle_square(self):
        return 3.14*(self.rad**2)

    def circle_circumf(self):
        return 2*3.14*self.rad
    
    def circle_square_result(self):
        print(f"Square of a {self.name}  = {self.circle_square()}")

    def circle_circum_result(self):
        print(f"Circumference of a {self.name}  = {self.circle_circumf()}")
        

# Создаем 3 объекта класса Circle
circle1 = Circle("circle1",4, "red")
circle2 = Circle("circle2",3, "blue")
circle3 = Circle("circle3",5, "green")

# Выводим результат площади круга трех объектов
circle1.circle_square_result()
circle2.circle_square_result()
circle3.circle_square_result()

# Выводим результат длины окружности трех объектов
print("\n")
circle1.circle_circum_result()
circle2.circle_circum_result()
circle3.circle_circum_result()

# Task 2 ---------------------
print("\n# 2. Task ------")

class BankAccount:
    def __init__(self, acc_number, name, balance):
        self.acc_number = acc_number
        self.name = name
        self.balance = balance

    def account_info(self):
        print(f"Account number \"{self.acc_number}\" belongs to {self.name} and has balance = {self.balance}")

    def Refill_account(self, refill):
        self.balance = self.balance  + refill
        print(f"Account refilled with {refill} money and  new balanсe of {self.name} account = {self.balance}") 
    
    def Withdraw_account(self, withdraw):
        if self.balance - withdraw >= 0:
            self.balance = self.balance - withdraw
            print(f"{withdraw} money was withdrawn from the {self.name}'s account and new balance = {self.balance}")
        elif self.balance - withdraw < 0:
             print(f"You try to withdraw {withdraw} money from {self.name}'s account, what is more than on the balance right now = {self.balance} ")
        else:
            self.balance = 0
            print(f"{withdraw} money was withdrawn from the {self.name}'s account and new balance = {self.balance}")
    
# Создаем 3 объекта класса BankAccount
account1 = BankAccount(4523, "Tom", 6780)
account2 = BankAccount(8907, "Bob", 12567)
account3 = BankAccount(3211, "Anna", 56987)

# Выводим информации о созданных объектах
account1.account_info()
account2.account_info()
account3.account_info()
print("\n")

# Пополняем счет в трех объектах и выводим новый баланс
account1.Refill_account(100)
account2.Refill_account(2000)
account3.Refill_account(3000)
print("\n")

# Снимаем деньги с аккаунта и выводим новый баланс
account1.Withdraw_account(45)
account2.Withdraw_account(14567)
account3.Withdraw_account(59988)

# Task 3 ---------------------
print("\n# 3. Task ------")

class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age  = age
        self.av_grade = None

    def student_info(self):
        print(f"Student {self.__name} has age  {self.__age} and average grade {self.av_grade}")

    def set_av_grade(self, av_grade):
        self.av_grade = av_grade
        
    def student_status(self):
        if self.av_grade >= 8.5 and self.av_grade <= 10:
            print(f"Studen {self.__name} has status \"Excellent\"")
        elif  self.av_grade >= 7 and self.av_grade < 8.5:
            print(f"Studen {self.__name} has status \"Good\"")
        else: 
            print(f"Studen {self.__name} has status \"Satisfactory\"")

# Создаем  3 объекты класса Student
student1 = Student("Alex", 18)
student2 = Student("Olga", 19)
student3 = Student("Ivan", 18.5)

# Установим средний бал каждого студента
student1.set_av_grade(8.6)
student2.set_av_grade(7.5)
student3.set_av_grade(6.8)

# Выводим информацию о всех объектах
student1.student_info()
student2.student_info()
student3.student_info()

# Выводим статус каждого студента
student1.student_status()
student2.student_status()
student3.student_status()

# Task 4 ---------------------
print("\n# 4. Task ------")

class Book:
    def __init__(self, book_name, book_author, publish_date):
        self.book_name = book_name
        self.book_author = book_author
        self.publish_date = publish_date

    def get_book_info(self):
        print(f"\"{self.book_name}\" written by the \"{self.book_author}\" was published  in {self.publish_date}")

    def set_book_attributes(self, name, author, date):
        self.book_name = name
        self.book_author = author
        self.publish_date = date

# Создаем дочерний класс
class Ebook(Book):
    def __init__(self, book_name, book_author, publish_date, book_price):
        super().__init__(book_name, book_author, publish_date)
        self.book_price = book_price

    def get_Ebook_info(self):
        print(f"\"{self.book_name}\" written by the \"{self.book_author}\" was published  in {self.publish_date} and current price is {self.book_price}")

    def set_Ebook_attributes(self, name, author, date, price):
        self.book_name    = name
        self.book_author  = author
        self.publish_date = date
        self.book_price   = price

# Создаем объект класса Book
book1 = Book("Анна Каренина", "Л.Н.Толстой", 1875)

# Создаем объекты класса Ebook
book2 = Ebook("The DevOps Handbook", "Gene Kim", 2021, 18.5)
book3 = Ebook("Technical Analysis", "J.Murphy", 1999, 22)

# Выводим данные созданных объектов
book1.get_book_info()
book2.get_Ebook_info()
book3.get_Ebook_info()
print("\n")

# Изменяем аттрибуды объктов через их методы
book1.set_book_attributes("Война и Мир", "Л.Н.Толстой", 1867)
book2.set_Ebook_attributes("Modern Physics", "Stephen Thornton", 2020, 76)
book3.set_Ebook_attributes("Basic Economics", "Thomas Sowell", 2014, 16)

# Выводим объекты с измененными аттрибутами
book1.get_book_info()
book2.get_Ebook_info()
book3.get_Ebook_info()



# Task 5 ---------------------
print("\n# 5. Task ------")

class Vehicle:
    def __init__(self, color, engine, model, release_year):
        self.color = color
        self.engine = engine
        self.model = model
        self.year = release_year

    def set_attributes(self, color, engine, model, release_year):
        self.color = color
        self.engine = engine
        self.model = model
        self.year = release_year

    def get_Car_info(self):
        print(f"Vehicle {self.model} has {self.color} color, engine is {self.engine} HP and release date {self.year}")
       
class Truck(Vehicle):
    def __init__(self, color, engine, model, release_year, type, price):
        super().__init__(color, engine, model, release_year)
        self.type = type
        self.price = price
    
    def set_attributes(self, type, price):
        self.type = type
        self.price = price

    def get_Truck_info(self):
        print(f"{self.model} is vehicle of  {self.type} type, has {self.color} color, engine is {self.engine} HP, release date {self.year} and price {self.price}")

class Bus(Vehicle):
    def __init__(self, color, engine, model , release_year, wheels, price):
        super().__init__(color, engine, model , release_year)
        self.wheels = wheels
        self.price = price

    def set_attributes(self, wheels, price):
        self.wheels = wheels
        self.price = price

    def get_Bus_info(self):
        print(f"Bus model is {self.model}, has {self.color} color, engine is {self.engine} HP, number of wheels {self.wheels}, release date {self.year} and price {self.price}")

# Создаем объект класса Vehicle
car1 = Vehicle("red", 250, "VW", 2016)

# Создаем объект класса Tuck
car2 = Truck("white", 900, "Volvo", 2024, "Truck", 5678)

# Создаем объект класса Bus
car3 = Bus("green", 1200 , "Maz", 2023, 8, 45600)

# Выводим данные о наших объектах
car1.get_Car_info()
car2.get_Truck_info()
car3.get_Bus_info()
print("\n")
# Изменим некоторые аттрибуты всех объектов
car1.set_attributes("black", 300, "BMW", 2013)
car2.set_attributes("Heavy Truck", 8900)
car3.set_attributes("10", 12200)

# Выводим данные о наших объектах
car1.get_Car_info()
car2.get_Truck_info()
car3.get_Bus_info()
