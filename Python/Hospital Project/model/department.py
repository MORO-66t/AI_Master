class Department:
    """class representing a department in the hospital"""

    _id_counter = 1

    def __init__(self, name):
        self.department_id = Department._id_counter
        Department._id_counter += 1
        self.name = name
        self.patients = []
        self.staff = []

    def __str__(self):
        return (f"Department ID: {self.department_id}, Name: {self.name}, "
                f"Patients: {len(self.patients)}, Staff: {len(self.staff)}")

    def add_patient(self, patient):
        """add a patient to the department"""
        if patient in self.patients:
            print(f"Patient '{patient.name}' is already in {self.name}.")
            return
        self.patients.append(patient)
        print(f"Patient '{patient.name}' added to {self.name} department.")

    def remove_patient(self, patient_name):
        """remove a patient from the department by name"""
        for patient in self.patients:
            if patient.name.lower() == patient_name.lower():
                self.patients.remove(patient)
                print(f"Patient '{patient_name}' removed from {self.name}.")
                return
        print(f"Patient '{patient_name}' not found in {self.name}.")

    def add_staff(self, staff_member):
        """add staff member to the department"""
        if staff_member in self.staff:
            print(f"Staff '{staff_member.name}' is already in {self.name}.")
            return
        self.staff.append(staff_member)
        print(f"Staff '{staff_member.name}' added to {self.name} department.")

    def remove_staff(self, staff_name):
        """remove staff member from the department by name"""
        for member in self.staff:
            if member.name.lower() == staff_name.lower():
                self.staff.remove(member)
                print(f"Staff '{staff_name}' removed from {self.name}.")
                return
        print(f"Staff '{staff_name}' not found in {self.name}.")
