print("---RPG Projekt---")
print("1 = Kezdés")
print("2 = Információk")
print("3 = Kilépés")
print("-----------------")

bemenet = int(input("Válassz!(1-3): \n"))

<<<<<<< Updated upstream
 
=======


          
>>>>>>> Stashed changes
class Karakter:
    def __init__(self, nev, eletero, sebzes, kepesseg, penz):
        self.nev = nev
        self.eletero = eletero
        self.sebzes = sebzes
        self.kepesseg = kepesseg
        self.penz = penz

    def adatok(self):
        print(f"A jelenlegi Karaktered: {self.nev}\nÉletereje: {self.eletero}\nSebzése: {self.sebzes}\nképessége: {self.kepesseg}\nPénze: {self.penz}")

<<<<<<< HEAD
karakter1 = Karakter("Harcos", 150, 30, "Nincs", 500)
karakter2 = Karakter("Varázsló", 120, 40, "Heal", 450)
karakter3 = Karakter("Íjász", 80, 45, "Nincs", 400)
=======



karakter1 = Karakter("Harcos", 150, 30, "Nincs")
karakter2 = Karakter("Varázsló", 120, 40, "Heal")
karakter3 = Karakter("Íjász", 80, 45, "Nincs")
>>>>>>> d98942aaa41b372f77ff1f48cd0f65537a3a1a40

karakterek = [karakter1,karakter2,karakter3]


<<<<<<< Updated upstream
if bemenet == 1:
    print(f"A játék elkezdődött!\n")
    karakter = input(f"Válaszd ki a Karaktered az alábbiak közül:\n{karakter1.nev}\n{karakter2.nev}\n{karakter3.nev}\n")

if karakter == karakter1.nev:
    karakter1.adatok()
elif karakter == karakter2.nev:
    karakter2.adatok()
elif karakter == karakter3.nev:
    karakter3.adatok()
=======
def karakterek1(self):
    for karakterek1 in karakterek:
        print(karakterek.nev)


if bemenet == 1:
    print(f"A játék elkezdődött. Válaszd ki a Karaktered az alábbiak közül: {karakter1}")
    input()
>>>>>>> Stashed changes


<<<<<<< HEAD

=======
>>>>>>> d98942aaa41b372f77ff1f48cd0f65537a3a1a40
