class Human:
    def init(self,ism1,ism2):
        self.name1=ism1
        self.name2=ism2
        
    def kuylash(self):
        print()
        print(f"Chiqish: {self.name1} kuylab berdi")
        
    def eshtish(self):    
        print(f"Chiqish: {self.name2} uni eshtdi")
    
    def gapirish(self):    
        print(f"Chiqish: {self.name2} undan zo'r qo'shiqchi chiqishini aytdi")

input_name1=input("Kuylaydigan foydalanuvchining ismini kiriting: ")
input_name2=input("Eshtidigan va gapiridigan foydalanuvchining ismini kiriting: ")

users=Human(input_name1, input_name2)

users.kuylash()
users.eshtish()
users.gapirish()