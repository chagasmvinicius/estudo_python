from pickle import FALSE
import adivinhacao_num, forca

def escolha_jogos():
    print('\n########################################')
    print('###### ESCOLHA UM JOGO PARA JOGAR! ######')
    print('########################################\n')

    escolha_feita = False

    while escolha_feita == False:
        escolha_jogo = int(input('\n(1) Jogo de Adivinhação de Números\n(2) Jogo da Forca\nDigite o número do jogo de sua escolha: '))

        if escolha_jogo == 1:
            escolha_feita = True
            adivinhacao_num.jogar()
        elif escolha_jogo == 2:
            escolha_feita = True
            forca.jogar()
        else:
            print('Escolha um dos números dos jogos existentes: 1 ou 2.\n')

if __name__ == '__main__':
    escolha_jogos()