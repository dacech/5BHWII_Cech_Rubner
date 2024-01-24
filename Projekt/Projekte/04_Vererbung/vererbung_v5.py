#gender bool
# main
class Person:
    def __init__(self, name, is_female):
        self.name = name
        self.is_female = is_female

    def display_info(self):
        gender = "Female" if self.is_female else "Male"
        print(f"Name: {self.name}, Gender: {gender}")


class Employee(Person):
    def __init__(self, name, is_female, employee_id, department):
        super().__init__(name, is_female)
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
    def __init__(self, name, is_female, employee_id, department, title):
        super().__init__(name, is_female, employee_id, department)
        self.title = title


class Company:
    def __init__(self, name):
        self.name = name
        self.departments = []

    def add_department(self, department):
        self.departments.append(department)

    def total_employees(self):
        total_employees = sum(len(department.employees) for department in self.departments)
        total_department_heads = sum(1 for department in self.departments if department.department_head is not None)
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
        total_employees = sum(len(department.employees) for department in self.departments)
        female_count = sum(1 for department in self.departments for employee in department.employees if employee.is_female)

        if total_employees == 0:
            return 0, 0

        female_percentage = (female_count / total_employees) * 100
        male_percentage = 100 - female_percentage

        return female_percentage, male_percentage


# Beispiel-Nutzung:

def main():
    person1XYZ = Person("Alice", True)  # True for Female
    employee1XYZ = Employee("Bob", False, "E001", "HR")  # False for Male
    department_head1XYZ = DepartmentHead("Charlie", False, "E002", "IT", "IT Manager")  # False for Male

    hr_departmentXYZ = Department("HR Department")
    hr_departmentXYZ.set_department_head(department_head1XYZ)
    hr_departmentXYZ.add_employee(person1XYZ)
    hr_departmentXYZ.add_employee(employee1XYZ)

    it_departmentXYZ = Department("IT Department")
    it_departmentXYZ.set_department_head(department_head1XYZ)
    it_departmentXYZ.add_employee(employee1XYZ)

    companyXYZ = Company("XYZ Company")
    companyXYZ.add_department(hr_departmentXYZ)
    companyXYZ.add_department(it_departmentXYZ)

    print_company_info(companyXYZ)


def print_company_info(company):
    print(f"Erstellte Firma: {company.name}")

    for department in company.departments:
        print(f"Abteilungen ({company.name}): {department.name}")

    print("\n")

    for department in company.departments:
        for employee in department.employees:
            employee.display_info()

    print("\n")

    total_employees, total_department_heads = company.total_employees()
    print(f"Gesamtzahl Mitarbeiter ({company.name}): {total_employees}")
    print(f"Gesamtzahl Abteilungsleiter ({company.name}): {total_department_heads}")
    print("\n")

    total_departments = company.total_departments()
    print(f"Gesamtzahl Abteilungen ({company.name}): {total_departments}")

    largest_department = company.largest_department()
    print(f"Abteilung mit der größten Mitarbeiterstärke ({company.name}): {largest_department}")

    female_percentage, male_percentage = company.gender_percentage()
    print(f"Prozentanteil Frauen ({company.name}): {female_percentage:.2f}%")
    print(f"Prozentanteil Männer ({company.name}): {male_percentage:.2f}%")


if __name__ == "__main__":
    main()
