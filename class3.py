import time

class Odam:
    def init(self, name):
        self.name=name
        
    def yugurish(self):
        print(f"{self.name} yugurvotdi.")

    def yiqilish(self):
        print(f"{self.name} yiqildi.")

name=input("Foydalanuvchining ismini kiriting: ")
print()
human=Odam(name)

human.yugurish()
time.sleep(5)
human.yiqilish()