import mysql.connector
from mysql.connector import Error

#função para conectar ao banco de dados MYSQL
def conectar_mysql (host, usuario, senha):
    try:
        #tenta estabelecer conexao com o banco
        conexao = mysql.connector.connect(
            host = host,
            user = usuario,
            password = senha
        )

        if conexao.is_connected():
            print("Aqui é mengão, Segue o Bonde!")
            cursor = conexao.cursor()

            #Obtém a lista de databases disponíveis.
            cursor.execute("SHOW DATABASES")
            bancos = cursor.fetchall()

            print("\n Bancos de dados disponíveis:")
            for banco in bancos:
                print(f"- {banco[0]}")

                #Solicita a escolha de um banco de dados.
                banco_escolhido = input("Digite o nome do banco para listar as suas tabelas: ")
                cursor.execute(f"USE {banco_escolhido}")

                #Obtém a lista de tabelas dentro do banco escolhido.
                cursor.execute("SHOW TABLES")
                tabelas = cursor.fetchall()

                #para depuração, um retorno simples pra identificar o vacilão e mandar ele pro microondas.
                print(f" Tabelas retornadas pelo server MYSQL {banco_escolhido}: {tabelas} ")

                if tabelas:
                    print("\n Tabelas Disponiveis: ")
                    for tabela in tabelas:
                        print(f" - {tabela[0]}")
                else:
                    print("\n Nenhuma tabela encontrada neste banco de dados, deu ruim.")

            #fecha o cursor e a conexao
            cursor.close()
            conexao.close()
    except Error as e:
        #captura e exibe os erros de conexao
        print(f" Foi de Va2cu: {e} ")