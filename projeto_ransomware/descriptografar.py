from cryptography.fernet import Fernet
import os

def carregar_chave():
    return open("chave.key", "rb").read()

def descriptografar_arquivo(arquivo, chave):
    f = Fernet(chave)
    with open(arquivo, "rb") as file:
        dados_encriptados = file.read()
    dados_desencriptados = f.decrypt(dados_encriptados)
    with open(arquivo, "wb") as file:
        file.write(dados_desencriptados)

def encontrar_arquivos(diretorio):
    lista = []
    for nome in os.listdir(diretorio):
        caminho = os.path.join(diretorio, nome)
        if os.path.isfile(caminho) and nome != ".py" and not nome.endswith(".key"):
            lista.append(caminho)
    return lista

def main():
    chave = carregar_chave()
    arquivos = encontrar_arquivos("test_files")
    for arquivo in arquivos:
        descriptografar_arquivo(arquivo, chave)
    print("Descriptografia concluída.")

if __name__ == "__main__":
    main()    