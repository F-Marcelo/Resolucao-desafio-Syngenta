from tests.Hotel import Hotel


def get_cheapest_hotel(dados):  # DO NOT change the function's name

    #Verifica se há entrada nula#
    if dados == '':
        return 'Campos Obrigatórios.'

    precoLake = 0
    precoBridge = 0
    precoRidge = 0

    #Instancia cada hotel#
    Lakewood = Hotel(3, 110, 80, 90, 80)
    Bridgewood = Hotel(4, 160, 110, 60, 50)
    Ridgewood = Hotel(5, 220, 100, 150, 40)


    informacoes = []
    #Retira as informações da entrada obtida#
    entrada = dados

    #Separa o tipo de cliente, se é 'Regular' ou 'Rewards'#
    informacoes.append(entrada.split(":"))

    tipo_cliente = informacoes[0][0]

    #Retira as informações de datas de hopedagem#
    Datas = []
    info_data = informacoes[0][1]
    Datas.append(info_data.split(','))

    Dias_sem = []
    #Retira os dias da semana da data dada na entrada#
    for i in range(len(Datas[0])):

        aux = Datas[0][i].split('(')

        dia_sem = aux[1][:-len(aux) + 1]
        Dias_sem.append(dia_sem)

    #Virifica se as entradas dos dias da semana estão válidas#
    for n in Dias_sem:
        if n not in 'montueswedthurfrisatsun':
            return 'Necessita-se dos dias da semana.'

    #Verifica se o cliente é 'Regular' para o calculo da hospedagem#
    if tipo_cliente == 'Regular':

    #Calculo do valor da hospegagem#
        for dia in Dias_sem:
            #São utilizados métodos presentes na classe hotel
            #para retornar os valores para a semana e final de semana de cada hotel#
            precoLake += Lakewood.ValorReg(dia)
            precoBridge += Bridgewood.ValorReg(dia)
            precoRidge += Ridgewood.ValorReg(dia)

        precos = {'Lakewood': precoLake, 'Bridgewood': precoBridge, 'Ridgewood': precoRidge}

        #Determina qual o menor valor entre os hoteis#
        menorpreco = min(precos, key=precos.get)

        #Verifica se o menor valor é igual a outro hotel com uma classificação maior#
        if precos[menorpreco] == precos['Ridgewood']:
            print('Ridgewood')
            cheapest_hotel = 'Ridgewood'
        elif precos[menorpreco] == precos['Bridgewood']:
            print('Bridgewood')
            cheapest_hotel = 'Bridgewood'
        else:
            print('Lakewood')
            cheapest_hotel = 'Lakewood'

        return cheapest_hotel

    #Aqui tem os mesmos calculos feitos anteriormente, mas para os clientes do tipo 'Rewards'#
    if tipo_cliente == 'Rewards':

        for dia in Dias_sem:
            precoLake += Lakewood.ValorRew(dia)
            precoBridge += Bridgewood.ValorRew(dia)
            precoRidge += Ridgewood.ValorRew(dia)

        precos = {'Lakewood': precoLake, 'Bridgewood': precoBridge, 'Ridgewood': precoRidge}


        menorpreco = min(precos, key=precos.get)


        if precos[menorpreco] == precos['Ridgewood']:
            print('Ridgewood')
            cheapest_hotel = 'Ridgewood'
        elif precos[menorpreco] == precos['Bridgewood']:
            print('Bridgewood')
            cheapest_hotel = 'Bridgewood'
        else:
            print('Lakewood')
            cheapest_hotel = 'Lakewood'

        return cheapest_hotel
