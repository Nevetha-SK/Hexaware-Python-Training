# entity/Project.py
class Project:
    def __init__(self, id=None, project_name=None, description=None, start_date=None, status=None):
        self.id = id
        self.project_name = project_name
        self.description = description
        self.start_date = start_date
        self.status = status
