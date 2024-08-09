class Dog() :
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sit(self):
        print(self.name.title()+" is now sitting!")
    def rolling_over(self):
        print(self.name.title() +" just rolled over!!")

my_dog = Dog('willie', 4)
print("My dog's name is "+my_dog.name+".")
print("My dog is "+str(my_dog.age)+" years old!")
my_dog.sit()
my_dog.rolling_over()
