class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Використання:
animals = [Dog(), Cat()]
for animal in animals:
    print(animal.speak())
    class Fish(Animal):
        pass

    animals.append(Fish())