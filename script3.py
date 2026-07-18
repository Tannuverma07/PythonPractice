class = Animal
    def sound(self):
        print("Animal is makes sound")
class Dog(Animal):
    def sound(self):
        print("Dog barks")
Dog = Dog()
Dog.sound()