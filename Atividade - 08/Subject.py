import Professor

class Subject:
    def __init__(self, name, code):
        self.name = name
        self.code = code
        self.professors = []

    def lancamento_notas(self,professors):
        for cont in professors:
            print(cont.name, "lançando notas de", self.name, "({})".format(self.code))