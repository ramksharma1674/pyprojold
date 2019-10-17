class Product:
    def __init__(self, name="", price=0.0, discountPercent=0):
        self.name = name
        self.price = price
        self.discountPercent = discountPercent
    

    def getDiscAmount(self):
        return self.price * self.discountPercent / 100
    
    def getDiscPrice(self):
        return self.price - self.getDiscAmount()    