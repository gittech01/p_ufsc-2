"""
Questão 2 (2.5):
Em uma eleição existem quatro candidatos. Os votos são informados através
de códigos. O sistema de urnas eletrônicas funciona da seguinte maneira:

    • Usuário digitou “1”, “2”, “3” ou “4” = voto para os respectivos
    candidatos;
    • Usuário digitou “5” = voto em branco;
    • Usuário digitou “0” = fim da eleição;
    • Usuário digitou qualquer outro valor = voto nulo.

Crie um menu para esta Urna Eletrônica, que esclareça o usuário o máximo
possível do que pode ser feito!
Na sequência, elabore um algoritmo que calcule e escreva:

    a) O total de eleitores que votaram;
    b) O total e o percentual total (com duas casas depois da vírgula) de
    votos para cada candidato;
    c) O total e o percentual (com duas casas depois da vírgula) de votos
    nulos;
    d) O total e o percentual (com duas casas depois da vírgula) de votos
    em branco;
    e) O nome do vencedor da eleição (Importante: se dois ou mais candidatos obtiverem o mesmo número de votos, informe que a
eleição irá para o segundo turno).

Explicando o exercício:
Candidatos:

    1 --> A
    2 --> B
    3 --> C
    4 --> D

    5 --> Voto Branco
    0 --> Fim da Eleição
    [6, +infinito[ --> Voto nulo

variaveis:
# variavel que vai guardar a quantidade de eleitores que votaram
a) total_eleitores = 0

# dicionario que conterá as informações do candita após eleição
sintaxe: 
informacao_de_votos_dos_candidatos = {
    candidato: [total_de_votos, porcentual_do_total]
}

Ex.: informacao_de_votos_dos_candidatos = {
    'A': [0, 0]
}

# quantidade de votos nulos e o porcentual do total
sintaxe: total_votos_nulos = [total_votos, porcentual_votos]
c) total_votos_nulos = [0, 0]

# quantidade de votos brancos e o porcentual do total
sintaxe: total_votos_brancos = [total_votos, porcentual_votos]
d) total_votos_brancos = [0, 0]

# vencendor da eleicao:
e) vencendor = ''

"""

total_eleitores = 0
informacao_de_votos_dos_candidatos = {
    'A': [0, 0],
    'B': [0, 0],
    'C': [0, 0],
    'D': [0, 0],
    'Votos Brancos': [0, 0],
    'Votos Nulos': [0, 0],
}

vencendor = ''


while True:
    voto = input(
        """
+-----------------------------------------------------------+
|                BEM VINDO A URNA ELECTRÓNICA               |
+-----------------------------------------------------------+

Escolhe o seu candidato um função do número que o representa:

    [1] --> A
    [2] --> B
    [3] --> C
    [4] --> D
    [5] --> Voto Branco

Ou digite [0] para encerrar.
Resp: """).strip()
    
    if voto == '0':
        print('Eleição encerrada!')
        break
    else:
        total_eleitores += 1

    if voto == '1':
        informacao_de_votos_dos_candidatos['A'][0] += 1
    elif voto == '2':
        informacao_de_votos_dos_candidatos['B'][0] += 1
    elif voto == '3':
        informacao_de_votos_dos_candidatos['C'][0] += 1
    elif voto == '4':
        informacao_de_votos_dos_candidatos['D'][0] += 1
    elif voto == '5':
        informacao_de_votos_dos_candidatos['Votos Brancos'][0] += 1
    else:
        informacao_de_votos_dos_candidatos['Votos Nulos'][0] += 1


if total_eleitores != 0:
    # calculando os porcentuais de cada candidato e de votos branco:
    for candidato in informacao_de_votos_dos_candidatos.keys():
        informacao_de_votos_dos_candidatos[candidato][1] = round(informacao_de_votos_dos_candidatos[candidato][0]/total_eleitores * 100, 2)
 
    porcentagem = 0
    validador_de_empate = 0
    nomes_dos_candidatos_empataram = []

    for candidato in informacao_de_votos_dos_candidatos.keys():
        if candidato.strip() not in ('Votos Brancos', 'Votos Nulos'):
            porcentagem_candidato = informacao_de_votos_dos_candidatos[candidato][1]

            if porcentagem == 0:
                porcentagem = porcentagem_candidato
                vencendor = candidato
                nomes_dos_candidatos_empataram += [candidato]
                continue

            if porcentagem < porcentagem_candidato:
                porcentagem = porcentagem_candidato
                vencendor = candidato
                nomes_dos_candidatos_empataram.pop()
                nomes_dos_candidatos_empataram += [candidato]
    else:
        for candidato in informacao_de_votos_dos_candidatos.keys():
            if candidato.strip() not in ('Votos Brancos', 'Votos Nulos', vencendor):
                porcentagem_candidato = informacao_de_votos_dos_candidatos[candidato][1]

                if porcentagem_candidato == porcentagem:
                    validador_de_empate += 1
                    nomes_dos_candidatos_empataram += [candidato]

            


print("\nProcessando os resultados...")

# a) O total de eleitores que votaram
print(f'\nO total de eleitores que votaram: {total_eleitores}\n')
print('   Candidato         Votos           %')
for candidatos in informacao_de_votos_dos_candidatos.keys():
    votos = informacao_de_votos_dos_candidatos[candidatos][0]
    porcs = informacao_de_votos_dos_candidatos[candidatos][1]
    print(f' {candidatos.center(13)}        {str(votos).zfill(2)}           {str(porcs).zfill(5)}')

if validador_de_empate == 0:
    print(f'\nVencedor das urnas foi: {vencendor} com {porcentagem:.2f}%')
else:
    print(f'\nAs Eleições teram segundo turno com os candidatos: {nomes_dos_candidatos_empataram}')