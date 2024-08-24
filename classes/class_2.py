
class User:
    def __init__(self, name, birthyear):
        self.name = name
        self.birthyear = birthyear

    def get_name(self):
        cap_name = self.name.capitalize()
        print("The name is " + cap_name + ".")

    def age(self, current_year):
        self.current_year = current_year
        age = self.current_year - self.birthyear
        print("Your age is " + str(age) + ".")

u1 = User('xyz', 1987)
u2 = User('rst', 1965)
u1.get_name()
u1.age(2024)