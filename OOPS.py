##oops concept
"""

"""
"""
=============================================================
  OBJECT-ORIENTED PROGRAMMING (OOP) IN PYTHON
  Basic to Advanced Concepts with Examples
=============================================================
"""

# =============================================================
# 1. CLASS AND OBJECT (Basic)
# =============================================================
# A class is a blueprint; an object is an instance of that class.

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.year} {self.brand} {self.model}"


# Creating objects
car1 = Car("Toyota", "Camry", 2022)
car2 = Car("Honda", "Civic", 2023)

print(car1.display_info())  # 2022 Toyota Camry
print(car2.display_info())  # 2023 Honda Civic


# =============================================================
# 2. INSTANCE vs CLASS vs STATIC VARIABLES
# =============================================================

class Employee:
    # Class variable - shared across all instances
    company = "TechCorp"
    employee_count = 0

    def __init__(self, name, salary):
        # Instance variables - unique to each object
        self.name = name
        self.salary = salary
        Employee.employee_count += 1

    @staticmethod
    def is_valid_salary(salary):
        """Static method - no access to instance or class"""
        return salary > 0

    @classmethod
    def get_employee_count(cls):
        """Class method - has access to class, not instance"""
        return f"Total employees: {cls.employee_count}"


emp1 = Employee("Alice", 75000)
emp2 = Employee("Bob", 85000)

print(Employee.company)              # TechCorp
print(Employee.get_employee_count()) # Total employees: 2
print(Employee.is_valid_salary(50000))  # True


# =============================================================
# 3. ENCAPSULATION (Access Modifiers)
# =============================================================
# Python uses naming conventions:
#   public    -> self.name
#   protected -> self._name  (convention, not enforced)
#   private   -> self.__name (name mangling)

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner          # public
        self._account_type = "Savings"  # protected
        self.__balance = balance    # private

    @property
    def balance(self):
        """Getter - controlled access to private attribute"""
        return self.__balance

    @balance.setter
    def balance(self, amount):
        """Setter - validation before setting value"""
        if amount < 0:
            raise ValueError("Balance cannot be negative")
        self.__balance = amount

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposited ${amount}. New balance: ${self.__balance}"
        return "Invalid amount"

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.__balance}"
        return "Insufficient funds or invalid amount"


account = BankAccount("John", 1000)
print(account.deposit(500))    # Deposited $500. New balance: $1500
print(account.withdraw(200))   # Withdrew $200. New balance: $1300
print(account.balance)         # 1300 (using property getter)

# account.__balance  # AttributeError! (private)
# account._BankAccount__balance  # Name mangling workaround (not recommended)


# =============================================================
# 4. INHERITANCE (Single, Multiple, Multilevel)
# =============================================================

# --- Single Inheritance ---
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        return f"{self.name} makes a sound"


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Dog")
        self.breed = breed

    def speak(self):  # Method overriding
        return f"{self.name} barks!"


class Cat(Animal):
    def speak(self):
        return f"{self.name} meows!"


dog = Dog("Rex", "German Shepherd")
cat = Cat("Whiskers", "Cat")
print(dog.speak())  # Rex barks!
print(cat.speak())  # Whiskers meows!


# --- Multiple Inheritance ---
class Flyable:
    def fly(self):
        return f"{self.name} is flying"


class Swimmable:
    def swim(self):
        return f"{self.name} is swimming"


class Duck(Animal, Flyable, Swimmable):
    def speak(self):
        return f"{self.name} quacks!"


duck = Duck("Donald", "Duck")
print(duck.speak())  # Donald quacks!
print(duck.fly())    # Donald is flying
print(duck.swim())   # Donald is swimming


# --- Multilevel Inheritance ---
class Puppy(Dog):
    def __init__(self, name, breed, toy):
        super().__init__(name, breed)
        self.toy = toy

    def play(self):
        return f"{self.name} plays with {self.toy}"


