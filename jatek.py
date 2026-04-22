print("---RPG Projekt---")
print("1 = Játék")
print("2 = Információk")
print("3 = Kilépés")
print("-----------------")

bemenet = int(input("Válassz!(1-3): \n"))

 
class Karakter:
    def __init__(self, nev, eletero, sebzes, kepesseg):
        self.nev = nev
        self.eletero = eletero
        self.sebzes = sebzes
        self.kepesseg = kepesseg

    def adatok(self):
        print(f"A jelenlegi Karaktered: {self.nev}\nÉletereje: {self.eletero}\nSebzése: {self.sebzes}\nképessége: {self.kepesseg}")


if bemenet == 1:
    print(f"A játék elkezdődött!\n")
    karakter = str(input("Add meg a hősöd nevét!"))


karakter1 = Karakter(karakter, 150, 30, "Nincs")




