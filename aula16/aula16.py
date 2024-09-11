"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
menos escreve "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva "Seu nome é normal";
Mario que 6 escreva "Seu nome é muito grande".
"""

nome = input("Escreva seu nome: ").strip() #remover os caracteres em branco do inicio e fim do texto
nome_sem_espaço = nome.replace(" ", "") #substitui o espeço entre as letras
contar_caracter = len(nome_sem_espaço)

if contar_caracter <= 4:
    print(f"O nome {nome} possui {contar_caracter} caracteres.")
    print("Seu nome é curto.")
elif contar_caracter <= 6:
    print(f"O nome {nome} possui {contar_caracter} caracteres.")
    print("Seu nome é normal.")
elif contar_caracter >= 7:
    print(f"O nome {nome} possui {contar_caracter} caracteres.")
    print("Seu nome é muito grande.")


