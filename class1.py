class Human:
    def init(self,ism):
        self.name=ism
        
    def salomlashish(self):
        print()
        print(f"Chiqish: Salom {self.name}")

input_name=input("Foydalanuvchining ismini kiriting: ")

user=Human(input_name)

user.salomlashish()