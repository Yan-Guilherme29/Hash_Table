import random  # Biblioteca para gerar números aleatórios

def gerar_cpf():
    """
    Gera um CPF aleatório no formato de string com 11 dígitos numéricos.
    Obs.: Não garante que seja um CPF válido oficial, apenas segue o padrão de 11 dígitos.
    """
    return ''.join(str(random.randint(0, 9)) for _ in range(11))
