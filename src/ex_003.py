"""
Questão 3 (5.0): Escreva um programa em Python que tome como
entrada um dicionário criado no corpo do programa com dados a respeito
dos empregados de determinada empresa.
As chaves deste dicionário representarão a matrícula de cada um deles na
empresa.

Os valores compreenderão:
      i. nomes completos dos funcionários;
     ii. salários;
    iii. uma lista de inteiros com idade, anos de trabalho na empresa e quantidade de filhos;
     iv. uma indicação lógica sobre se a pessoa é ou não casada.

A estrutura do dicionário deverá seguir o formato do dicionário exemplo
mostrado abaixo (disponível no Moodle no arquivo prova_rec_dic.py).

sintaxe:
    empregados = {
        chave : [nome_pregado, salario, [idade, tempo_trabalho, nros_filhos], casado?]
    }

empregados = {
                '01' : [ 'Fulano da Silva', 1000.00, [29, 5, 0], True ],
                '02' : [ 'Beltrano de Souza', 2000.00, [35, 13, 1], False ],
                '03' : [ 'Sicrano dos Santos', 2500.00, [22, 2, 0], False ],
                '04' : [ 'Maria das Couves', 3000.00, [42, 18, 3], True ],
                '05' : [ 'João Ninguém', 4000.00, [25, 3, 0], False ],
                '06' : [ 'Maria Chiquinha', 2230.00, [34, 12, 2], True ],
                '07' : [ 'João Valentão', 1400.00, [30, 8, 0], True ],
                '08' : [ 'Nonô Sem Dente', 27000.00, [20, 1, 0], False ],
                '09' : [ 'Robernélson da Luz', 3000.00, [45, 25, 4], True ],
                '10' : [ 'José Maria João', 1000.00, [38, 7, 1], True ],
                '11' : [ 'Agrícola Beterraba Areia Leão', 1500.00, [32, 9, 1], True ],
                '12' : [ 'Kenquem que Ninguém Quer', 800.00, [31, 4, 2], True ],
                '13' : [ 'Lindolfa Celidônia Calafange de Tefé', 25000.00, [21, 2, 0], False ],
                '14' : [ 'Simplício Simplório da Simplicidade Simples', 10000.00, [29, 5, 0], True ],
                '15' : [ 'Anônimo João Torquato', 7200.00, [40, 17, 0], False ]
             }

Para o exemplo acima, a primeira linha do dicionário apresenta o empregado 'Fulano da
Silva', que ganha R$ 1.000,00 de salário, possui 29 anos, trabalha há 5 anos na empresa,
não tem filhos e é casado.

Para um dicionário qualquer construído no padrão do exemplo acima,
construa um algoritmo que imprima:
    a) Os nomes completos de todos os funcionários, juntamente com seus
    salários e o número de letras de cada nome.
    b) O somatório total dos salários da empresa, com duas casas decimais.
    c) A média dos salários da empresa, com duas casas decimais.
    d) Uma verificação sobre se a parte inteira da média salarial é divisível por
    10, por 5, e/ou por 2. Se não for divisível por nenhum, informe também.
    e) A quantidade de palavras “Maria” e a quantidade de palavras “João”
    que existem nos nomes dos funcionários (levar em consideração erros
    de digitação e acentuação). Apresente um valor para cada termo.
    f) Uma indicação a respeito das quantidades de palavras “Maria” e “João”
    serem par ou ímpar (levar em consideração erros de digitação e
    acentuação). Apresente um valor para cada termo.
    g) O nome do empregado que ganha o maior salário, a matrícula e quantidade de filhos.
    h) O nome do empregado que ganha o menor salário, a matrícula e o tempo de empresa.
    i) A média de idade dos empregados, com duas casas depois da vírgula.
    j) O nome do empregado mais velho, se é casado ou não e a quantidade de filhos.
    k) O nome do empregado mais novo, se é casado ou não e o tempo de empresa.
    l) A matrícula e o nome dos empregados casados e sem filhos.
    m) A matrícula e o nome dos empregados solteiros e com filhos.
    n) A quantidade total de filhos do conjunto dos empregados da empresa.
    o) O nome do empregado mais antigo na empresa e o tempo de empresa.
    p) O nome e o tempo de empresa do empregado casado que trabalha há menos tempo na empresa.
    q) O nome e o tempo de empresa do empregado solteiro que trabalha há mais tempo na empresa.
    r) A média salarial dos casados, com duas casas depois da vírgula.
    s) O total e o nome completo dos empregados que possuem a letra 'a' (em qualquer formato, com ou sem acentuação) 
    no seu nome ou sobrenome.
    t) A lista dos nomes completos de todos os empregados, em ordem alfabética invertida pelos últimos sobrenomes.

    Importante: O seu código precisa ser genérico o suficiente para funcionar
    com qualquer dicionário que possua o formato indicado acima, e não apenas
    com o dicionário exemplo. A resposta que não levar isso em consideração
    será desconsiderada.

"""

