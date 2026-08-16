class Person:
    """base class for all people in the hospital"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def view_info(self):
        """view basic information about the person"""
        return f"Name: {self.name}, Age: {self.age}"
