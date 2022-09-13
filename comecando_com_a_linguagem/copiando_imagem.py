# Abrindo o arquivo em binário
logo = open('Twitter-Logo-650x366.png', 'rb')
data = logo.read()
logo.close()

# Criando um novo arquivo png e inserindo o mesmo código binário da imagem original
logo_copia = open('Twitter-Logo-650x366_2.png', 'wb')
logo_copia.write(data)
logo_copia.close()