import shutil
import os

# Caminho da pasta de origem
caminho_origem = r'[caminho da pasta a ser copiada]'

# Caminho de destino
caminho_destino = r'[caminho da pasta onde será feita a cópia]'

# Obter o nome da pasta base
pasta_base = os.path.basename(caminho_origem)

# Criar o caminho de destino completo
caminho_destino_completo = os.path.join(caminho_destino, pasta_base)

# Copiar o conteúdo da pasta de origem para o destino
shutil.copytree(caminho_origem, caminho_destino_completo, dirs_exist_ok=True)

print(f'A cópia de "{caminho_origem}" para "{caminho_destino_completo}" foi concluída com sucesso.')
