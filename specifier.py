class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary  # Internal/protected variable

    # 1. The Getter method:-
    @property
    def salary(self):
        """Retrieves the value of salary."""
        print("Fetching salary...")
        return self._salary

    # 2. The Setter Method:-
    @salary.setter
    def salary(self, value):
        """Validates and sets the value of salary."""
        if value < 0:
            raise ValueError("Salary cannot be negative!")
        print("Setting salary...")
        self._salary = value
emp = Employee("RituRaj", 50000)
print(emp.salary)
emp.salary = 60000
