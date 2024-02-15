import unittest
from program import ManagementSystem

class TestManagementSystem(unittest.TestCase):
    def setUp(self):
        self.ems = ManagementSystem()
        self.ems.addEmp("John Doe", 30, 1001, "HR")
        self.ems.addEmp("Jane Smith", 25, 1002, "IT")


    def test_get_existing_employee(self):
        self.ems.getEmp(1001)

    def test_get_non_existing_employee(self):
        self.ems.getEmp(1003)

    def test_delete_existing_employee(self):
        self.ems.deleteEmp(1002)

    def test_delete_non_existing_employee(self):
        self.ems.deleteEmp(1003)

if __name__ == '__main__':
    unittest.main()
