
print("---RPG Projekt---")
print("1 = Kezdés")
print("2 = Információk")
print("3 = Kilépés")
print("-----------------\n")

bemenet = int(input("Válassz!(1-3): \n"))

if bemenet == 2:
    print("---Információk---")
    print("infok")
    print("-----------------\n")
    print("---RPG Projekt---")
    print("1 = Kezdés")
    print("2 = Információk")
    print("3 = Kilépés")
    print("-----------------")
    bemenet = int(input("Válassz!(1-3): \n"))

if bemenet == 3:
    print("---Kilépés---")
    
 
class Karakter:
    def __init__(self, nev, eletero, sebzes, szint, penz):
        self.nev = nev
        self.eletero = int(eletero)
        self.sebzes = int(sebzes)
        self.szint = int(szint)
        self.penz = int(penz)

    def adatok(self):
        print(f"A jelenlegi Karaktered: {self.nev}\nÉletereje: {self.eletero}\nSebzése: {self.sebzes}\nképessége: {self.kepesseg}\nPénze: {self.penz}")

    def harc(self):
        pass


def jatek():
    print("---Játék---")
    print("1 = Harc")
    print("2 = Tárgyaid")
    print("3 = ...")
    jatek_menu_valasztas = int(input())
    if jatek_menu_valasztas == 1:
        pass        

if bemenet == 1:
    print(f"A játék elkezdődött!\n")
    karakter = input(f"Add meg a hősöd nevét!")
    jatek()


      

karakter1 = Karakter(karakter, 150, 30, 0, 500)

