from importa_arquivo import importar_alunos

# Função de hash
def hash_function(name, M):
    return sum(ord(char) for char in name) % M

# Nomes dos alunos
alunos = importar_alunos("alunosED_2023.txt")

# Testar diferentes valores de M
for M in [7, 13, 19, 31]:
    print("Para M = " + str(M))
    # Criar a tabela hash
    hash_table = {i: 0 for i in range(M)}

    # Preencher a tabela hash
    for aluno in alunos:
        index = hash_function(aluno, M)
        hash_table[index] += 1

    # Calcular a média de colisões
    media_colisoes = sum(hash_table.values()) / M

    # Imprimir resultados
    print(f"\nResultado para M = {M}:")
    print("Letra  Colisões")
    for letra, colisoes in hash_table.items():
        print(f"  {chr(letra + ord('A'))}      {colisoes}")

    print(f"Média de colisões: {media_colisoes}")
