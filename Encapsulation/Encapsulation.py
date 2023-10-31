# What is encapsulation?
# Access modifers
# Benefits of encapsulation
# Implemntation of encapsulation

#public- front door
#protected- back door
#private- secret door

class House:
    def __init__(self):

        #public attribute
        self.front_door = "Access granted to Public front door"

        #protected attribute
        self._back_door = "Access granted to Protected back door"

        #private attribute
        self.__secret_door = "Access granted to Private Secret door"
    
    #public method
    def enter_front_door(self):
        return f"Welcome throug the {self.front_door}!"

    #protected method
    def _enter_back_door(self):
        return f"Welcome throug the {self._back_door}"
    
    #private method
    def __enter_secret_door(self):
        return f"Welcome through the {self.__secret_door}"

my_house = House()

print(my_house.front_door) #access to door
print(my_house.enter_front_door()) #walking through door

print(my_house._back_door) #acces to door
print(my_house.enter_back_door()) #walking through door

print(my_house.__secret_door)
print(my_house.__enter_secret_door()) # Error: 'House' object has no attribute '__enter_secret_door'

# Accessing through the private method (using name mangling)
# print(my_house._House__secret_door) #access to door
# print(my_house__enter_secret_door()) #walking through door

