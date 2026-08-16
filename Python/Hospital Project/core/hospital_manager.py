from model.hospital import Hospital
from model.department import Department
from model.patient import Patient
from model.staff import Staff


class HospitalManager:
    """manager class that handles all the hospital operations"""

    def __init__(self):
        self.hospital = Hospital("City Hospital", "123 Main St")

    def add_department(self, name):
        if not name.strip():
            print("Error: Department name cannot be empty.")
            return None
        department = Department(name)
        self.hospital.add_department(department)
        return department.department_id

    def remove_department(self, department_id):
        self.hospital.remove_department(department_id)

    def get_all_departments(self):
        return self.hospital.get_all_departments()

    def search_departments(self, search_name):
        result = []
        for department in self.hospital.get_all_departments():
            if search_name.lower() in department.name.lower():
                result.append(department)
        return result

    def _find_department(self, department_id):
        """helper: return a department by id, or None if not found"""
        if department_id in self.hospital.departments:
            return self.hospital.departments[department_id]
        print("Invalid department ID.")
        return None

    def add_patient(self, department_id, name, age, medical_record):
        department = self._find_department(department_id)
        if department is None:
            return
        if not name.strip():
            print("Error: Patient name cannot be empty.")
            return
        patient = Patient(name, age, medical_record)
        department.add_patient(patient)

    def remove_patient(self, department_id, patient_name):
        department = self._find_department(department_id)
        if department is not None:
            department.remove_patient(patient_name)

    def get_patients(self, department_id):
        department = self._find_department(department_id)
        if department is not None:
            return department.patients
        return []

    def add_staff(self, department_id, name, age, position):
        department = self._find_department(department_id)
        if department is None:
            return
        if not name.strip():
            print("Error: Staff name cannot be empty.")
            return
        staff = Staff(name, age, position)
        department.add_staff(staff)

    def remove_staff(self, department_id, staff_name):
        department = self._find_department(department_id)
        if department is not None:
            department.remove_staff(staff_name)

    def get_staff(self, department_id):
        department = self._find_department(department_id)
        if department is not None:
            return department.staff
        return []
