class Professor:
    professors = [A, B, C, D, E]
    def __init__(self, name, subject):
        self.name = name
        self.__class__.subject.append(self)
    def __str__(self):
        return self.name
        
'''O próximo método importante é o pop(),
que remove o último item da lista e o
retorna como resultado da operação.
Caso seja necessário remover um índice específico,
basta informá-lo como argumento'''
