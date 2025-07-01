import pyodbc
from dao.IProjectRepository import IProjectRepository
from util.DBConnUtil import DBConnUtil
from entity.Project import Project
from entity.Employee import Employee
from entity.Task import Task
from exception.EmployeeNotFoundException import EmployeeNotFoundException

class ProjectRepositoryImpl(IProjectRepository):
    def create_employee(self, emp: Employee) -> bool:
        conn = DBConnUtil.get_connection()
        if not conn:
            return False
        try:
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO Employee (id, name, designation, gender, salary, project_id) VALUES (?, ?, ?, ?, ?, ?)",
                emp.id, emp.name, emp.designation, emp.gender, emp.salary, emp.project_id
            )
            conn.commit()
            return True
        except pyodbc.Error as e:
            print("Error creating employee:", e)
            return False
        finally:
            cur.close()
            conn.close()

    def create_project(self, pj: Project) -> bool:
        conn = DBConnUtil.get_connection()
        if not conn:
            return False
        try:
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO Project (id, project_name, description, start_date, status) VALUES (?, ?, ?, ?, ?)",
                pj.id, pj.project_name, pj.description, pj.start_date, pj.status
            )
            conn.commit()
            return True
        except pyodbc.Error as e:
            print("Error creating project:", e)
            return False
        finally:
            cur.close()
            conn.close()

    def create_task(self, task: Task) -> bool:
        conn = DBConnUtil.get_connection()
        if not conn:
            return False
        try:
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO Task (task_id, task_name, project_id) VALUES (?, ?, ?)",
                task.task_id, task.task_name, task.project_id
            )
            conn.commit()
            return True
        except pyodbc.Error as e:
            print("Error creating task:", e)
            return False
        finally:
            cur.close()
            conn.close()

    def assign_project_to_employee(self, project_id: int, employee_id: int) -> bool:
        conn = DBConnUtil.get_connection()
        if not conn:
            return False
        try:
            cur = conn.cursor()
            cur.execute(
                "UPDATE Employee SET project_id = ? WHERE id = ?",
                project_id, employee_id
            )
            conn.commit()
            return cur.rowcount > 0
        except pyodbc.Error as e:
            print("Error assigning project:", e)
            return False
        finally:
            cur.close()
            conn.close()

    def assign_task_in_project_to_employee(self, task_id: int, project_id: int, employee_id: int, status: str) -> bool:
        conn = DBConnUtil.get_connection()
        if not conn:
            return False
        try:
            cur = conn.cursor()
            cur.execute(
                "UPDATE Task SET project_id = ?, employee_id = ?, status = ? WHERE task_id = ?",
                project_id, employee_id, status, task_id
            )
            conn.commit()
            return cur.rowcount > 0
        except pyodbc.Error as e:
            print("Error assigning task:", e)
            return False
        finally:
            cur.close()
            conn.close()

    def delete_employee(self, employee_id: int) -> bool:
        conn = DBConnUtil.get_connection()
        if not conn:
            return False
        try:
            cur = conn.cursor()
            cur.execute("DELETE FROM Employee WHERE id = ?", employee_id)
            conn.commit()
            if cur.rowcount == 0:
                raise EmployeeNotFoundException(f"Employee {employee_id} not found")
            return True
        except pyodbc.Error as e:
            print("Error deleting employee:", e)
            return False
        finally:
            cur.close()
            conn.close()

    def delete_task(self, task_id: int) -> bool:
        conn = DBConnUtil.get_connection()
        if not conn:
            return False
        try:
            cur = conn.cursor()
            cur.execute("DELETE FROM Task WHERE task_id = ?", task_id)
            conn.commit()
            return cur.rowcount > 0
        except pyodbc.Error as e:
            print("Error deleting task:", e)
            return False
        finally:
            cur.close()
            conn.close()

    def get_all_tasks(self, emp_id: int) -> list:
        tasks = []
        conn = DBConnUtil.get_connection()
        if not conn:
            return tasks
        try:
            cur = conn.cursor()
            cur.execute(
                "SELECT task_id, task_name, project_id, status FROM Task WHERE employee_id = ?",
                emp_id
            )
            for row in cur:
                tasks.append(Task(row[0], row[1], row[2], emp_id, row[3]))
            return tasks
        except pyodbc.Error as e:
            print("Error listing tasks:", e)
            return tasks
        finally:
            cur.close()
            conn.close()

    def get_employee_by_id(self, emp_id: int) -> Employee:
        conn = DBConnUtil.get_connection()
        if not conn:
            return None
        try:
            cur = conn.cursor()
            cur.execute(
                "SELECT id, name, designation, gender, salary, project_id FROM Employee WHERE id = ?",
                emp_id
            )
            row = cur.fetchone()
            return Employee(*row) if row else None
        except pyodbc.Error as e:
            print("Error fetching employee:", e)
            return None
        finally:
            cur.close()
            conn.close()
