from datetime import datetime
import csv
import json


class Employee:
    def __init__(self, last_name, first_name, middle_name, position, hire_date, salary):
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.position = position
        self.hire_date = datetime.strptime(hire_date, "%d.%m.%Y")
        self.salary = salary

    def years_in_company(self):
        return (datetime.now() - self.hire_date).days // 365

    def is_programmer(self):
        return 'программист' in self.position.lower()

    def is_female(self):
        female_names = ['Анна', 'Екатерина', 'Алина', 'Светлана', 'Мария']
        return self.first_name in female_names

    def calculate_bonus_programmer(self):
        if self.is_programmer():
            return self.salary * 0.03
        return 0

    def calculate_bonus_march(self):
        if self.is_female():
            return 2000
        return 0

    def calculate_bonus_february(self):
        if not self.is_female():
            return 2000
        return 0

    def calculate_salary_increase(self):
        if self.years_in_company() > 10:
            return self.salary * 0.07
        else:
            return self.salary * 0.05

    def worked_more_than_six_months(self):
        return (datetime.now() - self.hire_date).days > 183


employees = [
    Employee("Иванов", "Иван", "Иванович", "Менеджер", "22.10.2013", 250000),
    Employee("Сорокина", "Екатерина", "Матвеевна",
             "Аналитик", "12.03.2020", 75000),
    Employee("Струков", "Иван", "Сергеевич",
             "Старший программист", "23.04.2012", 150000),
    Employee("Корнеева", "Анна", "Игоревна",
             "Ведущий программист", "22.02.2015", 120000),
    Employee("Старчиков", "Сергей", "Анатольевич",
             "Младший программист", "12.11.2021", 50000),
    Employee("Бутенко", "Артем", "Андреевич",
             "Архитектор", "12.02.2010", 200000),
    Employee("Савченко", "Алина", "Сергеевна",
             "Старший аналитик", "13.04.2016", 100000)
]


def calculate_bonuses_and_increases(employees):
    for employee in employees:
        programmer_bonus = employee.calculate_bonus_programmer()
        march_bonus = employee.calculate_bonus_march()
        february_bonus = employee.calculate_bonus_february()
        salary_increase = employee.calculate_salary_increase()

        print(f"{employee.first_name} {employee.last_name}:")
        print(f"  Премия программиста: {programmer_bonus}")
        print(f"  Премия к 8 марта: {march_bonus}")
        print(f"  Премия к 23 февраля: {february_bonus}")
        print(f"  Индексация зарплаты: {salary_increase}")


def employees_worked_more_than_six_months(employees):
    return [emp for emp in employees if emp.worked_more_than_six_months()]


def write_to_csv(employees, filename="employees.csv"):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Фамилия", "Имя", "Отчество",
                        "Должность", "Дата найма", "Оклад"])
        for emp in employees:
            writer.writerow([emp.last_name, emp.first_name, emp.middle_name,
                            emp.position, emp.hire_date.strftime("%d.%m.%Y"), emp.salary])


def write_to_json(employees, filename="employees.json"):
    with open(filename, mode='w', encoding='utf-8') as file:
        json.dump([emp.__dict__ for emp in employees],
                  file, ensure_ascii=False, indent=4)


calculate_bonuses_and_increases(employees)
worked_employees = employees_worked_more_than_six_months(employees)
print("nСотрудники, отработавшие более 6 месяцев:")

for emp in worked_employees:
    print(f"{emp.first_name} {emp.last_name}")

write_to_csv(employees)
write_to_json(employees)
