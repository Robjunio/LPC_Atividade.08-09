import Professor

class Subject:
    def __init__(self, name, code):
        self.name = name
        self.code = code

    def lancamento_notas(self,professors):
        for cont in professors:
            print(cont.name, "lançando notas de", self.name, "({})".format(self.code))


s = Subject("laboratorio", 12345)
p = Professor.Professor("jucimano")
s.lancamento_notas([p])