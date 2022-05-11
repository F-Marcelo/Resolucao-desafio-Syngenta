import unittest
from unittest import TestCase
from src.my_module import get_cheapest_hotel

class MyTest(TestCase):
    def tests1(self):
        result = "Lakewood"
        self.assertEqual(result, get_cheapest_hotel("Regular: 16Mar2009(mon), 17Mar2009(tues), 18Mar2009(wed)"))

    def tests2(self):
        result = "Bridgewood"
        self.assertEqual(result, get_cheapest_hotel("Regular: 20Mar2009(fri), 21Mar2009(sat), 22Mar2009(sun)"))

    def tests3(self):
        result = "Ridgewood"
        self.assertEqual(result, get_cheapest_hotel("Rewards: 26Mar2009(thur), 27Mar2009(fri), 28Mar2009(sat)"))

    #Teste criado para verificar se há entrada vazia#
    def tests4(self):
        result = 'Campos Obrigatórios.'
        self.assertEqual(result, get_cheapest_hotel(""))

    #Teste feito para verificar se os dias da semana são válidos#
    def tests5(self):
        result = 'Necessita-se dos dias da semana.'
        self.assertEqual(result, get_cheapest_hotel("Rewards: 26Mar2009(teste), 27Mar2009(teste), 28Mar2009(teste)"))

if __name__ == '__main__':
    unittest.main()
