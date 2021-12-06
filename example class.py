class Laptop:
    brand='Lenovo'
    def monitor(self):
        print('shows output')
    def keyboard(self):
        print('gives input')
class Hotel:
    item ='Biriyani'
    def price(self):
        print('Chicken Biriyani\nMutton Biriyani')
class Pubg:
    item='weapons'
    def loot(self):
        print('Low\nMedium\nHigh')
class Games:
    type='FPS'
    def AAA(self):
        print('CSGO\nR6Seige')
steam=Games().AAA()
ideapad=Laptop().monitor()
Thalapakatti=Hotel().price()
newroom=Pubg().loot()


