//Perguntas sobre cada banda:
import random
import os
import unicodedata

Questões = {
    "Bandas Musicais": [

    ]
}

def limpar_tela():

    # Limpa a tela do terminal dependendo do sistema operacional.
    # "cls" funciona no Windows e "clear" no Linux/Mac.
    os.system("cls" if os.name == "nt" else "clear")

def escolher_banda_musical():

    # Exibe o menu de bandas.
    print("=" * 43)
    print("┴┬┴┤(･_├┬┴┬┴ ESCOLHA UMA BANDA PARA COMEÇAR:")
    print("=" * 43)

    print("1 - Imagine Dragons")
    print("2 - Metálica")
    print("3 - Gorillaz")
    print("4 - Blur")
    print("5 - Linkin Park")
    print("6 - Nirvana")
    print("7 - Led Zeppelin")
    print("8 - AC/DC")
    print("9 - Slipknot")
    print("10 - Guns N' roses")
    print()

    # Loop infinito até o jogador digitar uma opção válida.
    while True:

        escolha = input("Digite a dificuldade: ")

        # Se escolher 1, retorna 8 vidas.
        if escolha == "1":
            return 8

        # Se escolher 2, retorna 6 vidas.
        elif escolha == "2":
            return 6

        # Se escolher 3, retorna 4 vidas.
        elif escolha == "3":
            return 4

        # Se escolher 4, retorna 2 vidas.
        elif escolha == "4":
            return 2

        # Caso digite algo inválido.
        else:
            print("Opção inválida.\n")
