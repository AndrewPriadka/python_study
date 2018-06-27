class Person:

    def __init__(self, name,surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def print_info(self):
        print(self.name, self.surname, self.age)


alex = Person('Alex', 'Stone', 32)

alex.print_info()
