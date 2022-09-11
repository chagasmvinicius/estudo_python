import random #módulo/biblioteca que possui o método random() ou randrange()

def jogar():
    print('\n########################################')
    print('### BEM VINDO AO JOGO DE ADIVINHACAO ###')
    print('########################################\n')

    count = 1
    chute = 0
    # numeroSecreto = round(random.random() * 100)
    numeroSecreto = random.randrange(1, 101) # gerar número randomico de 1 até 100.
    pontos = 1000

    print('Níveis de dificuldade\n(1) Fácil\n(2) Médio\n(3) Difícil\n')
    nivel = int(input('Digite o nível de dificuldade (1, 2 ou 3): '))

    if nivel == 1:
        totalTentativas = 20
    elif nivel == 2:
        totalTentativas = 10
    else:
        totalTentativas = 5

    for count in range(1, totalTentativas + 1):
        print('Tentativa {0} de {1}'.format(count, totalTentativas))
        chute = int(input('Digite um número entre 1 e 100: '))

        if chute < 1 or chute > 100:
            print('Você deve informar um número entre 1 e 100!\n')
            continue # o continue faz com que tenha um reset do laço, ou seja, não leia as linhas de código abaixo e inicie o laço novamente.
        
        if chute == numeroSecreto:
            print('ACERTOU! E fez um total de {0} pontos!\n'.format(pontos))
            break # o break faz com que saia do laço (for).
        else:
            if chute > numeroSecreto:
                print('ERROU!!! Chutou um número mais ALTO!\n')
            elif chute < numeroSecreto:
                print('ERROU!!! Chutou um número mais BAIXO!\n')
        pontosPerdidos = abs(numeroSecreto - chute)
        pontos = pontos - pontosPerdidos

    print('Fim de jogo! O número secreto da rodada foi {0}!'.format(numeroSecreto))

if __name__ == '__main__':
    jogar()