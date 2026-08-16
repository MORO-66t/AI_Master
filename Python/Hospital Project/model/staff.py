from model.person import Person


class Staff(Person):
    """class for hospital staff, inherits from Person"""

    def __init__(self, name, age, position):
        super().__init__(name, age)
        self.position = position

    def view_info(self):
        """view staff information"""
        return f"Staff Name: {self.name}, Age: {self.age}, Position: {self.position}"
