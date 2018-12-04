from pg import DB
from pg import DatabaseError
from pprint import pprint

def main():

    try:
        db = DB(dbname="imob", user="postgres", passwd="postgres", host="localhost", port=5432)
    except:
        print("ERRO AO ABRIR CONEXAO COM BD")
        exit(1)

    consulta1 = "select nome, sum(preco_aluguel * porcentagem_proprietario / 100) \
from contrato_aluguel natural join apartamento natural join proprietario \
group by nome;"

    consulta2 = "select nome_cidade, nome_bairro, preco_m2 \
from bairro \
natural join cidade \
where id_bairro in (select distinct id_bairro \
from casa \
natural join bairro \
where disponivel = true)"

    consulta3 = "select id_imovel, rua, nome_bairro, nome_cidade, proprietario.nome \
from 	imovel \
natural join proprietario \
natural join cidade \
natural join bairro \
where proprietario in (select distinct proprietario \
						from proprietario natural join imovel natural join contrato \
						where id_fiador is null);"

    consulta4 = "select id_imovel, rua, nome_bairro, nome_cidade, proprietario.nome \
from 	imovel \
natural join proprietario \
natural join cidade \
natural join bairro as bairro_top \
where not exists(select * \
					from bairro \
					natural join cidade \
					natural join imovel \
					where id_bairro = bairro_top.id_bairro and area < 80)"

    consulta5 = "select id_imovel, rua, nome_bairro, nome_cidade, area \
from 	apartamento \
natural join cidade \
natural join bairro \
where nome_bairro = 'São Gabriel' and banheiros > 1 and andar > 2"

    consulta6 = "select nome_cidade, id_imovel, rua, nome_bairro \
from 	imovel as imovel_top \
natural join cidade \
natural join bairro \
where preco_aluguel < (select avg(preco_aluguel) \
						from imovel \
						where id_cidade = imovel_top.id_cidade) \
order by nome_cidade"


    print("CONSULTA 1\n\n")
    print("-- Soma do valor devido à cada proprietário pelo alguel mensal\n\
	--Nome Proprietário, Soma do valor devido")
    q = db.query(consulta1)
    resultado = q.getresult()
    pprint(resultado)
    print("\n\n")
    str(input("Aperte enter para continuar"))
    print("\n\n")

    print("CONSULTA 2\n\n")
    print("-- Bairros que possuem casas disponíveis para venda\n\
	--Cidade, Nome dos bairros, preço do m²")
    q = db.query(consulta2)
    resultado = q.getresult()
    pprint(resultado)
    print("\n\n")
    str(input("Aperte enter para continuar"))
    print("\n\n")

    print("CONSULTA 3\n\n")
    print("-- Todos os imóveis de proprietários que já alugaram sem exigir fiador\n\
	--id_imovel, rua, bairro, cidade, nome proprietário")
    q = db.query(consulta3)
    resultado = q.getresult()
    pprint(resultado)
    print("\n\n")
    str(input("Aperte enter para continuar"))
    print("\n\n")

    print("CONSULTA 4\n\n")
    print("--todos os apartamentos de bairros que tenham somente imóveis entre 80 e 100 m²")
    q = db.query(consulta4)
    resultado = q.getresult()
    pprint(resultado)
    print("\n\n")
    str(input("Aperte enter para continuar"))
    print("\n\n")

    print("CONSULTA 5\n\n")
    print("--todos apartamentos de um determinado bairro, que não sejam no térreo e tenham mais que 2 banheiros")
    q = db.query(consulta5)
    resultado = q.getresult()
    pprint(resultado)
    print("\n\n")
    str(input("Aperte enter para continuar"))
    print("\n\n")

    print("CONSULTA 6\n\n")
    print("--todos imóveis de um determinado bairro com preço de aluguel menor que a média da cidade")
    q = db.query(consulta6)
    resultado = q.getresult()
    pprint(resultado)
    print("\n\n")
    str(input("Aperte enter para continuar"))
    print("\n\n")

    exit(0)


if __name__ == '__main__':
    main()
