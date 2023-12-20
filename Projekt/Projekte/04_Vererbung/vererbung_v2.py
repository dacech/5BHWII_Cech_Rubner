#nur ein Departmenthead
class Person:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def display_info(self):
        print(f"Name: {self.name}, Gender: {self.gender}")


class Employee(Person):
    def __init__(self, name, gender, employee_id, department):
        super().__init__(name, gender)
        self.employee_id = employee_id
        self.department = department

    def display_info(self):
        super().display_info()
        print(f"Employee ID: {self.employee_id}, Department: {self.department}")


class Department:
    def __init__(self, name):
        self.name = name
        self.department_head = None
        self.employees = []

    def set_department_head(self, department_head):
        if self.department_head is None:
            self.department_head = department_head
        else:
            print("Error: Department already has a department head.")

    def add_employee(self, employee):
        self.employees.append(employee)


class DepartmentHead(Employee):
    def __init__(self, name, gender, employee_id, department, title):
        super().__init__(name, gender, employee_id, department)
        self.title = title


class Company:
    def __init__(self, name):
        self.name = name
        self.departments = []

    def add_department(self, department):
        self.departments.append(department)


# Beispiel-Nutzung:

# Erstelle Personen, Mitarbeiter und Abteilungsleiter
person1 = Person("Alice", "Female")
employee1 = Employee("Bob", "Male", "E001", "HR")
department_head1 = DepartmentHead("Charlie", "Male", "E002", "IT", "IT Manager")

# Erstelle Abteilungen und füge Mitarbeiter hinzu
hr_department = Department("HR Department")
hr_department.set_department_head(department_head1)
hr_department.add_employee(person1)
hr_department.add_employee(employee1)

it_department = Department("IT Department")
it_department.set_department_head(department_head1)  # Dies wird einen Fehler auslösen
it_department.add_employee(employee1)

# Erstelle die Firma und füge Abteilungen hinzu
company = Company("XYZ Company")
company.add_department(hr_department)
company.add_department(it_department)

# Beispiel-Ausgabe
print(f"Company: {company.name}")
for department in company.departments:
    print(f"\nDepartment: {department.name}")
    print(f"Department Head: {department.department_head.name}")
    print("Employees:")
    for employee in department.employees:
        employee.display_info()
    print("\n------------------------")
