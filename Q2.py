import matplotlib.pyplot as plt
from importa_arquivo import importar_alunos

# Função de hash
def hash_function(name, M):
    return sum(ord(char) for char in name) % M

# Criar a tabela hash
M = 26
hash_table = {i: 0 for i in range(M)}

# Nomes dos alunos
alunos = importar_alunos("alunosED_2023.txt")

# Preencher a tabela hash
for aluno in alunos:
    index = hash_function(aluno, M)
    hash_table[index] += 1

# Imprimir o histograma
print("Letra  Colisões")
for letra, colisoes in hash_table.items():
    print(f"  {chr(letra + ord('A'))}      {colisoes}")

# Encontrar a letra com mais e menos colisões
mais_colisoes_letra = max(hash_table, key=hash_table.get)
menos_colisoes_letra = min(hash_table, key=hash_table.get)

# Imprimir resultados
print(f"\nLetra com mais colisões: {chr(mais_colisoes_letra + ord('A'))}")
print(f"Letra com menos colisões: {chr(menos_colisoes_letra + ord('A'))}")
print(f"Quantidade de colisões para a letra com mais colisões: {hash_table[mais_colisoes_letra]}")
print(f"Quantidade de colisões para a letra com menos colisões: {hash_table[menos_colisoes_letra]}")

# Gerar o histograma
letras = [chr(letra + ord('A')) for letra in hash_table]
colisoes = list(hash_table.values())

plt.bar(letras, colisoes)
plt.xlabel('Letra')
plt.ylabel('Colisões')
plt.title('Histograma de Colisões')
plt.show()
