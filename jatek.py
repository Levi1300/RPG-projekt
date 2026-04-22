from random import randint
print("\n---RPG Projekt---")
print("1 = Kezdés")
print("2 = Információk")
print("3 = Kilépés")
print("-----------------\n")

bemenet = int(input("Válassz!(1-3): \n"))

if bemenet == 2:
    print("---Információk---")
    print("infok.......................2")
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
        print(f"A karaktered neve: {self.nev}\nÉletereje: {self.eletero}\nSebzése: {self.sebzes}\nSzintje: {self.szint}\nPénze: {self.penz}")

class Ellenfel:
    def __init__(self, neve, elet, tamadas):
        self.neve = neve
        self.elet = int(elet)
        self.tamadas = int(tamadas)

    def adatok(self):
        print(f"Az ellenfél neve: {self.neve}\nÉletereje: {self.elet}\nSebzése: {self.tamadas}\n")




ellenfel1 = Ellenfel("Csontváz", 1500, 100)
ellenfel2 = Ellenfel("Zombi", 1212, 340)
ellenfel3 = Ellenfel("Sötét Lovag",30000, 1000)


def harc():
    ellenfelrandom = randint(1,3)
    if ellenfelrandom == 1:
        print(f"Az ellenfeled egy {ellenfel1.neve}")
    if ellenfelrandom == 2:
        print(f"Az ellenfeled egy {ellenfel2.neve}")
    if ellenfelrandom == 3:
        print(f"Az ellenfeled egy {ellenfel3.neve}")
    print("1 = támadás")
    print("2 = heal")
    print("3 = kihajolás")
    

def jatek():
    print("---Játék---")
    print("1 = Harc")
    print("2 = Tárgyaid")
    print("3 = ...")
    jatek_menu_valasztas = int(input())
    if jatek_menu_valasztas == 1:
        harc()

if bemenet == 1:
    print(f"A játék elkezdődött!\n")
    karakter = input(f"Add meg a hősöd nevét!")
    jatek()

karakter1 = Karakter(karakter, 15000, 300, 0, 500)
