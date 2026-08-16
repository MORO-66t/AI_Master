from model.person import Person


class Patient(Person):
    """class for hospital patients, inherits from Person"""

    def __init__(self, name, age, medical_record):
        super().__init__(name, age)
        self.medical_record = medical_record

    def view_record(self):
        """view the patient record"""
        return f"Patient Name: {self.name}, Age: {self.age}, Medical Record: {self.medical_record}"
