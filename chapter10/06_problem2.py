from random import randint

class train:
    def __init__(self,trainno):  #you can also use slf instead of self everywhwere even you can use any word
        self.trainno=trainno  

    def book(self,fro,to):
        print(f"train number {self.trainno} is booked successfully from {fro} to {to}")

    def status(self):
        print(f"train number {self.trainno} is currently in running phase") 

    def getfare(self,fro,to):
        print(f"fare for train number {self.trainno} from {fro} to {to} is {randint(100,500)}")

a=train(476001)
a.book("morena","delhi")
a.status()
a.getfare("morena","delhi")     
        