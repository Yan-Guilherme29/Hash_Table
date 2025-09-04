class Pessoa:

    # Construtor da classe que recebe CPF, nome e idade
    def __init__(self, cpf, nome, idade ):
    # Armazena-os como atributos da Pessoa
        self.cpf = cpf
        self.nome = nome
        self.idade = idade

    # Metodo para exibir a representação em texto de uma Pessoa
    def __repr__(self): # representação em str do objeto.
        # Retorna uma str formatada com os dados da pessoa
        return f"[CPF: {self.cpf} Nome: {self.nome} Idade:{self.idade}"