empregados = {
                '01' : [ 'Fulano da Silva', 1000.00, [29, 5, 0], True ],
                '02' : [ 'Beltrano de Souza', 2000.00, [35, 13, 1], False ],
                '03' : [ 'Sicrano dos Santos', 2500.00, [22, 2, 0], False ],
                '04' : [ 'Maria das Couves', 3000.00, [42, 18, 3], True ],
                '05' : [ 'João Ninguém', 4000.00, [25, 3, 0], False ],
                '06' : [ 'Maria Chiquinha', 2230.00, [34, 12, 2], True ],
                '07' : [ 'João Valentão', 1400.00, [30, 8, 0], True ],
                '08' : [ 'Nonô Sem Dente', 27000.00, [20, 1, 0], True ],
                '09' : [ 'Robernélson da Luz', 3000.00, [45, 25, 4], True ],
                '10' : [ 'José Maria João', 1000.00, [38, 7, 1], True ],
                '11' : [ 'Agrícola Beterraba Areia Leão', 1500.00, [32, 33, 1], False ],
                '12' : [ 'Kenquem que Ninguém Quer', 800.00, [31, 4, 2], True ],
                '13' : [ 'Lindolfa Celidônia Calafange de Tefé', 25000.00, [21, 2, 0], False ],
                '14' : [ 'Simplício Simplório da Simplicidade Simples', 10000.00, [55, 35, 0], True ],
                '15' : [ 'Anônimo João Torquato', 7200.00, [40, 17, 0], False ]
            }

# --------------------------------------------- SEÇÃO DEFINIÇÃO VARIÁVEL --------------------------------------------

# a) Os nomes completos de todos os funcionários, juntamente com seus salários e o número de letras de cada nome.
infos_funcionario = []             # infos_func = [nome, salario, nro_letra]

# b) O somatório total dos salários da empresa, com duas casas decimais.
total_salario_empresa = 0

# c) A média dos salários da empresa, com duas casas decimais.
media_salario_empresa = 0

# d) Uma verificação sobre se a parte inteira da média salarial é divisível por 10, por 5, e/ou por 2. Se não for divisível por nenhum, informe também.


# e) A quantidade de palavras “Maria” e a quantidade de palavras “João” que existem nos nomes dos funcionários (levar em consideração erros
# de digitação e acentuação). Apresente um valor para cada termo.
qtidade_nome_maria = 0
qtidade_nome_joao = 0

# g) O nome do empregado que ganha o maior salário, a matrícula e quantidade de filhos.
infos_func_maior_salario = []   # infos_func_maior_salario = [nome, matricula, qtidade_filhos]
maior_salario = 0

# h) O nome do empregado que ganha o menor salário, a matrícula e o tempo de empresa.
infos_func_menor_salario = []   # infos_func_menor_salario = [nome, matricula, tempo_trabalho]
menor_salario = 0

# i) A média de idade dos empregados, com duas casas depois da vírgula.
total_idade = 0
idade_media_funcs = 0

# j) O nome do empregado mais velho, se é casado ou não e a quantidade de filhos.
maior_idade = 0                 # auxilia no encontrar 
infos_func_maior_idade = []     # nome_func_mais_velho = [nome, estado_civil(Casado, Solteiro), qtdade_filhos]

