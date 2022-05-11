class Hotel:
    def __init__(self, Classificacao, TaxaRegSe, TaxaRewSe, TaxaRegFds, TaxaRewFds):
        self.clas = Classificacao
        self.TaxRegS = TaxaRegSe
        self.TaxRewS = TaxaRewSe
        self.TaxRegFds = TaxaRegFds
        self.TaxRewFds = TaxaRewFds

    def getClas(self):
        return self.clas

    def getTaxRegS(self):
        return self.TaxRegS

    def getTaxRewS(self):
        return self.TaxRewS

    def getTaxRegFds(self):
        return self.TaxRegFds

    def getTaxRewFds(self):
        return self.TaxRewFds

    #Métodos para retornar os valores a partir do tipo do cliente e de qual dia da semana#

    def ValorReg(self, data):
        if data in 'montueswedthurfri':
            return self.TaxRegS
        else:
            return self.TaxRegFds

    def ValorRew(self, data):
        if data in 'montueswedthurfri':
            return self.TaxRewS

        else:
            return self.TaxRewFds
