from Models.Pessoa import Pessoa             # Importa a classe Pessoa
from Structures.HashTable import HashTable   # Importa a tabela hash
# from utils.helpers import gerar_cpf        # Importa a função para gerar CPFs aleatórios

def menu():
    tabela = HashTable(17)  # Cria uma tabela hash com tamanho 17

    while True:  # Loop infinito até o usuário escolher sair
        print("\n--- Sistema de Cadastro com Tabela Hash ---")
        print("1 - Inserir Pessoa")
        print("2 - Buscar Pessoa")
        print("3 - Excluir Pessoa")
        print("4 - Imprimir Tabela")
        print("5 - Estatísticas")
        print("0 - Sair")

        opcao = input("Escolha: ")  # Recebe a opção do usuário

        if opcao == "1":  # Inserção de pessoa
            cpf = input("Digite o CPF: ")     # Pede CPF
            nome = input("Digite o nome: ")   # Pede nome
            idade = int(input("Digite a idade: "))  # Pede idade
            tabela.inserir(Pessoa(cpf, nome, idade)) # Insere a pessoa na tabela

        elif opcao == "2":  # Buscar pessoa
            cpf = input("Digite o CPF para buscar: ")   # Pede CPF para busca
            pessoa = tabela.buscar(cpf)                 # Busca na tabela
            print("Encontrado:", pessoa if pessoa else "Não encontrado") # Mostra o resultado

        elif opcao == "3":  # Excluir pessoa
            cpf = input("Digite o CPF para excluir: ")  # Pede CPF
            print("Excluído!" if tabela.excluir(cpf) else "Não encontrado") # Mostra se conseguiu excluir

        elif opcao == "4":  # Imprimir tabela completa
            tabela.imprimir()

        elif opcao == "5":  # Mostrar estatísticas
            tabela.estatisticas()

        elif opcao == "0":  # Sair do sistema
            break

        else:  # Se digitar opção inválida
            print("Opção inválida!")

if __name__ == "__main__":
    menu()