# k) O nome do empregado mais novo, se é casado ou não e o tempo de empresa.
menor_idade = 0
infos_func_menor_idade = []     # nome_func_mais_novo = [nome, estado_civil(Casado, Solteiro), tempo_trabalho]



# l) A matrícula e o nome dos empregados casados e sem filhos.
infos_func_c_sfilhos = []       # infos_func_c_sfilhos = [matricula, nome] --> informações dos funcionarios casados e sem filhos

# m) A matrícula e o nome dos empregados solteiros e com filhos.
infos_func_s_cfilhos = []       # infos_func_s_cfilhos = [matricula, nome] --> informações dos funcionarios solteiros e com filhos

# n) A quantidade total de filhos do conjunto dos empregados da empresa.
total_filhos_funcs = 0

# o) O nome do empregado mais antigo na empresa e o tempo de empresa.
maior_tempo_empresa = 0         # maior_tempo_empresa variavel que ajuda a encontrar o funcionario na linha O
infos_func_antigo = []          # infos_func_antigo = [nome, tempo] --> informações do funcionario com mais tempo de empresa

# p) O nome e o tempo de empresa do empregado casado que trabalha há menos tempo na empresa.
menor_tempo_empresa = 0         # menor_tempo_empresa variavel que ajuda a encontrar o funcionarios na linha p
infos_func_c_menos_tempo = []   # infos_func_c_menos_tempo = [nome, tempo_trabalho] --> informações do funcionario casa com menos tempo de empresa

# q) O nome e o tempo de empresa do empregado solteiro que trabalha há mais tempo na empresa.
maior_tempo_s_empresa = 0       # maior_tempo_s_empresa variavel que ajuda a encontrar os funcionarios nas linhas o e q
infos_func_s_mais_tempo = []    # infos_func_s_mais_tempo = [nome, tempo_trabalho] --> informações do funcionario solteiro com mais tempo de empresa


# r) A média salarial dos casados, com duas casas depois da vírgula.
media_salario_casado = 0
total_salario_casado = 0

# s) O total e o nome completo dos empregados que possuem a letra 'a' (em qualquer formato, com ou sem acentuação)
# no seu nome ou sobrenome.
total_funcionario_nome_contem_a = 0
nome_funcionarios_nome_contem_a = []

# t) A lista dos nomes completos de todos os empregados, em ordem alfabética invertida pelos últimos sobrenomes.
ordena_alf_invertida_sobrenome_funcionario = {}   # ordena_alf_invertida_sobrenome_funcionario = {sobrenome: nome_funcionario}

# -----------------------------------------------------------------------------------------------


"""
sintaxe:
    empregados = {
        chave : [nome_pregado, salario, [idade, tempo_trabalho, nros_filhos], casado?]
    }
"""

# biblioteca para retirar todos os acentos
from unidecode import unidecode


