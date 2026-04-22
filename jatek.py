
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
    def __init__(self, nev, eletero, sebzes, kepesseg, penz):
        self.nev = nev
        self.eletero = eletero
        self.sebzes = sebzes
        self.kepesseg = kepesseg
        self.penz = penz

    def adatok(self):
        print(f"A jelenlegi Karaktered: {self.nev}\nÉletereje: {self.eletero}\nSebzése: {self.sebzes}\nképessége: {self.kepesseg}\nPénze: {self.penz}")

if bemenet == 1:
    print(f"A játék elkezdődött!\n")
    karakter = input(f"Add meg a hősöd nevét!")

karakter1 = Karakter(karakter, 150, 30, "Nincs", 500)

