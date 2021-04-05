import Adivinhacao
import forca

print ("(1) Jogo de adivinhação  |  (2) Jogo da Forca")
escolhe_jogo = int(input("Escolha seu jogo: "))

if (escolhe_jogo == 1):
    Adivinhacao.jogar()
elif (escolhe_jogo == 2):
    forca.jogar()
else:
    print("Jogo inválido!! Digite 1 ou 2 para selecionar seu jogo!")

