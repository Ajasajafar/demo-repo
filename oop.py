# name = 'Danny'
# age = 29
# print(type(name))
# print(type(age))

# class Dog:
#     def __init__(self, name, breed, owner):
#         self.name = name
#         self.breed = breed
#         self.owner = owner
#     def bark(self):
#         print('Whoah Whoahf!!')

# class Owner:
#     def __init__(self, name, address, contact_number):
#         self.name = name
#         self.address = address
#         self.contact = contact_number


# owner1 = Owner("Ajasa", "35, Wahab-larinde street", "09068938558")
# dog1 = Dog('Sparrow', 'Local Dog', owner1)
# print(dog1.owner.address)


# owner2 = Owner("Tajudeen", "1, Church Street", "08088967968")
# dog2 = Dog("Cleo", "Chiuaua", owner2)

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age =  age
#     def greet(self):
#         print(f"My name is {self.name} and I am {self.age} years old")

# person1 = Person("Ajasa", 19)
# person1.greet()

# Accessing Modifying Object data
class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
    def say_hi_to_user(self, user):
        print(f"Sending message to {user.name}: Hi {user.name}, It's {self.name}.")

user1 = User("Ajasa", "bolarinwaayorinde97@gmIL.com", "123")
user2 = User('Oti', "otitheekrerator@yahoo.com", '419')

user1.say_hi_to_user(user2)

# Access Modifiers: Protected attributes
