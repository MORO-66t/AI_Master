from core.hospital_manager import HospitalManager


def show_menu():
    print("\n" + "=" * 50)
    print("1. Add department")
    print("2. Remove department")
    print("3. Add patient to a department")
    print("4. Remove patient from a department")
    print("5. Add staff to a department")
    print("6. Remove staff from a department")
    print("7. Search departments")
    print("8. Get all departments")
    print("9. Get all patients of a department")
    print("10. Get all staff of a department")
    print("11. Exit")
    print("=" * 50)


def add_department(manager):
    name = input("Enter department name: ").strip()
    dept_id = manager.add_department(name)
    if dept_id is not None:
        print("Department ID:", dept_id)


def remove_department(manager):
    try:
        dept_id = int(input("Enter department ID: "))
        manager.remove_department(dept_id)
    except ValueError:
        print("Invalid input. Department ID must be an integer.")


def add_patient(manager):
    try:
        dept_id = int(input("Enter department ID: "))
        name = input("Enter patient name: ").strip()
        age = int(input("Enter patient age: "))
        record = input("Enter medical record: ").strip()
        manager.add_patient(dept_id, name, age, record)
    except ValueError:
        print("Invalid input. Department ID and age must be integers.")


def remove_patient(manager):
    try:
        dept_id = int(input("Enter department ID: "))
    except ValueError:
        print("Invalid input. Department ID must be an integer.")
        return
    name = input("Enter patient name: ").strip()
    manager.remove_patient(dept_id, name)


def add_staff(manager):
    try:
        dept_id = int(input("Enter department ID: "))
        name = input("Enter staff name: ").strip()
        age = int(input("Enter staff age: "))
        position = input("Enter position: ").strip()
        manager.add_staff(dept_id, name, age, position)
    except ValueError:
        print("Invalid input. Department ID and age must be integers.")


def remove_staff(manager):
    try:
        dept_id = int(input("Enter department ID: "))
    except ValueError:
        print("Invalid input. Department ID must be an integer.")
        return
    name = input("Enter staff name: ").strip()
    manager.remove_staff(dept_id, name)


def search_departments(manager):
    search_name = input("Enter department name to search: ").strip()
    departments = manager.search_departments(search_name)
    if departments:
        print("Matching departments:")
        for department in departments:
            print(department)
    else:
        print("No departments found with that name.")


def get_all_departments(manager):
    departments = manager.get_all_departments()
    if departments:
        print("All departments:")
        for department in departments:
            print(department)
    else:
        print("No departments found.")


def get_patients(manager):
    try:
        dept_id = int(input("Enter department ID: "))
    except ValueError:
        print("Invalid input. Department ID must be an integer.")
        return
    patients = manager.get_patients(dept_id)
    if patients:
        print("Patients:")
        for patient in patients:
            print(patient.view_record())
    else:
        print("No patients in this department.")


def get_staff(manager):
    try:
        dept_id = int(input("Enter department ID: "))
    except ValueError:
        print("Invalid input. Department ID must be an integer.")
        return
    staff = manager.get_staff(dept_id)
    if staff:
        print("Staff:")
        for member in staff:
            print(member.view_info())
    else:
        print("No staff in this department.")


def core():
    manager = HospitalManager()
    while True:
        show_menu()
        choice = input("Enter choice: ").strip()

        if choice == '1':
            add_department(manager)
        elif choice == '2':
            remove_department(manager)
        elif choice == '3':
            add_patient(manager)
        elif choice == '4':
            remove_patient(manager)
        elif choice == '5':
            add_staff(manager)
        elif choice == '6':
            remove_staff(manager)
        elif choice == '7':
            search_departments(manager)
        elif choice == '8':
            get_all_departments(manager)
        elif choice == '9':
            get_patients(manager)
        elif choice == '10':
            get_staff(manager)
        elif choice == '11':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 11.")


if __name__ == "__main__":
    core()
