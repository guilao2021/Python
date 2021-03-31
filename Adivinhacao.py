print("---------------------------------")
print("Bem vindo ao jogo de adivinhação!")
print("---------------------------------")

numero_secreto = 40

chute = int(input("Digite um número: "))

if (numero_secreto == chute):
    print("Você acertou! O número secreto era",numero_secreto,".")

else:
    print("Você errou!! O número secreto era",numero_secreto,".")

print("FIM DO JOGO")