import os

nome_arquivo = input("Digite o nome do arquivo que gostaria de editar:")

def ler_arquivo(nome_arquivo):
    try:
        with open(f"{nome_arquivo}", "r", encoding="utf-8") as ler:
            conteudo = ler.read()
            print(conteudo)
    except FileNotFoundError:
        print(f"O arquivo '{nome_arquivo}' não foi encontrado.")

def deletar_aluno(nome_arquivo):
    try:
        with open(f"{nome_arquivo}", "r", encoding="utf-8") as ler:
            linhas = ler.readlines()
    except FileNotFoundError:
        print(f"O arquivo '{nome_arquivo}' não foi encontrado.")

    nome_aluno = input("Digite o nome do aluno que deseja excluir:")
    linhas_modificadas = [linha for linha in linhas if nome_aluno not in linha]

    if len(linhas_modificadas) == len(linhas):
        print(f"O aluno {nome_aluno} não foi encontrado.")
    else:
        with open(f"{nome_arquivo}", "w", encoding="utf-8") as f:
            f.writelines(linhas_modificadas)
            print(f"O aluno {nome_aluno} foi excluido com sucesso do arquivo.")

def escrever_arquivo(nome_arquivo):
    while True:
        a = input("Digite o nome do aluno:")
        if a.lower() == "sair":
            break
        else:
            n1 = float(input("Digite a primeira nota:"))
            n2 = float(input("Digite a segunda nota:"))
            n3 = float(input("Digite a terceira nota:"))
            media = (n1 + n2 + n3) / 3
            situacao = "Aprovado" if media >= 6.5 else "Reprovado"
            with open(f"{nome_arquivo}", "a", encoding="utf-8") as write:
                write.write(f"{a}: {n1:.1f}; {n2:.1f}; {n3:.1f}; {situacao}\n")
            print(f"Aluno {a} adicionado com sucesso. Média: {media}, Situação: {situacao}")

def menu_principal(nome_arquivo):
    print("\x1b[2J\x1b[1;1H")  # Limpa o terminal
    while True:
        if nome_arquivo.lower() == "sair":
            break
        acao = input("O que gostaria de fazer: \n[Read]\n[Write]\n[Delete]\n>. ")
        if acao.lower() == "sair":
            break
        elif acao.lower() == "read":
            ler_arquivo(nome_arquivo)
        elif acao.lower() == "write":
            escrever_arquivo(nome_arquivo)
        elif acao.lower() == "delete":
            deletar_aluno(nome_arquivo)
        else:
            print("Comando inválido!!!\n")
            
if __name__ == "__main__":
    menu_principal(nome_arquivo)
