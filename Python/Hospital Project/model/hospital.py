class Hospital:
    """class representing a hospital"""

    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.departments = {} 

    def add_department(self, department):
        """add a department to the hospital"""
        self.departments[department.department_id] = department
        print(f"Department '{department.name}' added to {self.name}.")

    def remove_department(self, department_id):
        """remove a department from the hospital"""
        if department_id in self.departments:
            department = self.departments[department_id]
            if department.patients or department.staff:
                print(f"Department '{department.name}' has patients or staff. Cannot remove.")
            else:
                del self.departments[department_id]
                print(f"Department '{department.name}' removed from {self.name}.")
        else:
            print("Invalid department ID.")

    def get_all_departments(self):
        """return all the departments in the hospital"""
        return list(self.departments.values())
