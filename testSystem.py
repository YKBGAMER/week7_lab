import unittest
from program import ManagementSystem

class TestManagementSystem(unittest.TestCase):
    def setUp(self):
        self.ems = ManagementSystem()
        self.ems.addEmp("John Doe", 30, 1001, "HR")
        self.ems.addEmp("Jane Smith", 25, 1002, "IT")

    def test_get_existing_employee(self):
        # Test getting an existing employee
        employee = self.ems.getEmp(1001)
        self.assertIsNotNone(employee)  # Check that the employee information is retrieved
        self.assertEqual(employee["name"], "John Doe")  # Check name
        self.assertEqual(employee["age"], 30)  # Check age
        self.assertEqual(employee["id"], 1001)  # Check ID
        self.assertEqual(employee["department"], "HR")  # Check department

    def test_get_non_existing_employee(self):
        # Test getting a non-existing employee
        employee = self.ems.getEmp(1003)
        self.assertIsNone(employee)  # Check that no employee information is retrieved

    def test_delete_existing_employee(self):
        # Test deleting an existing employee
        initial_count = len(self.ems.employees)
        self.ems.deleteEmp(1002)
        self.assertEqual(len(self.ems.employees), initial_count - 1)  # Check that the employee is deleted

    def test_delete_non_existing_employee(self):
        # Test deleting a non-existing employee
        initial_count = len(self.ems.employees)
        self.ems.deleteEmp(1003)
        self.assertEqual(len(self.ems.employees), initial_count)  # Check that no employee is deleted

if __name__ == '__main__':
    unittest.main()
