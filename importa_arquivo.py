def importar_alunos(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            # Lê as linhas do arquivo
            linhas = arquivo.readlines()
            
            # Remove espaços em branco e quebras de linha, e divide o texto em nomes
            alunos = [linha.strip() for linha in linhas if linha.strip()]

        return alunos
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
        return None
    except Exception as e:
        print(f"Erro ao importar alunos: {str(e)}")
        return None
