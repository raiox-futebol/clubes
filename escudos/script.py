import os
import re
from collections import defaultdict



# Diretório a ser percorrido
diretorio = "."

# Dicionário para agrupar os arquivos pelo trecho uf_nome
grupos = defaultdict(list)

# Percorre todos os arquivos do diretório
for arquivo in os.listdir(diretorio):
    caminho = os.path.join(diretorio, arquivo)

    # Ignora diretórios
    if not os.path.isfile(caminho):
        continue

    # Procura o padrão uf_nome_numero
    # O número é considerado a parte depois do último "_"

    match = re.match(r"[a-z]{2}_(.+)_", arquivo)

    if match:
        arq = match.group()[:-1]
        detalhe = caminho[(caminho.find(arq)+len(arq)):]     

        # Mantém o nome completo do arquivo, mas adiciona "escudos/"
        novo_nome = f"escudos/{arq}{detalhe}"

        grupos[arq].append(novo_nome)

# Imprime uma linha para cada grupo
for arq, arquivos in sorted(grupos.items()):
    print(",".join(sorted(arquivos)))