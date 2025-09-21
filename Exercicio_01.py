# Sensores: 0 = livre, 1 = obstáculo
frontal = int(input("Digite 0 se a frente está livre ou 1 se tem obstáculo: "))
direita = int(input("Digite 0 se a direita está livre ou 1 se tem obstáculo: "))
esquerda = int(input("Digite 0 se a esquerda está livre ou 1 se tem obstáculo: "))

if frontal == 0:
    print("O robô vai seguir em frente")
else:
    if direita == 0:
        print("O robô vai virar para a direita")
    else:
        if esquerda == 0:
            print("O robô vai virar para a esquerda")
        else:
            print("O robô vai parar (nenhum caminho livre)")
