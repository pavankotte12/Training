# Employee class with employee and manager salaries 

# Define the base class
class Employee:
    # Constructor to initialize the employee's name and salary
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    # Method to return salary
    def annual_salary(self):
        return self.salary * 12

# Define the manager subclass
class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

     # Override the annual_salary method
    def annual_salary(self):
        return (self.salary * 12) + self.bonus

# Create Employee and Manager objects
employee = Employee("Rahul", 50000)
manager = Manager("Akash", 100000, 150000)

# Print annual salaries
print(employee.name, "Annual Salary:", employee.annual_salary())
print(manager.name, "Annual Salary:", manager.annual_salary())