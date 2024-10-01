class Time:
    def init(self, hours, minutes, seconds):
        self.hours=hours
        self.minutes=minutes
        self.seconds=seconds
        
class Hour(Time):
    def increased_to_five(self):
        self.hours+=5
        print(f"Soat: {self.hours}")
    
class Minute(Time):
    def increased_to_five(self):
        self.minutes+=5
        print(f"Minutlar: {self.minutes}")
        
class Second(Time):
    def increased_to_five(self):
        self.seconds+=5
        print(f"Soniyalar: {self.seconds}")

print("Kirish: ")
hours=int(input("Soatni kiriting: "))
minutes=int(input("Minutni kiriting: "))
seconds=int(input("Soniyani kiriting: "))

print()
print("Chiqish: ")
time1=Hour(hours, minutes, seconds)
time1.increased_to_five()
time2=Minute(hours, minutes, seconds)
time2.increased_to_five()
time3=Second(hours, minutes, seconds)
time3.increased_to_five()