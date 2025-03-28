# Número fixo a ser adivinhado
numero_secreto = 7

# Número de tentativas permitidas
tentativas = 0
limite_tentativas = 3

# Loop de tentativas
while tentativas < limite_tentativas:
    chute = int(input("Adivinhe o número (entre 1 e 10): "))
    tentativas += 1
    
    if chute == numero_secreto:
        print("Parabéns! Você acertou o número!")
        break
    else:
        if tentativas < limite_tentativas:
            print("Tente novamente! Você ainda tem", limite_tentativas - tentativas, "tentativa(s).")
        else:
            print("Suas tentativas acabaram. O número correto era", numero_secreto)