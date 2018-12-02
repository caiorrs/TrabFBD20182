from pg import DB
from pg import DatabaseError
import sys
from pprint import pprint



def main():

    try:
        db = DB(dbname="imobiliaria", user="postgres", passwd="postgres", host="localhost", port=5432)
    except:
        print("ERRO AO ABRIR CONEXAO COM BD")
        exit(1)

    tabelas = db.get_tables()

    pprint(tabelas)

    tabela = "pessoa"

    q = db.query(f"select * from {tabela}")



    dicionario_insercao = {}
    dicionario_insercao['RG'] = "32345678901234"
    dicionario_insercao['nome'] = "alguem"
    dicionario_insercao['nome_pai'] = None  # equivale ao nulo
    dicionario_insercao['nome_mae'] = "mae de alguem"

    try:
        db.insert(tabela, dicionario_insercao)
    except DatabaseError as e:
        pprint("ERRO AO INSERIR REGISTRO")
        print(e)

    resultado = q.getresult()
    print("RESULTADO BANCO")
    print(resultado)


if __name__ == '__main__':
    main()
