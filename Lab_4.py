class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"{self.emp_id} {self.name} {self.age} {self.salary}"

class EmployeeTable:
    def __init__(self):
        self.employees = []

    def add_employee(self, emp):
        self.employees.append(emp)

    def search_by_age(self, age):
        return [emp for emp in self.employees if emp.age == age]

    def search_by_name(self, name):
        return [emp for emp in self.employees if emp.name == name]

    def search_by_salary(self, operator, salary):
        if operator == ">":
            return [emp for emp in self.employees if emp.salary > salary]
        elif operator == "<":
            return [emp for emp in self.employees if emp.salary < salary]
        elif operator == ">=":
            return [emp for emp in self.employees if emp.salary >= salary]
        elif operator == "<=":
            return [emp for emp in self.employees if emp.salary <= salary]

if __name__ == "__main__":
    table = EmployeeTable()
    table.add_employee(Employee("161E90", "Raman", 41, 56000))
    table.add_employee(Employee("161F91", "Himadri", 38, 67500))
    table.add_employee(Employee("161F99", "Jaya", 51, 82100))
    table.add_employee(Employee("171E20", "Tejas", 30, 55000))
    table.add_employee(Employee("171G30", "Ajay", 45, 44000))

    print("Please choose the search parameter:")
    print("[1] Age\n[2] Name\n[3] Salary (>, <, <=, >=)")
    choice = input("Enter your choice: ")

    if choice == "1":
        age = int(input("Enter the age: "))
        result = table.search_by_age(age)
    elif choice == "2":
        name = input("Enter the name: ")
        result = table.search_by_name(name)
    elif choice == "3":
        operator = input("Enter the operator: ")
        salary = int(input("Enter the salary: "))
        result = table.search_by_salary(operator, salary)

    print("\nSearch Results:")
    for r in result:
        print(r)
