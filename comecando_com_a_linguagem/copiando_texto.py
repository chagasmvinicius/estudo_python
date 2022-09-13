# Abrindo o arquivo e salvando os binários na variável "palavras":
conteudo = open('palavras.txt', 'rb')
palavras = conteudo.read()
conteudo.close()

# Criando um novo txt e salvando lá os binários recolhidos anteriormente:
palavras2 = open('palavras2.txt', 'wb')
palavras2.write(palavras)
palavras2.close()