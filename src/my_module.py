from tests.Hotel import Hotel


def get_cheapest_hotel(dados):  # DO NOT change the function's name

    precoLake = 0
    precoBridge = 0
    precoRidge = 0

    Lakewood = Hotel(3, 110, 80, 90, 80)
    Bridgewood = Hotel(4, 160, 110, 60, 50)
    Ridgewood = Hotel(5, 220, 100, 150, 40)

    informacoes = []

    entrada = dados

    # entrada == Regular: 16Mar2009(mon), 17Mar2009(tues), 18Mar2009(wed)
    informacoes.append(entrada.split(":"))

    tipo_cliente = informacoes[0][0]


    Datas = []
    info_data = informacoes[0][1]
    Datas.append(info_data.split(','))


    Dias_sem = []

    for i in range(len(Datas[0])):

        aux = Datas[0][i].split('(')

        dia_sem = aux[1][:-len(aux) + 1]
        Dias_sem.append(dia_sem)



    if tipo_cliente == 'Regular':

        for dia in Dias_sem:
            precoLake += Lakewood.ValorReg(dia)
            precoBridge += Bridgewood.ValorReg(dia)
            precoRidge += Ridgewood.ValorReg(dia)

        precos = {'Lakewood': precoLake, 'Bridgewood': precoBridge, 'Ridgewood': precoRidge}


        menorpreco = min(precos, key=precos.get)
        # print(menorpreco)
        # print(precos[menorpreco])

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

    if tipo_cliente == 'Rewards':

        for dia in Dias_sem:
            precoLake += Lakewood.ValorRew(dia)
            precoBridge += Bridgewood.ValorRew(dia)
            precoRidge += Ridgewood.ValorRew(dia)

        precos = {'Lakewood': precoLake, 'Bridgewood': precoBridge, 'Ridgewood': precoRidge}


        menorpreco = min(precos, key=precos.get)
        print(menorpreco)
        print(precos[menorpreco])

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

