import random

def jogar():
    print('\n########################################')
    print('####### BEM VINDO AO JOGO FORCA ########')
    print('########################################\n')

    # Lendo o arquivo e trazendo as palavras como uma lista. O ".strip()" serve para limpar os espaços em branco e \n.
    palavras = []
    with open('palavras.txt', 'r') as arquivo:
        for linha in arquivo:
            palavras.append(linha.strip())

    palavra_secreta = palavras[random.randrange(0, len(palavras))].upper()
    
    # letras_acertadas = []
    # for index in palavra_secreta:
    #     letras_acertadas.append('_')
    
    # OU... \/
    # letras_acertadas = ['_'] * len(palavra_secreta)
    
    # OU... \/ (list comprehensions)
    letras_acertadas = ['_' for index in palavra_secreta]

    acertou = False
    enforcou = False
    erros = 0
    tentativas = 10

    print(f'Palavra: {letras_acertadas}')

    while not acertou and not enforcou:
        chute = input("Digite uma letra: ").strip().upper()
        print('\n')

        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if chute == letra:
                    #letras_acertadas.insert(index, letra)
                    #letras_acertadas.pop(index + 1)
                    # OU... \/
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
            print(f'Chute com a letra errada! Faltam {tentativas - erros} tentativas!\n')
        
        enforcou = erros == tentativas
        acertou = '_' not in letras_acertadas        
        
        print(letras_acertadas)
    
    if acertou:
        print('\nG A N H O U!\nFim de jogo!')
    else:
        print(f'\nP E R D E U!\nFim de jogo!\nA palavra secreta foi "{palavra_secreta}"')

if __name__ == '__main__':
    jogar()
