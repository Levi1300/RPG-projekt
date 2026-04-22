print("---RPG Projekt---")
print("1 = Játék")
print("2 = Információk")
print("3 = Kilépés")
print("-----------------\n")

bemenet = int(input("Válassz!(1-3): \n"))

<<<<<<< HEAD
if bemenet == 2:
    print("Információk")
    print("infok")
    print("-----------------\n")
    print("---RPG Projekt---")
    print("1 = Kezdés")
    print("2 = Információk")
    print("3 = Kilépés")
    print("-----------------")
    bemenet = int(input("Válassz!(1-3): \n"))

=======
>>>>>>> b0b98fc4b82b8585559351774eb1cb1e373ccf3c
 
class Karakter:
    def __init__(self, nev, eletero, sebzes, kepesseg):
        self.nev = nev
        self.eletero = eletero
        self.sebzes = sebzes
        self.kepesseg = kepesseg

    def adatok(self):
<<<<<<< HEAD
        print(f"A jelenlegi Karaktered: {self.nev}\nÉletereje: {self.eletero}\nSebzése: {self.sebzes}\nképessége: {self.kepesseg}\nPénze: {self.penz}")

karakter1 = Karakter("Harcos", 150, 30, "Nincs", 500)
karakter2 = Karakter("Varázsló", 120, 40, "Heal", 450)
karakter3 = Karakter("Íjász", 80, 45, "Nincs", 400)

karakterek = [karakter1,karakter2,karakter3]
=======
        print(f"A jelenlegi Karaktered: {self.nev}\nÉletereje: {self.eletero}\nSebzése: {self.sebzes}\nképessége: {self.kepesseg}")
>>>>>>> b0b98fc4b82b8585559351774eb1cb1e373ccf3c


if bemenet == 1:
    print(f"A játék elkezdődött!\n")
<<<<<<< HEAD
    karakter = input(f"Válaszd ki a Karaktered az alábbiak közül:\n{karakter1.nev}\n{karakter2.nev}\n{karakter3.nev}\n")

if karakter == karakter1.nev:
    karakter1.adatok()
elif karakter == karakter2.nev:
    karakter2.adatok()
elif karakter == karakter3.nev:
    karakter3.adatok()


=======
    karakter = str(input("Add meg a hősöd nevét!"))


karakter1 = Karakter(karakter, 150, 30, "Nincs")




>>>>>>> b0b98fc4b82b8585559351774eb1cb1e373ccf3c
