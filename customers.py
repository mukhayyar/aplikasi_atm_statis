from atm_card import AtmCard

class Customers(AtmCard):
    def __init__(self, custPin, custBalance):
        super().__init__(custPin, custBalance)

    def checkPin(self):
        return self.defaultPin
    
    def changePin(self, custPin):
        self.defaultPin = custPin
        return self.defaultPin
    
    def checkBalance(self):
        return self.defaultBalance
    
    def debet_saldo(self, nominal):
        debet = self.defaultBalance - nominal
        return debet
    
    def simpan_saldo(self, nominal):
        simpan = self.defaultBalance + nominal
        return simpan
