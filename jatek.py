print("---RPG Projekt---")
print("1 = Kezdés")
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




karakter1 = Karakter("Harcos", 150, 30, "Nincs")
karakter2 = Karakter("Varázsló", 120, 40, "Heal")
karakter3 = Karakter("Íjász", 80, 45, "Nincs")

karakterek = [karakter1,karakter2,karakter3]


if bemenet == 1:
    print(f"A játék elkezdődött!\n")
    karakter = input(f"Válaszd ki a Karaktered az alábbiak közül:\n{karakter1.nev}\n{karakter2.nev}\n{karakter3.nev}\n")

if karakter == karakter1.nev:
    karakter1.adatok()
elif karakter == karakter2.nev:
    karakter2.adatok()
elif karakter == karakter3.nev:
    karakter3.adatok()


