def jogar():
    print("---------------------------------")
    print("***Bem vindo ao jogo de Forca!***")
    print("---------------------------------")

    # variaveis
    enforcou = False
    acertou = False
    tentativas = 1
    total_tentativas = 5

    palavra_secreta = ["banana","melancia","onomatopeia"]

    # Selecionar dificuldade
    print("1 - Fácil | 2 - Médio | 3 - Difícil ")
    dificuldade = int(input("Digite um número de 1 a 3 para selecionar o nível de dificuldade: "))

    if (dificuldade == 1):
        palavra_secreta = palavra_secreta[0].upper()
        total_tentativas = 5
    elif (dificuldade == 2):
        palavra_secreta = palavra_secreta[1].upper()
        total_tentativas = 10
    elif (dificuldade == 3):
        palavra_secreta = palavra_secreta[2].upper()
        total_tentativas = 15
    else:
        enforcou = True

    print("Você tem {} tentativas...".format(total_tentativas))
    letras_acertadas = ['_' for letra in palavra_secreta]
    print(letras_acertadas)

    # main
    while (not enforcou and not acertou):
        chute = input("Qual a letra? ")
        chute = chute.strip().upper()

        if (chute in palavra_secreta):
            posicao = 0
            for letra in palavra_secreta:
                if (chute == letra):
                    letras_acertadas[posicao] = letra
                posicao += 1
            print("Acertou a letra! Você tem mais {} tentativa(s)...".format(total_tentativas - tentativas))
            tentativas += 1

        elif(total_tentativas >= 0):
            print("Você errou e tem mais {} tentativa(s)...".format(total_tentativas - tentativas))
            tentativas += 1
        else:
            tentativas += 1
        enforcou = tentativas > total_tentativas
        acertou = '_' not in letras_acertadas
        print(letras_acertadas)

    if (acertou):
        print("Parabéns!! Você ganhou!!!")
    else:
        print("Você perdeu!!!A palavra secreta era {} !".format(palavra_secreta))

    print("**FIM DO JOGO**")

if (__name__ == "__main__"):
   jogar()

