print("---------------------------------")
print("Bem vindo ao jogo de adivinhação!")
print("---------------------------------")

numero_secreto = 40

#Contador
rodada = 1
total_tentativas = 3

for rodada in range (1,total_tentativas + 1):
    print("** Tentativa {} de {} **".format(rodada,total_tentativas))
    chute = int(input("Digite um número de 1 á 50: "))
    if (chute < 1 or chute > 50):
        print("Você deve digitar um número entre 1 e 50: ")
        continue;
    if (chute == numero_secreto):
        print("Você acertou! O número secreto era {}.".format(numero_secreto))
        break;
    else:
        if(chute > numero_secreto):
            print("Você errou!! O número secreto era menor.")
        elif(chute < numero_secreto):
            print("Você errou!! O número secreto era maior.")

print("FIM DO JOGO")