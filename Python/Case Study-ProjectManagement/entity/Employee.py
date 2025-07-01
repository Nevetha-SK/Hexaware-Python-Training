# entity/Employee.py
class Employee:
    def __init__(self, id=None, name=None, designation=None, gender=None, salary=None, project_id=None):
        self.id = id
        self.name = name
        self.designation = designation
        self.gender = gender
        self.salary = salary
        self.project_id = project_id
