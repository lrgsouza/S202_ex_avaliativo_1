from classes import *

class AulaDB():

    def __init__(self, db):
        self.db = db

    def getAulas(self):
        return self.db.read()

    def getOneAula(self, id):
        return self.db.readOne(id)

    def updateAula(self, id, parametro, valor):
        # atualizando
        self.db.update(id, parametro, valor)
        pass

    def addAula(self, id, aula: Aula):
        assunto = aula.assunto
        professor = aula.professor
        lista_presenca = aula.lista_presenca
        self.db.create(id, assunto, professor, lista_presenca)

    def deleteAula(self, id):
        self.db.delete(id)
        pass