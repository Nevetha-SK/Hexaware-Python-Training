# entity/Task.py
class Task:
    def __init__(self, task_id=None, task_name=None, project_id=None,
                 employee_id=None, status=None):
        self.task_id = task_id
        self.task_name = task_name
        self.project_id = project_id
        self.employee_id = employee_id
        self.status = status
