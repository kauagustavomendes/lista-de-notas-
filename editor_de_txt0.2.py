import os
print("\x1b[2J\x1b[1;1H")

while True:
    nome_arquivo = input("Qual arquivo.txt você gostaria de editar?")
    if nome_arquivo.lower() == "sair":
        break

    while True:
        control = input(f"Qual sua ação para {nome_arquivo}: \n[read]\n[write]\n[sair]\n[delete]\n>. ")
        def error_control():
            return    ["sair", "delete", "read", "write"]

        if control.lower() == "sair":
            break

        elif control.lower() not in error_control():
            print("Comando invalido!!!\n")

        elif control.lower() == "write":

            try:
                with open(f"{nome_arquivo}.txt", "x", encoding="utf-8") as f:
                        f.write("Lista de notas. \n\n")
            except FileExistsError:
                pass

            while True:
                a = str(input("Digite o nome do aluno: "))
                if a.lower() == "sair":
                    break
                else:
                    n1 = float(input("digite a primeira nota do aluno: "))
                    n2 = float(input("digite a segunda nota do aluno:" ))
                    media = (n1+n2)/2
                    situação = "Aprovado" if media >= 6.5 else "Reprovado"
                    if situação.lower() == "aprovado":
                        print("Aprovado")
                    else:
                        print("Reprovado")
                    with open(f"{nome_arquivo}.txt", "a", encoding="utf-8") as f:
                        f.write(f"{a}: {n1:.1f}; {n2:.2f}; {situação}\n")

        elif control.lower() == "read":
            try:
                with open(f"{nome_arquivo}.txt", "r", encoding="utf-8") as ler:
                    conteudo = ler.read()  # Lê todo o conteúdo do arquivo
                    print(conteudo)

            except FileNotFoundError:
                print(f"O arquivo '{nome_arquivo}' não foi encontrado.")

        elif control.lower() == "delete":
            try:
                with open(f"{nome_arquivo}.txt", "r") as ler:
                    linhas = ler.read()
            except FileNotFoundError:
                continue
            nome_aluno = input("Digite o nome do aluno que deseja excluir: ")
            linhas_modificadas = [linha for linha in linhas if nome_aluno not in linha]

            if len(linhas_modificadas) == len(linhas): # checa se o aluno está na lista
                print(f"Aluno {nome_aluno} não encontrado no arquivo.")
            else:
                with open(f"{nome_arquivo}.txt", "w", encoding="utf-8") as f:
                    f.writelines(linhas_modificadas) #sob escreve o arquivo
                print(f"Aluno {nome_aluno} deletado com sucesso do arquivo.")

        else:
            break

