class classroom:
    def __init__(self):
        self.cgst=0.18
        self.sgst=0.18
        self.insurance=100000
    def company(self):
        while True:
            print("select a car from ferrari mahindra volva")
            self.n=input("select a car")
            if self.n=="ferrari":
                print("welcome to ferrari")
                self.model()
                break
            elif self.n=="volva":
                print("welcome to volva")
                self.model()
                break
            elif self.n=="mahindra":
                print("welcome to mahindra")
                self.model()
                break
            else:
                print("enter valid data")
                def model(self):
                    if self.n=="ferrari":
                        while True:
                            print("select a car from GTB ROVA")
                            self.choice=input("your desired car")
                            if self.choice=="GTB":
                                self.price(self,choice)
                                break
                            elif self.choice=="s90":
                                self.price(self.choice)
                                break
                            else:
                                print("enter a valid model")
def price(self):
    if self.choice=="GTB":

obj=classroom()
obj.company()
