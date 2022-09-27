
class Pessoa(object):
    def __init__(self,nome):
        self.nome = nome

class Aluno(Pessoa):

    def __init__(self,nome,matricula,curso,periodo):
        super().__init__(nome)
        self.matricula = matricula
        self.curso = curso
        self.periodo = periodo

    def toString(self):
        return self.nome, self.matricula, self.curso, self.periodo

class Professor(Pessoa):

    def __init__(self,nome,especialidade):
        super().__init__(nome)
        self.especialidade = especialidade

    def toString(self):
        return self.nome, self.especialidade

class Aula(object):

    def __init__(self,assunto,lista_presenca,professor):
        self.assunto = assunto
        self.lista_presenca = lista_presenca
        self.professor = professor

    def getListaPresenca(self):
        print(f'Aula de {self.assunto}')
        nome, especialidade = self.professor.toString()
        print(f'    Professor: {nome}')
        print(f'    Especialidade: {especialidade}\n')
        for aluno in self.lista_presenca:
            nome, matricula, curso, periodo = aluno.toString()
            print(f'        nome: {nome}')
            print(f'        matricula: {matricula}')
            print(f'        nocursome: {curso}')
            print(f'        periodo: {periodo}\n')