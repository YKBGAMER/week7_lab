class ManagementSystem:
    def __init__(self):
        self.employees = []

    def addEmp(self, name, age, id, department):
        if not all((name, age, id, department)):
            raise ValueError("Missing values for employee!!!!")
        emp = {
            "name": name,
            "age": age,
            "id": id,
            "department": department
        }
        self.employees.append(emp)
        print("Employee created successfully.")

    def getEmp(self, id):
        for emp in self.employees:
            if emp["id"] == id:
                print("Name:", emp["name"])
                print("Age:", emp["age"])
                print("ID:", emp["id"])
                print("Department:", emp["department"])
                return
        print("Employee not found.")

    def deleteEmp(self, id):
        for emp in self.employees:
            if emp["id"] == id:
                self.employees.remove(emp)
                print("Employee deleted successfully.")
                return
        print("Employee not found.")

ems = ManagementSystem()
ems.addEmp("John Doe", 30, 1001, "HR")
# ems.addEmp("Jane Smith", 25, 1002, "IT")

# ems.getEmp(1001)
# ems.getEmp(1003)  # Employee not found

# ems.deleteEmp(1002)
# ems.deleteEmp(1003)  # Employee not found
