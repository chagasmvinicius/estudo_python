Documentação Python 3: https://docs.python.org/3/tutorial/

🎖 CERTIFICADOS:

[CURSO] PYTHON: COMENÇANDO COM A LINGUAGEM: https://cursos.alura.com.br/certificate/94cae4ff-e32c-420d-9a16-8ed7f9e4b2b1

📝 APRENDIZADOS DIFERENTES:

=> List Comprehensions: https://pythonacademy.com.br/blog/list-comprehensions-no-python

Exemplos:
1. [expr for item in lista]
Em outras palavras: aplique a expressão expr em cada item da lista.

2. [expr for item in lista if cond]
Aplique a expressão expr em cada item da lista caso a condição cond seja satisfeita.

3. [resultado_if if expr else resultado_else for item in lista]
Em outras palavras: para cada item da lista, aplique o resultado resultado_if se a expressão expr for verdadeira, caso contrário, aplique resultado_else.

=> Função open() para leitura (r), escrita (w), inclusão (a) de informações em arquivos: https://docs.python.org/pt-br/3/library/functions.html#open
1. Caso não passemos o modificador de acesso, o "r" (read) será utilizado. O segundo parâmetro da função (modificador de acesso) é opcional. Ex.: arquivo = open("entrada.txt"). Além do "r", "w" e "a" existe o modificador "b" que devemos utilizar quando queremos trabalhar no modo binário. Para abrir uma imagem devemos usar: imagem = open("foto.jpg", "rb").
2. O programa pode parar a execução sem ter fechado o arquivo mesmo com o .close(). Para evitar esse tipo de situação, o Python criou uma sintaxe especial para abertura de arquivo:
with open("palavras.txt") as arquivo:
    for linha in arquivo:
        print(linha)
