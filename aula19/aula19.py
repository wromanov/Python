"""
Laço de repetição - While

Controle de Fluxo
"break" para o fluxo de execução e sai do laço.
"continue" pula uma iteração do laço de repetição.
"pass" é uma palavra que deve ser usada sempre que o programa requisitar sintaticamente que se preencha uma lacuna para execução.

"""


x = 0 # Variável de controle

while True:
    if x == 3:
        x += 1
        continue # pula a iteração quando o valor for = 3.

    print(x)
    x += 1 #Incremento

    if x > 5:
        break #Condição de saida



print("Fim da contagem...")