puppy = Puppy("Buddy", "Labrador", "ball")
print(puppy.speak())  # Buddy barks! (inherited from Dog)
print(puppy.play())   # Buddy plays with ball


# --- MRO (Method Resolution Order) ---
print(Duck.__mro__)  # Shows the order Python looks for methods


# =============================================================
# 5. POLYMORPHISM
# =============================================================

# --- Duck Typing (Implicit Polymorphism) ---
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


# Polymorphism in action - same interface, different behavior
shapes = [Circle(5), Rectangle(4, 6), Triangle(3, 8)]
for shape in shapes:
    print(f"{shape.__class__.__name__}: Area = {shape.area():.2f}")


# --- Operator Overloading ---
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"


v1 = Vector(2, 3)
v2 = Vector(4, 1)
print(v1 + v2)   # Vector(6, 4)
print(v1 - v2)   # Vector(-2, 2)
print(v1 * 3)    # Vector(6, 9)


# =============================================================
# 6. ABSTRACTION (Abstract Base Classes)
# =============================================================

from abc import ABC, abstractmethod


class Shape(ABC):
    """Abstract class - cannot be instantiated directly"""

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def description(self):
        """Concrete method in abstract class"""
        return f"{self.__class__.__name__}: Area={self.area():.2f}, Perimeter={self.perimeter():.2f}"


