from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, first_name, initial_name, last_name):
        self.first_name = first_name
        self.initial_name = initial_name
        self.last_name = last_name

    @abstractmethod
    def calculate_monthly_pay(self):
        pass

    def display_details(self):
        print(f"Name: {self.first_name} {self.initial_name}. {self.last_name}")

class SalaryEmployee(Employee):
    def __init__(self, first_name, initial_name, last_name, monthly_salary):
        super().__init__(first_name, initial_name, last_name)
        self.monthly_salary = monthly_salary

    def calculate_monthly_pay(self):
        return self.monthly_salary

class HourlyEmployee(Employee):
    def __init__(self, first_name, initial_name, last_name, hours_worked, hourly_rate):
        super().__init__(first_name, initial_name, last_name)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_monthly_pay(self):
        return self.hours_worked * self.hourly_rate

def main():
    employees = []

    se = SalaryEmployee("Jane", "B", "Smith", 5000.00)
    he = HourlyEmployee("Bob", "C", "Johnson", 160, 25.50)

    employees.append(se)
    employees.append(he)

    for emp in employees:
        emp.display_details()
        print(f"Monthly Pay: ${emp.calculate_monthly_pay():.2f}")
        print("--------------------------------")

if __name__ == "__main__":
    main()
