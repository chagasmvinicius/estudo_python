def jogar():
    print('\n########################################')
    print('####### BEM VINDO AO JOGO FORCA ########')
    print('########################################\n')

    palavra_secreta = 'banana'
    letras_acertadas = []
    for index in palavra_secreta:
        letras_acertadas.append('_')

    acertou = False
    enforcou = False

    print(f'Palavra: {letras_acertadas}')

    while not acertou and not enforcou:
        chute = input("Digite uma letra: ").strip()

        index = 0
        for letra in palavra_secreta:
            if chute.lower() == letra.lower():
                #letras_acertadas.insert(index, letra)
                #letras_acertadas.pop(index + 1)
                # OU... \/
                letras_acertadas[index] = letra
            index = index + 1
        print(letras_acertadas)

if __name__ == '__main__':
    jogar()
