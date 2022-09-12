def jogar():
    print('\n########################################')
    print('####### BEM VINDO AO JOGO FORCA ########')
    print('########################################\n')

    palavra_secreta = ('banana').upper()
    
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
    tentativas = 6

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
        print('\nP E R D E U!\nFim de jogo!')

if __name__ == '__main__':
    jogar()
