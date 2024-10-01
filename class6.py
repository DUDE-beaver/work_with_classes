class Kitob:
    def init(self, name, author, value, publisher):
        self.name=name
        self.author=author
        self.value=value
        self.publisher=publisher

    def kirish(self):
        if 'A'<=self.publisher[0]<='H' or 'a'<=self.publisher[0]<='h':
            diction1=dict()
            diction2=dict()
            diction1["Nomi"]=self.name
            diction1["Muallifi"]=self.author
            diction1["Narxi"]=self.value
            diction1["Nashriyoti"]=self.publisher
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

count_of_users=int(input("Nechta foydalanuvchilar o'z kitoblari haqida ma'lumotlarni kiritadi?: "))
list=[]
print()
print("Kirish: ")
for user_turn in range(count_of_users):
    print(f"{user_turn+1}-foydalanuvchi: ")
    book_name=input("Kitobning nomini kiriting: ")
    book_author=input("Kitobning muallifini kiriting: ")
    book_value=int(input("Kitobning narxini kiriting: "))
    book_publisher=input("Kitobning nashriyotini kiriting: ")
    print()
    
    var=Kitob(book_name, book_author, book_value, book_publisher)
    
    var.kirish()

print("Chiqish: ")    
var.chiqish()