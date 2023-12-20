# + methoden
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

    def total_employees(self):
        total_employees = 0
        total_department_heads = 0

        for department in self.departments:
            total_employees += len(department.employees)
            if department.department_head is not None:
                total_department_heads += 1

        return total_employees, total_department_heads

    def total_departments(self):
        return len(self.departments)

    def largest_department(self):
        max_employees = 0
        largest_department = None

        for department in self.departments:
            if len(department.employees) > max_employees:
                max_employees = len(department.employees)
                largest_department = department.name

        return largest_department

    def gender_percentage(self):
        total_employees = 0
        female_count = 0

        for department in self.departments:
            for employee in department.employees:
                total_employees += 1
                if employee.gender.lower() == 'female':
                    female_count += 1

        male_count = total_employees - female_count
        if total_employees == 0:
            return 0, 0

        female_percentage = (female_count / total_employees) * 100
        male_percentage = (male_count / total_employees) * 100

        return female_percentage, male_percentage


# Beispiel-Nutzung:

# Schritt 1: Erstelle Personen, Mitarbeiter und Abteilungsleiter

person1XYZ = Person("Alice", "Female")
employee1XYZ = Employee("Bob", "Male", "E001", "HR")
department_head1XYZ = DepartmentHead("Charlie", "Male", "E002", "IT", "IT Manager")

# Schritt 2: Erstelle Abteilungen und füge Mitarbeiter hinzu
hr_departmentXYZ = Department("HR Department")
hr_departmentXYZ.set_department_head(department_head1XYZ)
hr_departmentXYZ.add_employee(person1XYZ)
hr_departmentXYZ.add_employee(employee1XYZ)

it_departmentXYZ = Department("IT Department")
it_departmentXYZ.set_department_head(department_head1XYZ)
it_departmentXYZ.add_employee(employee1XYZ)

# Schritt 3: Erstelle die Firma und füge Abteilungen hinzu
companyXYZ = Company("XYZ Company")
companyXYZ.add_department(hr_departmentXYZ)
companyXYZ.add_department(it_departmentXYZ)

# Schritt 4: Beispiel-Ausgabe

print(f"Erstellte Firma: {companyXYZ.name}")
print(f"Abteilungen ({companyXYZ.name}): {hr_departmentXYZ.name}, {it_departmentXYZ.name}")
print("\n")

print(f"Person 1 ({companyXYZ.name}): {person1XYZ.name} {person1XYZ.gender}")
print(f"Employee 1 ({companyXYZ.name}): {employee1XYZ.name} {employee1XYZ.gender} {employee1XYZ.employee_id} {employee1XYZ.department}")
print(f"Department-Head 1 ({companyXYZ.name}): {department_head1XYZ.name} {department_head1XYZ.gender} {department_head1XYZ.employee_id} {department_head1XYZ.department} {department_head1XYZ.title}")
print("\n")

total_employees, total_department_heads = companyXYZ.total_employees()
print(f"Gesamtzahl Mitarbeiter ({companyXYZ.name}): {total_employees}")
print(f"Gesamtzahl Abteilungsleiter ({companyXYZ.name}): {total_department_heads}")
print("\n")

total_departments = companyXYZ.total_departments()
print(f"Gesamtzahl Abteilungen ({companyXYZ.name}): {total_departments}")

largest_department = companyXYZ.largest_department()
print(f"Abteilung mit der größten Mitarbeiterstärke ({companyXYZ.name}): {largest_department}")

female_percentage, male_percentage = companyXYZ.gender_percentage()
print(f"Prozentanteil Frauen ({companyXYZ.name}): {female_percentage:.2f}%")
print(f"Prozentanteil Männer ({companyXYZ.name}): {male_percentage:.2f}%")
