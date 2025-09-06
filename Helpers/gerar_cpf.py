import random  # Biblioteca para gerar números aleatórios

def gerar_cpf():

    return ''.join(str(random.randint(0, 9)) for _ in range(11))
