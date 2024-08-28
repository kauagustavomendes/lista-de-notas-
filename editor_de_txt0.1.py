import os

try:
    with open("notas.txt", "x", encoding="utf-8") as f:
            f.write("Lista de notas. \n\n")
except FileExistsError:
    pass # validar se o arquivo já existe

while True:
     a = str(input("Digite o nome do aluno:"))
     if a.lower() == "sair": # quebrar o loop
          break
     else:
          n1 = float(input("digite a primeira nota do aluno:"))
          n2 = float(input("digite a segunda nota do aluno:"))
          media = (n1+n2)/2
          situação = "Aprovado" if media >= 6.5 else "Reprovado"
          if situação.lower() == "aprovado":
               print("Aprovado")
          else:
               print("Reprovado")
          with open("notas.txt", "a", encoding="utf-8") as f:
           f.write(f"{a}: {n1:.1f}; {n2:.2f}; {situação}\n")  # exemplo "kauã: 7.0; 8.00; Aprovado" 
            