for key in empregados.keys():

    nome_funcionario = empregados[key][0]
    salario_funcionario = empregados[key][1]
    idade_funcionario = empregados[key][2][0]
    tempo_funcionario = empregados[key][2][1]
    nros_filhos_funcionario = empregados[key][2][2]
    estado_civil = empregados[key][3]

    nome_sem_espacos = ''
    for parte_nome in nome_funcionario.split(' '):
        nome_sem_espacos += parte_nome

    nro_letra_funcionario = len(nome_sem_espacos)

    # a) Os nomes completos de todos os funcionários, juntamente com seus salários e o número de letras de cada nome.
    infos_funcionario += [(nome_funcionario, salario_funcionario, nro_letra_funcionario)]
    
    # b) O somatório total dos salários da empresa, com duas casas decimais.
    total_salario_empresa += salario_funcionario

    # e) A quantidade de palavras “Maria” e a quantidade de palavras “João” que existem nos nomes dos funcionários (levar em consideração erros
    # de digitação e acentuação). Apresente um valor para cada termo.
    if 'maria' in unidecode(nome_funcionario.lower()):
        qtidade_nome_maria += 1

    if 'joao' in unidecode(nome_funcionario.lower()):
        qtidade_nome_joao += 1

    # g) O nome do empregado que ganha o maior salário, a matrícula e quantidade de filhos.
    if maior_salario < salario_funcionario:
        if maior_salario == 0:
            menor_salario = salario_funcionario

        maior_salario = salario_funcionario
        infos_func_maior_salario.clear()

        infos_func_maior_salario += [nome_funcionario]
        infos_func_maior_salario += [key]
        infos_func_maior_salario += [nros_filhos_funcionario]
    
    # h) O nome do empregado que ganha o menor salário, a matrícula e o tempo de empresa.
    if menor_salario > salario_funcionario:
            menor_salario = salario_funcionario
            infos_func_menor_salario.clear()

            infos_func_menor_salario += [nome_funcionario]
            infos_func_menor_salario += [key]
            infos_func_menor_salario += [tempo_funcionario]

    # i) A média de idade dos empregados, com duas casas depois da vírgula.
    total_idade += idade_funcionario 

    # j) O nome do empregado mais velho, se é casado ou não e a quantidade de filhos.
    if maior_idade < idade_funcionario:
        if maior_idade == 0:
            menor_idade = idade_funcionario

        maior_idade = idade_funcionario
        infos_func_maior_idade.clear()

        infos_func_maior_idade += [nome_funcionario]
        if estado_civil:
            infos_func_maior_idade += ['Casado']
        else:
            infos_func_maior_idade += ['Solteiro']
        infos_func_maior_idade += [nros_filhos_funcionario]
    
    # k) O nome do empregado mais novo, se é casado ou não e o tempo de empresa.
    if menor_idade > idade_funcionario:
            menor_idade = idade_funcionario
            infos_func_menor_idade.clear()

            infos_func_menor_idade += [nome_funcionario]
            if estado_civil:
                infos_func_menor_idade += ['Casado']
            else:
                infos_func_menor_idade += ['Solteiro']
            infos_func_menor_idade += [tempo_funcionario]

    # l) A matrícula e o nome dos empregados casados e sem filhos.
    # infos_func_c_sfilhos = [matricula, nome]
    if estado_civil and nros_filhos_funcionario == 0:
        infos_func_c_sfilhos += [(key, nome_funcionario)]

    # m) A matrícula e o nome dos empregados solteiros e com filhos.
    # infos_func_s_cfilhos = [matricula, nome]
    if not estado_civil and nros_filhos_funcionario:
        infos_func_s_cfilhos += [(key, nome_funcionario)]

    # n) A quantidade total de filhos do conjunto dos empregados da empresa.
    total_filhos_funcs += nros_filhos_funcionario

    # o) O nome do empregado mais antigo na empresa e o tempo de empresa.
    # infos_func_antigo = [nome, tempo]
    if maior_tempo_empresa < tempo_funcionario:
        if maior_tempo_empresa == 0:
            menor_tempo_empresa = tempo_funcionario
        
        maior_tempo_empresa = tempo_funcionario
        infos_func_antigo.clear()
        infos_func_antigo += [nome_funcionario]
        infos_func_antigo += [maior_tempo_empresa]

    # p) O nome e o tempo de empresa do empregado casado que trabalha há menos tempo na empresa.
    # infos_func_antigo = [nome, tempo]
    if menor_tempo_empresa > tempo_funcionario and estado_civil:        
        menor_tempo_empresa = tempo_funcionario
        infos_func_c_menos_tempo.clear()
        infos_func_c_menos_tempo += [nome_funcionario]
        infos_func_c_menos_tempo += [menor_tempo_empresa]

    # q) O nome e o tempo de empresa do empregado solteiro que trabalha há mais tempo na empresa.
    # infos_func_s_mais_tempo = [nome, tempo_trabalho]
    # valida se o estado civil do funcionario e solteiro
    if maior_tempo_s_empresa < tempo_funcionario and not estado_civil:
        maior_tempo_s_empresa = tempo_funcionario
        infos_func_s_mais_tempo.clear()
        infos_func_s_mais_tempo += [nome_funcionario]
        infos_func_s_mais_tempo += [maior_tempo_s_empresa]
    
    # r) A média salarial dos casados, com duas casas depois da vírgula.
    if estado_civil:
        total_salario_casado += salario_funcionario

    # s) O total e o nome completo dos empregados que possuem a letra 'a' (em qualquer formato, com ou sem acentuação)
    # no seu nome ou sobrenome.
    if 'a' in unidecode(nome_funcionario.lower()):
        total_funcionario_nome_contem_a += 1
        nome_funcionarios_nome_contem_a += [nome_funcionario]

    # t) A lista dos nomes completos de todos os empregados, em ordem alfabética invertida pelos últimos sobrenomes.
    # i) Os nomes de todas as esposas ordenados alfabeticamente pelos últimos sobrenomes.
    ultimo_sobrenome = nome_funcionario.rsplit(' ', maxsplit=1)[1]
    ordena_alf_invertida_sobrenome_funcionario[ultimo_sobrenome] = nome_funcionario   

