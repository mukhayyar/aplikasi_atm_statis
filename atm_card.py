class AtmCard:
    def __init__(self, defaultPin, defaultBalance):
        self.defaultPin = defaultPin
        self.defaultBalance = defaultBalance

    def checkPin(self):
        return self.defaultPin
    
    def checkBalance(self):
        return self.defaultBalance