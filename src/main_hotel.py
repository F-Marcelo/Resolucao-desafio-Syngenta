from tests.Hotel import Hotel
from src.my_module import get_cheapest_hotel


Lakewood = Hotel(3, 110, 80, 90, 80)
Bridgewood = Hotel(4, 160, 110, 60, 50)
Ridgewood = Hotel(5, 220, 100, 150, 40)


informacoes = []


entrada = input('Informações de hospedagem: ')

#entrada == Regular: 16Mar2009(mon), 17Mar2009(tues), 18Mar2009(wed)
informacoes.append(entrada.split(":"))
print(f'informacoes = {informacoes}')
tipo_cliente = informacoes[0][0]
print(f'tipo cliente = {tipo_cliente}')

Datas = []
info_data = informacoes[0][1]
Datas.append(info_data.split(','))
print(f'Datas = {Datas}')

Dias_sem = []

for i in range(len(Datas[0])):
    print(f'dias semana = {Datas[0][i]}')
    aux = Datas[0][i].split('(')
    print(aux[1][:-len(aux)+1])
    dia_sem = aux[1][:-len(aux)+1]
    Dias_sem.append(dia_sem)

print(Dias_sem)
print(f'total dias = {len(Dias_sem)}')

if tipo_cliente == 'Regular':

    precoLake = 0
    precoBridge = 0
    precoRidge = 0

    for dia in Dias_sem:
        precoLake += Lakewood.ValorReg(dia)
        precoBridge += Bridgewood.ValorReg(dia)
        precoRidge += Ridgewood.ValorReg(dia)

    get_cheapest_hotel(precoLake, precoBridge, precoRidge)

if tipo_cliente == 'Rewards':
    precoLake = 0
    precoBridge = 0
    precoRidge = 0

    for dia in Dias_sem:
        precoLake += Lakewood.ValorRew(dia)

        precoBridge += Bridgewood.ValorRew(dia)

        precoRidge += Ridgewood.ValorRew(dia)

    get_cheapest_hotel(precoLake, precoBridge, precoRidge)