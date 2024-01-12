# ..---__OOPS Concepts with examples in Python___--...--

# ...----------Class and object in python---..
class Dog:
    def __init__(self,name):
        self.name = name

    def bark(self):
        print(f"{self.name} says boow")

dog1=Dog("buddy")

dog1.bark()

# ______.....Inheritance Example______.....

class Animal:
    def __init__(self,name):
        self.name=name

class Dog(Animal):
    def speak(self):
        print(f"{self.name} is saying orayya")

class cat(Animal):
    def bark(self):
        print(f"{self.name} is saying poda")
        
wolf=Dog("Madmax")
Jaguar=cat("Bigcat")

wolf.speak()
Jaguar.bark()

# --__---__PolyMorphism__---__


class Vehicle:
    def __init__(self,name):
        self.name=name

    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        return f"{self.name} is driving on highway"

class small_lorry(Vehicle):
     def move(self):
        return f"{self.name} is rash driving in water and moon but good on highway"
 # Function to demonstrate polymorphism   
def journey(Vehicle):
    print(Vehicle.move())

# Creating instances of different vehicles
car=Car("Fortuner")
Lorry=small_lorry("TATA GOLD")

#Using polymorphism in action
journey(car)
journey(Lorry)

# In this example, we have a base class Vehicle with a move method. 
# Three subclasses (Car, Boat, and Plane) inherit from Vehicle and override the move method 
# with their own implementations. The travel function takes a Vehicle object as an argument and calls its move method, demonstrating polymorphism.



