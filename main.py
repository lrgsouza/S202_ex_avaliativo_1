from pprint import pprint
from classes import *
from db.database import Database
from helper.WriteAJson import writeAJson
from aula import AulaDB

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    ##### == EXERCICIO AVALIATIVO 1 == ####

    # criando conexão com Atlas
    db = Database("S202", 'Aulas')

    # iniciando uma instancia de auladb
    auladb = AulaDB(db)

    while True:
        # iniciando menu
        print(f'==== Bem vindo ao adminstrador de aulas do INATEL ======')

        opcao = int(input(f'Selecione sua opção:\n1 - Criar uma aula\n2 - Deletar uma aula\n3 - Modificar uma aula\n'
              f'4 - Listar todas as aulas\n0 - Sair\nOpção:'))

        # criando uma aula
        if opcao == 1:
            id_aula = int(input('Insira o ID da aula: '))
            assunto_aula = input('Insira o assunto da aula: ')
            nome_professor = input('Insira o nome do professor: ')
            esp_professor = input('Insira a especialidade do professor: ')
            professor = Professor(nome_professor,esp_professor)
            n_alunos = int(input('Quantos alunos tem a aula: '))
            alunos = []
            for i in range(0,n_alunos):
                nome_aluno = input('Nome do aluno: ')
                mat_aluno = input('Matricula do aluno: ')
                curso_aluno = input('Curso do aluno: ')
                periodo_aluno = input('Periodo do aluno: ')
                alunos.append(Aluno(nome_aluno,mat_aluno,curso_aluno,periodo_aluno))
            # criando Aula
            aula = Aula(assunto_aula,alunos,professor)
            auladb.addAula(id_aula, aula)
            aulas = auladb.getAulas()
            for aula in aulas:
                pprint(aula)
                print('\n----------------------------------------------------\n')

        if opcao == 2:
            #listando aulas
            print('\nAulas criadas:\n')
            aulas = auladb.getAulas()
            has_aula = False
            for aula in aulas:
                pprint(aula)
                print('\n----------------------------------------------------\n')
                has_aula = True
            if has_aula:
                aula_id = int(input('Insira o ID da aula que quer deletar: '))
                auladb.deleteAula(aula_id)
            else:
                print(f'Sem aulas criadas')

        if opcao == 3:
            # listando aulas
            print('\nAulas criadas:\n')
            aulas = auladb.getAulas()
            for aula in aulas:
                pprint(aula)
                print('\n----------------------------------------------------\n')
            aula_id = int(input('Insira o ID da aula que quer modificar: '))
            parametro = int(input('Qual parametro quer modificar?\n1 - assunto\n2 - professor\nOpção: '))
            if parametro == 1:
                valor = input(f'Qual o novo assunto: ')
                auladb.updateAula(aula_id, parametro, valor)
            if parametro == 2:
                nome = input(f'Insira o nome do professor: ')
                espec = input(f'Insira a especialidade do professor: ')
                prof = {'Nome':nome,
                        'Especialidade':espec}
                auladb.updateAula(aula_id, parametro, prof)


        if opcao == 4:
            print('\nAulas criadas:\n')
            aulas = auladb.getAulas()
            for aula in aulas:
                pprint(aula)
                print('\n----------------------------------------------------\n')

        if opcao == 0:
            break