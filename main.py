from conexao_mysql import conectar_mysql
import getpass
import re

# Ponto de entrada do programa
if __name__ == "__main__":
    host = input("Manda ai o IP do servidor: ")
    usuario = input("Manda teu nome de usuário: ")
    senha = getpass.getpass("Digite sua senha (Mais oculta que o mundial do Palmeiras): ")

    # Chama a função para testar a conexão
    conectar_mysql(host, usuario, senha)
