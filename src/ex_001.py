"""
Questão 1 (2.5): Implemente um código que funcione como um jogo de
tradução. O programa deverá possuir um dicionário de no mínimo 30
registros no qual palavras sejam as chaves e os valores uma lista com as
grafias delas em dois idiomas diferentes, à sua escolha. Crie o dicionário
diretamente no código.

No exemplo abaixo, as palavras foram traduzidas para o inglês e francês.
Poderiam ser para outras línguas.

Ex.:
        palavras = {
                        'peixe': ['fish', 'poisson'],
                        'garrafa': ['bottle', 'bouteille'],
                        'computador': ['computer', 'ordinateur'],
                        'boné': ['cap', 'casquette']
                    }

O jogo da tradução deverá possuir exatas 10 rodadas. Em cada rodada, o
usuário deverá entrar com uma palavra em português e uma tradução numa
das línguas estrangeiras. Ao final de todas as rodadas, o jogo imprime os
acertos, de acordo com o exemplo de saída mostrado abaixo.

Exemplo:
    Entrada:
        (Rodada 1/10) Digite uma palavra: xxxxxxx
        Em qual língua você quer verificar a tradução? (digite 'I' para inglês ou 'F' para francês)
        Digite a tradução: yyyyyy
        (Rodada 2/10) Digite uma palavra: wwwww
        Em qual língua você quer verificar a tradução? (digite 'I' para inglês ou 'F' para francês)
        Digite a tradução: zzzzzzzzz
        
        ...
    
    Saída:
        Número total de erros: x
        Número total de acertos: y
        Palavras corretamente traduzidas: “xxxxxxx” (“tradução”), “ssssssss” (“tradução”), ....
        Tentativas fracassadas: “aaaaa” (“tradução incorreta”), “rrrrrr” (“tradução incorreta”), ....

Importante: uma palavra não pode ter sua tradução tentada mais de uma
vez pelo usuário. Verifique também se a palavra digitada existe no dicionário!

Prepare o programa para tratar os dados digitados pelo usuário. Inclua
também mensagens explicativas. Se algum erro acontecer, avise ao usuário
de que o jogo será reiniciado.
"""

# dicionario de validação de traducao ingles e frances
dicionario = {
    'peixe': ['fish', 'poisson'],
    'garrafa': ['bottle', 'bouteille'],
    'computador': ['computer', 'ordinateur'],
    'boné': ['cap', 'casquette']
}

# dicionario de palavras e traducao do usuario que sao fornecenidas no momento de interacao
# onde a chave sera a palavra e o valor sera uma lista com os valores da lingua e a traducao
palavras_lingua_traducao = {}


# nesta secao iteramos quantidade de rodadas [10]
for rodada in range(1, 11):

    # recebe a palavra que o usuario quer validar a traducao
    palavra_a_ser_traduzida = input(f'(Rodada {rodada}/{10}) Digite uma palavra: ').strip().lower()

    # repete a requisicao ao usuario caso a palavra a ser traduzida ja tenha sido inserida
    while palavra_a_ser_traduzida in palavras_lingua_traducao.keys() \
            or palavra_a_ser_traduzida not in dicionario.keys():

        # checa se a palavra inserida consta no dicionário raiz
        # para informar ao usuário o erro cometido
        if palavra_a_ser_traduzida not in dicionario.keys():
            print('Palavra inserida não se encontra no Dicionario Raiz para validar a tradução. Informe uma outra palavra.')

        # checa se a palavra inserida consta no dicionário criado pelo usuário
        # para informar ao usuário o erro cometido
        if palavra_a_ser_traduzida in palavras_lingua_traducao.keys():
            print('Palavra já inserida para validar a tradução. Informe uma outra palavra.')
        
        # interage com o usuário pedindo a palavra certa novamente
        palavra_a_ser_traduzida = input(f'(Rodada {rodada}/{10}) Digite uma palavra: ').strip()

    # escolhe a língua pelo qual quer validar a traducao
    lingua = input("""Em qual língua você quer verificar a tradução? 
    Digite:
        I --> Inglês
        F --> Francês
    Resp: """).strip()

    while lingua.upper() not in ('F', 'I'):
        print('Opção de tradução errada. Inseri as opções válidas!')
        lingua = input("""Em qual língua você quer verificar a tradução? 
    Digite:
        I --> Inglês
        F --> Francês
    Resp: """).strip()


    # traducao da palavra inserida pelo usuario
    traducao_da_palavra = input('Digite a tradução: ').strip()

    # adiciona os valores recebidos do usuario no dicionario
    palavras_lingua_traducao[palavra_a_ser_traduzida] = [lingua, traducao_da_palavra]
else:
    # variaveis que irao contabilizar o total de acerto e erros respetivamente.
    total_acerto = 0
    total_errada = 0

    # lista que guardaram as palavras traduzidas corretas e incorretamente
    palavra_traduzida_corretamente = []
    palavra_traduzida_ncorretamente = []

    for palavra in palavras_lingua_traducao.keys():

        # validacao da palavra na categoria ingles
        if palavras_lingua_traducao[palavra][0].upper() == 'I':
            if palavras_lingua_traducao[palavra][1].lower() == dicionario[palavra][0].lower():
                total_acerto += 1
                palavra_traduzida_corretamente += [f'"{palavra}" ("{dicionario[palavra][0]}")']
                continue
            total_errada += 1
            palavra_traduzida_ncorretamente += [f'"{palavra}" ("{palavras_lingua_traducao[palavra][1]}")']

        # validacao da palavra na categoria frances 
        if palavras_lingua_traducao[palavra][0].upper() == 'F':
            if palavras_lingua_traducao[palavra][1].lower() == dicionario[palavra][1].lower():
                total_acerto += 1
                palavra_traduzida_corretamente += [f'"{palavra}" ("{dicionario[palavra][1]}")']
                continue
            total_errada += 1
            palavra_traduzida_ncorretamente += [f'"{palavra}" ("{palavras_lingua_traducao[palavra][1]}")']

    print()
    print(f'Número total de acerto: {total_acerto}')
    print(f'Número total de erros: {total_errada}')

    print('\nPalavras corretamente traduzidas: ', end='')
    for corretamente in palavra_traduzida_corretamente:
        print(corretamente, end=', ')
    else:
        print('...')
    
    print('\nPalavras fracassadas: ', end='')
    for ncorretamente in palavra_traduzida_ncorretamente:
        print(ncorretamente, end=', ')
    else:
        print('...')