else:
    total_func = len(empregados.keys())

    print('\na) Os nomes completos de todos os funcionários, juntamente com seus salários e o número de letras de cada nome.')
    for infos in infos_funcionario:
        print(f'    Nome Funcionário: {infos[0]}')
        print(f'    Salário: R$ {infos[1]:.2f}')
        print(f'    Número letras: {infos[2]}')
        print()

    print('\nb) O somatório total dos salários da empresa, com duas casas decimais.')
    print(f'    Total dos Salários da Empresa: R$ {total_salario_empresa}')

    # calculando a média salarial da empresa
    media_salario_empresa = round(total_salario_empresa / total_func, 2)
    print('\nc) A média dos salários da empresa, com duas casas decimais.')
    print(f'    Média Salarial da Empresa: R$ {media_salario_empresa}')

    # retirando a parte inteira do resultante da média
    parte_inteira_media_salario_empresa = int(media_salario_empresa)
    print('''\nd) Uma verificação sobre se a parte inteira da média salarial é divisível por 10, por 5, e/ou por 2.
Se não for divisível por nenhum, informe também.''')
    if parte_inteira_media_salario_empresa % 10 == 0:
        print(f'    Parte inteira da média salário empresa: {parte_inteira_media_salario_empresa} é divisível por 10')
    else:
        print(f'    Parte inteira da média salário empresa: {parte_inteira_media_salario_empresa} é não divisível por 10')
    if parte_inteira_media_salario_empresa % 5 == 0:
        print(f'    Parte inteira da média salário empresa: {parte_inteira_media_salario_empresa} é divisível por 5')
    else:
        print(f'    Parte inteira da média salário empresa: {parte_inteira_media_salario_empresa} é não divisível por 5')
    if parte_inteira_media_salario_empresa % 2 == 0:
        print(f'    Parte inteira da média salário empresa: {parte_inteira_media_salario_empresa} é divisível por 2')
    else:
        print(f'    Parte inteira da média salário empresa: {parte_inteira_media_salario_empresa} é não divisível por 2')

    print('''\ne) A quantidade de palavras “Maria” e a quantidade de palavras “João” que existem nos nomes dos funcionários 
(levar em consideração erros de digitação e acentuação). Apresente um valor para cada termo.''')
    print(f'    Quantidade de palavras Maria: {qtidade_nome_maria}')
    print(f'    Quantidade de palavras João: {qtidade_nome_joao}')

    print('''\nf) Uma indicação a respeito das quantidades de palavras “Maria” e “João” serem par ou ímpar 
(levar em consideração erros de digitação e acentuação). Apresente um valor para cada termo.''')
    if qtidade_nome_maria % 2 == 0:
        print(f'    Quantidade de palavras Maria [{qtidade_nome_maria}]: Par')
    else:
        print(f'    Quantidade de palavras Maria [{qtidade_nome_maria}]: Ímpar')
    if qtidade_nome_joao % 2 == 0:
        print(f'    Quantidade de palavras João [{qtidade_nome_joao}]: Par')
    else:
        print(f'    Quantidade de palavras João [{qtidade_nome_joao}]: Ímpar')

    print('\ng) O nome do empregado que ganha o maior salário, a matrícula e quantidade de filhos.')
    print(f'    Nome Funcionário: {infos_func_maior_salario[0]} --- Matrícula: {infos_func_maior_salario[1]} --- Qtidade Filhos: {infos_func_maior_salario[2]}')

    print('\nh) O nome do empregado que ganha o menor salário, a matrícula e o tempo de empresa.')
    print(f'    Nome Funcionário: {infos_func_menor_salario[0]} --- Matrícula: {infos_func_menor_salario[1]} --- Tempo na Empresa: {infos_func_menor_salario[2]}')

    # calculando a idade média
    idade_media_funcs = round(total_idade/total_func)
    print('\ni) A média de idade dos empregados, com duas casas depois da vírgula.')
    print(f'    Idade média dos funcionario: {idade_media_funcs}')

    print('\nj) O nome do empregado mais velho, se é casado ou não e a quantidade de filhos.')
    print(f'    Nome Funcionário: {infos_func_maior_idade[0]} --- Estado Cívil: {infos_func_maior_idade[1]} --- Qtidade Filhos: {infos_func_maior_idade[2]}')

    print('\nk) O nome do empregado mais novo, se é casado ou não e o tempo de empresa.')
    print(f'    Nome Funcionário: {infos_func_menor_idade[0]} --- Estado Cívil: {infos_func_menor_idade[1]} --- Tempo na Empresa: {infos_func_menor_idade[2]}')

    print('\nl) A matrícula e o nome dos empregados casados e sem filhos.')
    for infos in infos_func_c_sfilhos:
        print(f'    Matrícula: {infos[0]} --- Nome Funcionário: {infos[1]}')

    print('\nm) A matrícula e o nome dos empregados solteiros e com filhos.')
    for infos in infos_func_s_cfilhos:
        print(f'    Matrícula: {infos[0]} --- Nome Funcionário: {infos[1]}')

    print('\nn) A quantidade total de filhos do conjunto dos empregados da empresa.')
    print(f'    Total de filhos do conjunto de funcionários: {total_filhos_funcs}')

    print('\no) O nome do empregado mais antigo na empresa e o tempo de empresa.')
    print(f'    Nome Funcionário: {infos_func_antigo[0]} --- Tempo na Empresa: {infos_func_antigo[1]}')

    print('\np) O nome e o tempo de empresa do empregado casado que trabalha há menos tempo na empresa.')
    print(f'    Nome Funcionário: {infos_func_c_menos_tempo[0]} --- Tempo na Empresa: {infos_func_c_menos_tempo[1]}')

    print('\nq) O nome e o tempo de empresa do empregado solteiro que trabalha há mais tempo na empresa.')
    print(f'    Nome Funcionário: {infos_func_s_mais_tempo[0]} --- Tempo na Empresa: {infos_func_s_mais_tempo[1]}')

    # calculando a média salarial dos casado
    media_salario_casado = round(total_salario_casado / total_func, 2)
    print('\nr) A média salarial dos casados, com duas casas depois da vírgula.')
    print(f'    Média Salarial dos Casados na Empresa: R$ {media_salario_casado}')

    print('''\ns) O total e o nome completo dos empregados que possuem a letra "a" (em qualquer formato, com ou sem acentuação)
no seu nome ou sobrenome.''')
    print(f'    Total de nomes que contém a letra "a": {total_funcionario_nome_contem_a}')
    print()
    for nome in nome_funcionarios_nome_contem_a:
        print(f'    -- {nome}')

    # gerando lista de sobrenomes
    ultimo_sobrenome = list(ordena_alf_invertida_sobrenome_funcionario.keys())
    ultimo_sobrenome.sort(reverse=True) # invertendo a ordem alfabetica da lista
    print('\nt) A lista dos nomes completos de todos os empregados, em ordem alfabética invertida pelos últimos sobrenomes.')
    for nome in ultimo_sobrenome:
        print(f'    -- {ordena_alf_invertida_sobrenome_funcionario.get(nome)}')