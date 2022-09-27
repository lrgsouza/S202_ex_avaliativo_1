import pymongo


class Database:
    def __init__(self, database, collection, dataset=None):
        connectionString = "mongodb+srv://root:root@cluster0.rib3fl7.mongodb.net/test"
        self.clusterConnection = pymongo.MongoClient(
            connectionString,
            # CASO OCORRA O ERRO [SSL_INVALID_CERTIFICATE]
            tlsAllowInvalidCertificates=True
        )
        self.db = self.clusterConnection[database]
        self.collection = self.db[collection]
        if dataset:
            self.dataset = dataset

    def resetDatabase(self):
        self.db.drop_collection(self.collection)
        self.collection.insert_many(self.dataset)

    def create(self, id, assunto, professor, lista_presenca):
        lista_list = []
        for aluno in lista_presenca:
            dict_aluno = {'Nome':aluno.nome,
                          'Matricula':aluno.matricula,
                          'Curso':aluno.curso,
                          'Periodo':aluno.periodo}
            lista_list.append(dict_aluno)
        # arrumando professor
        dict_professor = {'Nome': professor.nome,
                      'Especialidade': professor.especialidade}

        return self.collection.insert_one(
            {"_id": id,
             "assunto": assunto,
             "professor": dict_professor,
             "lista_presenca": lista_list}
        )

    def read(self):
        return self.collection.find({})

    def readOne(self,id):
        return self.collection.find({"_id": id})

    def update(self, id, parametro, valor):
        if parametro == 1:
            return self.collection.update_one(
                {"_id": id},
                {
                    "$set": {"assunto": valor},
                    "$currentDate": {"lastModified": True}
                }
            )
        if parametro == 2:
            return self.collection.update_one(
                {"_id": id},
                {
                    "$set": {"professor":
                                 {"Nome":valor['Nome'],
                                  "Especialidade":valor['Especialidade']}
                             },
                    "$currentDate": {"lastModified": True}
                }
            )


    def delete(self, id):
        return self.collection.delete_one({"_id": id})
