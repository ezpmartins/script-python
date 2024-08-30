import os
import shutil

def verificar_e_copiar_arquivos(pasta1, pasta2, extensao='.netsec'):
    # Criar a terceira pasta automaticamente
    pasta3 = os.path.join(os.path.dirname(pasta1), 'pasta03')
    if not os.path.exists(pasta3):
        os.makedirs(pasta3)

    # Obter lista de arquivos em ambas as pastas
    arquivos_pasta1 = [f for f in os.listdir(pasta1) if f.endswith(extensao)]
    arquivos_pasta2 = [f for f in os.listdir(pasta2) if f.endswith(extensao)]

    # Encontrar arquivos com o mesmo nome e extensão em ambas as pastas
    arquivos_comuns = set(arquivos_pasta1).intersection(arquivos_pasta2)

    # Copiar arquivos comuns para a terceira pasta sem alterar os nomes
    for arquivo in arquivos_comuns:
        caminho_arquivo_pasta1 = os.path.join(pasta1, arquivo)
        caminho_arquivo_pasta2 = os.path.join(pasta2, arquivo)

        shutil.copy2(caminho_arquivo_pasta1, os.path.join(pasta3, arquivo))
        shutil.copy2(caminho_arquivo_pasta2, os.path.join(pasta3, arquivo))

        print(f"Copiado {arquivo} de {pasta1} para {pasta3}")
        print(f"Copiado {arquivo} de {pasta2} para {pasta3}")

if __name__ == "__main__":
    # Solicitar os caminhos das pastas 01 e 02 ao usuário
    pasta1 = input("Cole o caminho da pasta 01: ").strip()
    pasta2 = input("Cole o caminho da pasta 02: ").strip()

    # Verificar e copiar arquivos
    verificar_e_copiar_arquivos(pasta1, pasta2)

    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
