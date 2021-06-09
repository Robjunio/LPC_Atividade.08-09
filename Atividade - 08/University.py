from Department import Department


class University:
    def __init__(self, name, department: Department):
        self.name = name
        self.departments = [department]

    def add_departament(self, departament):
        self.departments.append(departament)


