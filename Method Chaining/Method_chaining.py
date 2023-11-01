class Person:

    def set_name(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        return self
    
    def set_age(self, age):
        self.age = age
        return self

    def set_address(self, address):
        self.address = address
        return self

    def display_info(self):
        print(f"Name: {self.first_name} {self.last_name}, Age: {self.age}, Address: {self.address}")

person = Person()
person.set_age(25)
person.set_name("Jane", "Smith")
person.set_address("123 Main St")
person.display_info()

person2 = Person().set_age(30).set_name("John", "Doe").set_address("456 Elm St").display_info()