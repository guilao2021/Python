print("---------------------------------")
print("Bem vindo ao jogo de adivinhação!")
print("---------------------------------")

numero_secreto = 40

#Contador
rodada = 1
total_tentativas = 3

for rodada in range (rodada,total_tentativas + 1):
    print("** Tentativa {} de {} **".format(rodada,total_tentativas))
    chute = int(input("Digite um número: "))
    if (chute == numero_secreto):
        print("Você acertou! O número secreto era {}.".format(numero_secreto))
    else:
        if(chute > numero_secreto):
            print("Você errou!! O número secreto era menor.")
        elif(chute < numero_secreto):
            print("Você errou!! O número secreto era maior.")

print("FIM DO JOGO")