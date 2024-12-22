class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        return "Ця тварина видає звук."

    def get_info(self):
        return f"Ім'я: {self.name}, Вік: {self.age}"


class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def speak(self):
        return "Гав-гав!"

    def get_info(self):
        return f"Собака: {self.name}, Вік: {self.age}, Порода: {self.breed}"


class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        return "Мяу!"

    def get_info(self):
        return f"Кіт: {self.name}, Вік: {self.age}, Колір: {self.color}"


if __name__ == "__main__":
    my_dog = Dog(name="Барсик", age=3, breed="Німецька вівчарка")
    my_cat = Cat(name="Мурчик", age=2, color="Рудий")

    print(my_dog.get_info())
    print(my_dog.speak())
    print(my_cat.get_info())
    print(my_cat.speak())