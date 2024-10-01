class Computer:
    def init(self, name, RAM, value, proccessor):
        self.name=name
        self.RAM=RAM
        self.value=value
        self.proccessor=proccessor

    def kirish(self):
        if 4<=self.RAM<=16:
            diction1=dict()
            diction2=dict()
            diction1["Nomi"]=self.name
            diction1["RAMi"]=self.RAM
            diction1["Narxi"]=self.value
            diction1["Protsessori"]=self.proccessor
            diction2[user_turn+1]=diction1
            list.append(diction2)

    def chiqish(self):
        for value in list:
            d=dict()
            for key1 in value:
                print(f"{key1}-foydalanuvchi: ")
                d=value[key1]
                for key2 in d:
                    print(f"{key2}: {d[key2]}")
                print()    

count_of_users=int(input("Nechta foydalanuvchilar o'z kompyuterlari haqida ma'lumotlarni kiritadi?: "))
list=[]
print()
print("Kirish: ")
for user_turn in range(count_of_users):
    print(f"{user_turn+1}-foydalanuvchi: ")
    computer_name=input("Kompyuterning nomini kiriting: ")
    computer_RAM=int(input("Kompyuterning RAMini kiriting: "))
    computer_value=int(input("Kompyuterning narxini kiriting: "))
    computer_proccessor=input("Kompyuterning protsessori: ")
    print()
    
    var=Computer(computer_name, computer_RAM, computer_value, computer_proccessor)
    
    var.kirish()

print("Chiqish: ")    
var.chiqish()