import unittest
from unittest.mock import patch, MagicMock
from dao.ProjectRepositoryImpl import ProjectRepositoryImpl
from entity.Employee import Employee
from entity.Project import Project
from entity.Task import Task
from exception.EmployeeNotFoundException import EmployeeNotFoundException

class TestProjectRepository(unittest.TestCase):

    @patch('dao.ProjectRepositoryImpl.DBConnUtil.get_connection')
    def test_create_employee_success(self, mock_get_conn):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_conn.cursor.return_value = mock_cursor
        mock_get_conn.return_value = mock_conn

        repo = ProjectRepositoryImpl()
        emp = Employee(id=1, name="Alice", designation="Dev", gender="F", salary=50000.0, project_id=None)
        result = repo.create_employee(emp)

        self.assertTrue(result)
        mock_cursor.execute.assert_called_once_with(
            "INSERT INTO Employee (id, name, designation, gender, salary, project_id) VALUES (?, ?, ?, ?, ?, ?)",
            emp.id, emp.name, emp.designation, emp.gender, emp.salary, emp.project_id
        )
        mock_conn.commit.assert_called_once()
        mock_cursor.close.assert_called_once()

    @patch('dao.ProjectRepositoryImpl.DBConnUtil.get_connection')
    def test_create_project_success(self, mock_get_conn):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_conn.cursor.return_value = mock_cursor
        mock_get_conn.return_value = mock_conn

        repo = ProjectRepositoryImpl()
        pj = Project(id=10, project_name="ProjX", description="Desc", start_date="2025-06-01", status="dev")
        result = repo.create_project(pj)

        self.assertTrue(result)
        mock_cursor.execute.assert_called_once_with(
            "INSERT INTO Project (id, project_name, description, start_date, status) VALUES (?, ?, ?, ?, ?)",
            pj.id, pj.project_name, pj.description, pj.start_date, pj.status
        )
        mock_conn.commit.assert_called_once()
        mock_cursor.close.assert_called_once()

    @patch('dao.ProjectRepositoryImpl.DBConnUtil.get_connection')
    def test_create_task_success(self, mock_get_conn):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_conn.cursor.return_value = mock_cursor
        mock_get_conn.return_value = mock_conn

        repo = ProjectRepositoryImpl()
        t = Task(task_id=5, task_name="Task1", project_id=10, employee_id=None, status=None)
        result = repo.create_task(t)

        self.assertTrue(result)
        mock_cursor.execute.assert_called_once_with(
            "INSERT INTO Task (task_id, task_name, project_id) VALUES (?, ?, ?)",
            t.task_id, t.task_name, t.project_id
        )
        mock_conn.commit.assert_called_once()
        mock_cursor.close.assert_called_once()

    @patch('dao.ProjectRepositoryImpl.DBConnUtil.get_connection')
    def test_delete_employee_not_found_raises(self, mock_get_conn):
        from exception.EmployeeNotFoundException import EmployeeNotFoundException

        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_cursor.rowcount = 0  # simulate no existing record
        mock_conn.cursor.return_value = mock_cursor
        mock_get_conn.return_value = mock_conn

        repo = ProjectRepositoryImpl()
        with self.assertRaises(EmployeeNotFoundException):
            repo.delete_employee(999)

        mock_cursor.execute.assert_called_once_with("DELETE FROM Employee WHERE id = ?", 999)
        mock_conn.commit.assert_called_once()

    @patch('dao.ProjectRepositoryImpl.DBConnUtil.get_connection')
    def test_get_all_tasks_returns_list(self, mock_get_conn):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        # Simulate 2 rows
        mock_cursor.__iter__.return_value = [(1, "T1", 10, "Assigned"), (2, "T2", 10, "Started")]
        mock_conn.cursor.return_value = mock_cursor
        mock_get_conn.return_value = mock_conn

        repo = ProjectRepositoryImpl()
        tasks = repo.get_all_tasks(emp_id=100)

        self.assertEqual(len(tasks), 2)
        self.assertTrue(all(isinstance(t, Task) for t in tasks))
        mock_cursor.execute.assert_called_once_with(
            "SELECT task_id, task_name, project_id, status FROM Task WHERE employee_id = ?",
            100
        )
        mock_cursor.close.assert_called_once()

if __name__ == '__main__':
    unittest.main()
