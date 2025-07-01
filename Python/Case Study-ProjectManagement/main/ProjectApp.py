from util.DBConnUtil import DBConnUtil
from dao.ProjectRepositoryImpl import ProjectRepositoryImpl
from entity.Project import Project
from entity.Employee import Employee
from entity.Task import Task
from exception.EmployeeNotFoundException import EmployeeNotFoundException
from exception.ProjectNotFoundException import ProjectNotFoundException
from util.StatusEnum import ProjectStatus, TaskStatus

def test_connection():
    conn = DBConnUtil.get_connection()
    print("✅ Connected to SQL Server" if conn else "❌ Connection failed")
    if conn:
        conn.close()

repo = ProjectRepositoryImpl()

def add_employee():
    e = Employee(
        id=int(input("Employee ID: ")),
        name=input("Name: "),
        designation=input("Designation: "),
        gender=input("Gender: "),
        salary=float(input("Salary: ")),
        project_id=None
    )
    print("✅ Added" if repo.create_employee(e) else "❌ Failed to add")

def add_project():
    pid = int(input("Project ID: "))
    pname = input("Project Name: ")
    desc = input("Description: ")
    sdate = input("Start Date (YYYY-MM-DD): ")
    allowed = "('started','dev','build','test','deployed')"
    status_input = input(f"Status {allowed}: ").strip()
    if status_input not in [s.value for s in ProjectStatus]:
        print(f"❌ Invalid status. Must be one of {allowed}")
        return
    p = Project(
        id=pid,
        project_name=pname,
        description=desc,
        start_date=sdate,
        status=status_input
    )
    print("✅ Project added!" if repo.create_project(p) else "❌ Failed to add project")

def add_task():
    tid = int(input("Task ID: "))
    tname = input("Task Name: ")
    pid = int(input("Project ID: "))
    t = Task(task_id=tid, task_name=tname, project_id=pid, employee_id=None, status=None)
    print("✅ Task added to project!" if repo.create_task(t) else "❌ Failed to add task")

def assign_project():
    pid = int(input("Project ID: "))
    eid = int(input("Employee ID: "))
    print("✅ Project Assigned" if repo.assign_project_to_employee(pid, eid) else "❌ Failed to assign project")

def assign_task():
    tid = int(input("Task ID: "))
    pid = int(input("Project ID: "))
    eid = int(input("Employee ID: "))
    allowed = "('Assigned','Started','Completed')"
    status_input = input(f"Status {allowed}: ").strip()
    if status_input not in [s.value for s in TaskStatus]:
        print(f"❌ Invalid status. Must be one of {allowed}")
        return
    print("✅ Task Assigned" if repo.assign_task_in_project_to_employee(tid, pid, eid, status_input)
          else "❌ Failed to assign task")

def delete_employee():
    eid = int(input("Employee ID to delete: "))
    try:
        if repo.delete_employee(eid):
            print("✅ Deleted")
        else:
            raise EmployeeNotFoundException(f"Employee {eid} not found")
    except EmployeeNotFoundException as ex:
        print("⚠️", ex)

def delete_task():
    tid = int(input("Task ID to delete: "))
    print("✅ Deleted" if repo.delete_task(tid) else "⚠️ Task not found or deletion failed")

def list_tasks():
    eid = int(input("Employee ID: "))
    emp = repo.get_employee_by_id(eid)
    emp_name = emp.name if emp else "Unknown"
    tasks = repo.get_all_tasks(eid)
    if not tasks:
        print("No projects or tasks found for this employee.")
    else:
        for t in tasks:
            print(f"Employee: {emp_name} | Task ID: {t.task_id} | Project ID: {t.project_id} | "
                  f"Task Name: {t.task_name} | Status: {t.status}")

def main_menu():
    menu = """
1. Add Employee
2. Add Project
3. Add Task (project only)
4. Assign Project to Employee
5. Assign Task within a Project to Employee
6. Delete Employee
7. Delete Task
8. List all projects assigned with tasks to an employee
9. Exit
"""
    options = {
        '1': add_employee,
        '2': add_project,
        '3': add_task,
        '4': assign_project,
        '5': assign_task,
        '6': delete_employee,
        '7': delete_task,
        '8': list_tasks,
        '9': exit
    }
    while True:
        print(menu)
        choice = input("Choose option (1–9): ").strip()
        action = options.get(choice)
        if action:
            action()
        else:
            print("❌ Invalid choice, try again.")

if __name__ == "__main__":
    test_connection()
    main_menu()
