# Definição da classe HashTable
class HashTable:
    # Construtor da tabela hash
    def __init__(self, tamanho=17):
        self.tamanho = tamanho                    # Define o tamanho da tabela (quantidade de índices disponíveis)
        self.tabela = [[] for _ in range(tamanho)] # Cria uma lista de listas (encadeamento para tratar colisões)
        self.colisoes = 0                         # Contador de colisões

    # Função hash para calcular o índice da tabela a partir do CPF
    def hash_func(self, cpf):
        return int(cpf) % self.tamanho  # Converte o CPF em número e aplica o módulo pelo tamanho da tabela

    # Inserção de uma nova pessoa na tabela
    def inserir(self, pessoa):
        indice = self.hash_func(pessoa.cpf)  # Calcula o índice da tabela usando o CPF da pessoa
        for p in self.tabela[indice]:        # Percorre as pessoas que já estão no mesmo índice
            if p.cpf == pessoa.cpf:          # Se já existir esse CPF, não insere de novo
                print("⚠️ CPF já cadastrado!")
                return
        if self.tabela[indice]:              # Se a posição já tiver alguém, ocorreu uma colisão
            self.colisoes += 1
        self.tabela[indice].append(pessoa)   # Adiciona a pessoa na lista do índice correspondente

    # Busca uma pessoa na tabela pelo CPF
    def buscar(self, cpf):
        indice = self.hash_func(cpf)          # Calcula o índice a partir do CPF
        for p in self.tabela[indice]:         # Percorre as pessoas armazenadas nesse índice
            if p.cpf == cpf:                  # Se o CPF for igual ao procurado, retorna a pessoa
                return p
        return None                           # Caso não encontre, retorna None

    # Remove uma pessoa da tabela pelo CPF
    def excluir(self, cpf):
        indice = self.hash_func(cpf)          # Calcula o índice da tabela
        for i, p in enumerate(self.tabela[indice]): # Percorre as pessoas armazenadas nesse índice
            if p.cpf == cpf:                  # Se encontrar o CPF
                del self.tabela[indice][i]    # Remove a pessoa da lista
                return True                   # Retorna True indicando sucesso
        return False                          # Retorna False se não encontrar

    # Imprime todo o conteúdo da tabela
    def imprimir(self):
        for i, lista in enumerate(self.tabela):   # Percorre cada índice da tabela
            print(f"Índice {i}: {lista}")         # Mostra o índice e a lista de pessoas dentro dele

    # Exibe estatísticas sobre a tabela
    def estatisticas(self):
        print(f"🔹 Colisões: {self.colisoes}")                          # Mostra o número de colisões
        ocupacao = sum(len(l) for l in self.tabela)                    # Conta quantas pessoas foram inseridas no total
        print(f"🔹 Registros armazenados: {ocupacao}")                 # Mostra o total de registros
        print(f"🔹 Eficiência: {(ocupacao / self.tamanho):.2f} itens por slot") # Mostra a média de ocupação por índice
