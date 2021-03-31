print("---------------------------------")
print("Bem vindo ao jogo de adivinhação!")
print("---------------------------------")

numero_secreto = 40

chute = int(input("Digite um número: "))

chute_acertou = chute == numero_secreto

chute_maior   = chute > numero_secreto

chute_menor   = chute < numero_secreto

if (chute_acertou):
    print("Você acertou! O número secreto era",numero_secreto,".")

else:
    if(chute_maior):
        print("Você errou!! O número secreto era menor.")
    elif(chute_menor):
        print("Você errou!! O número secreto era maior.")

print("FIM DO JOGO")