class CircleShape(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14159 * self.radius


class RectangleShape(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


# shape = Shape()  # TypeError! Cannot instantiate abstract class
circle = CircleShape(5)
rect = RectangleShape(4, 6)
print(circle.description())  # CircleShape: Area=78.54, Perimeter=31.42
print(rect.description())    # RectangleShape: Area=24.00, Perimeter=20.00


# =============================================================
# 7. MAGIC/DUNDER METHODS (Advanced)
# =============================================================

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        """Human-readable string (print)"""
        return f"'{self.title}' by {self.author}"

    def __repr__(self):
        """Developer-readable string (debugging)"""
        return f"Book('{self.title}', '{self.author}', {self.pages})"

    def __len__(self):
        return self.pages

    def __lt__(self, other):
        return self.pages < other.pages

    def __contains__(self, keyword):
        return keyword.lower() in self.title.lower()


book1 = Book("Python Mastery", "Guido", 450)
book2 = Book("Clean Code", "Robert Martin", 320)

print(str(book1))        # 'Python Mastery' by Guido
print(repr(book1))       # Book('Python Mastery', 'Guido', 450)
print(len(book1))        # 450
print(book1 > book2)     # True (450 > 320)
print("Python" in book1) # True


# =============================================================
# 8. COMPOSITION vs INHERITANCE
# =============================================================
# "Has-a" relationship (Composition) vs "Is-a" relationship (Inheritance)

class Engine:
    def __init__(self, horsepower, fuel_type):
        self.horsepower = horsepower
        self.fuel_type = fuel_type

    def start(self):
        return f"{self.fuel_type} engine ({self.horsepower}HP) started"


class GPS:
    def __init__(self):
        self.location = "Unknown"

    def get_location(self):
        return f"Current location: {self.location}"


class ModernCar:
    """Uses composition - Car HAS an Engine and GPS"""

    def __init__(self, brand, model, hp, fuel):
        self.brand = brand
        self.model = model
        self.engine = Engine(hp, fuel)  # Composition
        self.gps = GPS()                # Composition

    def start(self):
        return f"{self.brand} {self.model}: {self.engine.start()}"


tesla = ModernCar("Tesla", "Model S", 670, "Electric")
print(tesla.start())           # Tesla Model S: Electric engine (670HP) started
print(tesla.gps.get_location())  # Current location: Unknown


# =============================================================
# 9. DESIGN PATTERNS (Advanced)
# =============================================================

# --- Singleton Pattern ---
class DatabaseConnection:
    """Only one instance can exist"""
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, host="localhost"):
        self.host = host


db1 = DatabaseConnection("server1")
db2 = DatabaseConnection("server2")
print(db1 is db2)  # True - same instance


# --- Factory Pattern ---
class NotificationFactory:
    """Creates objects without exposing creation logic"""

    @staticmethod
    def create(channel, message):
        if channel == "email":
            return EmailNotification(message)
        elif channel == "sms":
            return SMSNotification(message)
        elif channel == "push":
            return PushNotification(message)
        raise ValueError(f"Unknown channel: {channel}")


class EmailNotification:
    def __init__(self, message):
        self.message = message

    def send(self):
        return f"Email sent: {self.message}"


class SMSNotification:
    def __init__(self, message):
        self.message = message

    def send(self):
        return f"SMS sent: {self.message}"


class PushNotification:
    def __init__(self, message):
        self.message = message

    def send(self):
        return f"Push notification: {self.message}"


notif = NotificationFactory.create("email", "Hello!")
print(notif.send())  # Email sent: Hello!


# --- Observer Pattern ---
class EventManager:
    """Subject that notifies observers"""

    def __init__(self):
        self._subscribers = {}

    def subscribe(self, event_type, listener):
        if event_type not in self._subscribers:
            self._subscribers[event_type] = []
        self._subscribers[event_type].append(listener)

    def notify(self, event_type, data):
        for listener in self._subscribers.get(event_type, []):
            listener.update(data)


class Logger:
    def update(self, data):
        print(f"[LOG] {data}")


class AlertSystem:
    def update(self, data):
        print(f"[ALERT] {data}")


manager = EventManager()
manager.subscribe("error", Logger())
manager.subscribe("error", AlertSystem())
manager.notify("error", "Server crashed!")
# [LOG] Server crashed!
# [ALERT] Server crashed!


# =============================================================
# 10. MIXINS AND MULTIPLE INHERITANCE (Advanced)
# =============================================================

class JsonMixin:
    """Mixin to add JSON serialization capability"""
    import json

    def to_json(self):
        import json
        return json.dumps(self.__dict__, default=str)

    @classmethod
    def from_json(cls, json_str):
        import json
        data = json.loads(json_str)
        return cls(**data)


class LogMixin:
    """Mixin to add logging capability"""

    def log(self, message):
        print(f"[{self.__class__.__name__}] {message}")


class User(JsonMixin, LogMixin):
    def __init__(self, name, email, role="user"):
        self.name = name
        self.email = email
        self.role = role

    def promote(self):
        self.role = "admin"
        self.log(f"{self.name} promoted to admin")


user = User("Alice", "alice@example.com")
print(user.to_json())  # {"name": "Alice", "email": "alice@example.com", "role": "user"}
user.promote()         # [User] Alice promoted to admin


# =============================================================
# 11. DATACLASSES (Modern Python 3.7+)
# =============================================================

from dataclasses import dataclass, field


@dataclass
class Product:
    """Reduces boilerplate for data-holding classes"""
    name: str
    price: float
    quantity: int = 0
    tags: list = field(default_factory=list)

    @property
    def total_value(self):
        return self.price * self.quantity

    def __post_init__(self):
        """Validation after initialization"""
        if self.price < 0:
            raise ValueError("Price cannot be negative")


p1 = Product("Laptop", 999.99, 5, ["electronics", "computers"])
p2 = Product("Laptop", 999.99, 5, ["electronics", "computers"])

print(p1)            # Product(name='Laptop', price=999.99, quantity=5, tags=[...])
print(p1 == p2)      # True (auto-generated __eq__)
print(p1.total_value)  # 4999.95


# =============================================================
# 12. CONTEXT MANAGERS WITH CLASSES
# =============================================================

class FileHandler:
    """Custom context manager using __enter__ and __exit__"""

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        if exc_type:
            print(f"Error occurred: {exc_val}")
        return False  # Don't suppress exceptions


# Usage:
# with FileHandler("test.txt", "w") as f:
#     f.write("Hello OOP!")


# =============================================================
# 13. DESCRIPTORS (Advanced)
# =============================================================

class ValidatedField:
    """Descriptor for type-checked and validated attributes"""

    def __init__(self, field_type, min_val=None, max_val=None):
        self.field_type = field_type
        self.min_val = min_val
        self.max_val = max_val

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return obj.__dict__.get(self.name)

    def __set__(self, obj, value):
        if not isinstance(value, self.field_type):
            raise TypeError(f"{self.name} must be {self.field_type.__name__}")
        if self.min_val is not None and value < self.min_val:
            raise ValueError(f"{self.name} must be >= {self.min_val}")
        if self.max_val is not None and value > self.max_val:
            raise ValueError(f"{self.name} must be <= {self.max_val}")
        obj.__dict__[self.name] = value


class Student:
    name = ValidatedField(str)
    age = ValidatedField(int, min_val=0, max_val=150)
    gpa = ValidatedField(float, min_val=0.0, max_val=4.0)

    def __init__(self, name, age, gpa):
        self.name = name
        self.age = age
        self.gpa = gpa


student = Student("Alice", 21, 3.8)
print(f"{student.name}, Age: {student.age}, GPA: {student.gpa}")

# student.age = -5    # ValueError: age must be >= 0
# student.gpa = 5.0   # ValueError: gpa must be <= 4.0
# student.name = 123  # TypeError: name must be str


# =============================================================
# 14. METACLASSES (Expert Level)
# =============================================================

class SingletonMeta(type):
    """Metaclass that enforces Singleton pattern"""
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class AppConfig(metaclass=SingletonMeta):
    def __init__(self):
        self.settings = {}

    def set(self, key, value):
        self.settings[key] = value

    def get(self, key):
        return self.settings.get(key)


config1 = AppConfig()
config1.set("debug", True)

config2 = AppConfig()
print(config2.get("debug"))  # True (same instance)
print(config1 is config2)    # True


# =============================================================
# SUMMARY TABLE
# =============================================================
"""
| #  | Concept              | Level    | Key Idea                              |
|----|----------------------|----------|---------------------------------------|
| 1  | Class & Object       | Basic    | Blueprint and instance                |
| 2  | Variables/Methods    | Basic    | Instance vs Class vs Static           |
| 3  | Encapsulation        | Basic    | Data hiding with properties           |
| 4  | Inheritance          | Medium   | Code reuse (single/multiple/multi)    |
| 5  | Polymorphism         | Medium   | Same interface, different behavior    |
| 6  | Abstraction          | Medium   | Abstract base classes (ABC)           |
| 7  | Dunder Methods       | Medium   | Customize object behavior             |
| 8  | Composition          | Medium   | "Has-a" vs "Is-a" relationships       |
| 9  | Design Patterns      | Advanced | Singleton, Factory, Observer          |
| 10 | Mixins               | Advanced | Reusable functionality via MI         |
| 11 | Dataclasses          | Advanced | Modern Python data containers         |
| 12 | Context Managers     | Advanced | Resource management (__enter__/exit)  |
| 13 | Descriptors          | Expert   | Attribute access control              |
| 14 | Metaclasses          | Expert   | Classes that create classes           |
"""

# class.mro(), class.__mro__
#Class.mro()-> returns a list
#Class.__mro__ -> returns a tuple

"""Inheritance class"""
Class Person:
    def __init__(self, id, name):
        self.id = id 
        self.name = name
    def printDetails(self):
        print(self.id)
        print(self.name)
        
Class Employee(Person):
    def __init__(self,id, name, sal):
        super().__init__(id, name)
        self.salary = sal
    def printDetails(self):
        super().printDetails()
        print(self.salary)

Class SalesEmployee(Employee):
    def __init__(self, id, name, sal, si):
        super.__init__(id, name, sal)
        self.salesInc = si
    def printDetails(self):
        super.printDetails()
        print(self.salesInc)
        
se = SalesEmployee(101, "rahul", 40000, 2000)
se. printDetails()

e = Employee(102, "Sandy", 50000)
print()
e.printDetails()
