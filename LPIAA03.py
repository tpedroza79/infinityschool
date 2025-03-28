# Número fixo a ser adivinhado
numero_secreto = 7
tentativas = 0
limite_tentativas = 3

while tentativas < limite_tentativas:
    chute = int(input("Adivinhe o número (entre 1 e 10): "))
    tentativas += 1

    if chute == numero_secreto:
        print("Parabéns! Você acertou o número! Continue assim!")
        break
else:
    # Este else é executado apenas se o loop terminar sem 'break'
    print("Que pena! Suas 3 tentativas acabaram. Tente novamente mais tarde!")