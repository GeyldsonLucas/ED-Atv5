#Fazer um histograma sobre Tabela Hash, usando o M = 26 e a primeira letra do nome como função hashing

import matplotlib.pyplot as plt
from importa_arquivo import importar_alunos

#from importa_arquivo import importar_alunos
import matplotlib.pyplot as plt

def funcao_hash(nomes):
    tamanho_hash = 36
    tabela_hash = [0] * tamanho_hash
    colisoes_por_letra = {}

    for nome in nomes:
        primeira_letra = nome[0].lower()  # Convertendo para minúscula para garantir consistência
        indice_hash = ord(primeira_letra) % tamanho_hash

        tabela_hash[indice_hash] += 1
        colisoes_por_letra[primeira_letra] = colisoes_por_letra.get(primeira_letra, 0) + 1

    letra_mais_colisoes = max(colisoes_por_letra, key=colisoes_por_letra.get)
    letra_menos_colisoes = min(colisoes_por_letra, key=colisoes_por_letra.get)

    print("Número de colisões por letra:")
    for letra, colisoes in colisoes_por_letra.items():
        print(f"{letra}: {colisoes} colisões")

    print("\nLetra com mais colisões:", letra_mais_colisoes)
    print("Letra com menos colisões:", letra_menos_colisoes)

    # Criar histograma
    letras = list(colisoes_por_letra.keys())
    colisoes = list(colisoes_por_letra.values())

    plt.bar(letras, colisoes, color='blue')
    plt.xlabel('Letras')
    plt.ylabel('Número de Colisões')
    plt.title('Histograma de Colisões por Letra')
    plt.show()

# Exemplo de uso:
nomes = importar_alunos("alunosED_2023.txt")
funcao_hash(nomes)
