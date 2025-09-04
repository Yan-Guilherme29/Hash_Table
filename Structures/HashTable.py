class HashTable:

    # Construtor da Classe
    def __init__(self, tamanho=17): # __init__ - inicializa os atributos do objeto
        self.tamanho = tamanho # Define o tamanho da Tabela
        self.tabela = [[] for _ in range(tamanho)] # Cria uma lista de listas (encadeamento para tratar colisões)
        self.colisoes = 0 # Contador de colisões

# ---------------------------------------------------------------------------------------------------------------------

    # Função hash para calcular o índice da tabela a partir do CPF

    def hash_funcao(self, cpf):
     return int(cpf) % self.tamanho  # Converte o CPF em número e aplica o módulo pelo tamanho da tabela

# ---------------------------------------------------------------------------------------------------------------------

    # Inserção de uma nova pessoa na tabela

    def insercao (self, pessoa):
        indice = self.hash_funcao(pessoa.cpf) # Calcula o índice da tabela usando o CPF da pessoa
        for p in self.tabela[indice]: # Percorre as pessoas que já estão no mesmo índice
            if p.cpf == pessoa.cpf: # Se já existir esse CPF, não insere de novo
                print("⚠️ CPF já cadastrado!")
                return

        if self.tabela[indice]:
            self.colisoes += 1  # Se a posição já tiver alguém, ocorreu uma colisão
        self.tabela[indice].append(pessoa)  # Adiciona a pessoa na lista do índice correspondente
# ---------------------------------------------------------------------------------------------------------------------

    # Busca uma pessoa na tabela pelo CPF

    def buscar(self,cpf):
        indice = self.hash_funcao(cpf) # Calcula em qual posição da tabela o CPF deveria estar
        for p in self.tabela[indice]: # Percorre todas as pessoas na lista desse índice
            if p.cpf == cpf: # Se tiver alguém com o CPF igual
                return p # Retorna o objeto Pessoa encontrado
        return None # Se não encontrar ninguém, retorna None

# ---------------------------------------------------------------------------------------------------------------------

    # Remove uma pessoa da tabela pelo CPF

    def excluir(self,cpf):
        indice = self.hash_func(cpf)  # Calcula em qual índice o CPF deveria estar
        for i, p in enumerate(self.tabela[indice]): # Percorre a lista com Índice + Objeto
            if p.cpf == cpf: # Se encontrar o CPF
                del self.tabela[indice][i] # Remove a Pessoa da Lista
                print("✅ Registro Excluído!")
                return
        print("⚠️ CPF não encontrado!") # Se não encontrar, mostra o Aviso

# ---------------------------------------------------------------------------------------------------------------------

    # Imprime todo o conteudo da tabela

    def imprimir(self):
        for i, lista in enumerate(self.tabela): # Para cada índice na tabela
            print(f"Índice {i} :  {lista}") # Imprimir na tela Índice e Lista

# ---------------------------------------------------------------------------------------------------------------------

    # Exibe estatísticas sobre a tabela

    def estatisticas(self):
        print(f"🔹 Colisões: {self.colisoes}")  # Mostra o número de colisões
        ocupacao = sum(len(l) for l in self.tabela)  # Conta quantas pessoas foram inseridas no total
        print(f"🔹 Registros armazenados: {ocupacao}")  # Mostra o total de registros
        print(f"🔹 Eficiência: {(ocupacao / self.tamanho):.2f} itens por slot")  # Mostra a média de ocupação por índice