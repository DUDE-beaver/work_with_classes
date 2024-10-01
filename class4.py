class Odam:
    def init(self, name, name_subject):
        self.name=name
        self.name_subject=name_subject
        
    def tepish(self):
        pass
        
class Koptok(Odam):
    def uchish(self):
        print(f"{self.name} {self.name_subject}ni tepdi.")
        print(f"Tepgandan keyin {self.name_subject} uchib ketdi.")

ball=Koptok("Zokir", "koptok")   

ball.tepish()
ball.uchish()