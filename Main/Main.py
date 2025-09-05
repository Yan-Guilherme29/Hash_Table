from Models.Pessoa import Pessoa              # Importa a classe Pessoa
from Structures.HashTable import HashTable    # Importa a tabela hash
from Helpers.gerar_cpf import gerar_cpf
import time




def menu():
    tabela = HashTable(17)  # Cria uma tabela hash com tamanho 17

    # 🔹 Gera e insere 30 CPFs antes do menu
    print("\n--- CPFs gerados automaticamente ---")
    for i in range(30):
        cpf = gerar_cpf()  # gera CPF aleatório
        nome = f"Pessoa{i + 1}"  # cria nome fictício
        idade = 18 + (i % 40)  # idades variadas
        tabela.inserir(Pessoa(cpf, nome, idade))  # insere na hash
        print(f"{i + 1:02d}. CPF: {cpf} | Nome: {nome} | Idade: {idade}")
    print("--------------------------------------------------------------")




    while True:  # Loop infinito até o usuário escolher sair
        print("-------------------------------------------")
        print("--- Sistema de Cadastro com Tabela Hash ---\n")
        print("1 - Inserir Pessoa")
        print("2 - Buscar Pessoa")
        print("3 - Excluir Pessoa")
        print("4 - Imprimir Tabela")
        print("5 - Estatísticas")
        print("0 - Sair")
        print("-------------------------------------------")
        time.sleep(1)

        opcao = input("Escolha: ")  # Recebe a opção do usuário

        if opcao == "1":  # Inserção de pessoa
            cpf = input("Digite o CPF: ")     # Pede CPF
            nome = input("Digite o nome: ")   # Pede nome
            idade = int(input("Digite a idade: "))  # Pede idade
            tabela.inserir(Pessoa(cpf, nome, idade)) # Insere a pessoa na tabela


        elif opcao == "2":  # Buscar pessoa
            cpf = input("Digite o CPF para buscar: ")   # Pede CPF para busca
            pessoa = tabela.buscar(cpf)                 # Busca na tabela
            print(pessoa if pessoa else "\nNão encontrado") # Mostra o resultado

        elif opcao == "3":  # Excluir pessoa
            cpf = input("Digite o CPF para excluir: ")  # Pede CPF
            print("\nExcluído!" if tabela.excluir(cpf) else "\nNão encontrado") # Mostra se conseguiu excluir

        elif opcao == "4":  # Imprimir tabela completa
            print(" ")
            tabela.imprimir()

        elif opcao == "5":  # Mostrar estatísticas
            print(" ")
            tabela.estatisticas()

        elif opcao == "0":  # Sair do sistema
            print("...")
            time.sleep(1)
            print("Programa Finalizado ! Até a Próxima !")
            break

        else:  # Se digitar opção inválida
            print("Opção inválida!")

if __name__ == "__main__":
    menu()
