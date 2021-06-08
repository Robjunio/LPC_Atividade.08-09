from Professor import Professor


class Department:
    def __init__(self, professor: Professor, name):
        self.professors = [professor]
        self.name = name
