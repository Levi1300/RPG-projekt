from random import randint, choice

print("\n---RPG Projekt---")

class Karakter:
    def __init__(self, nev, eletero, sebzes, szint, penz):
        self.nev = nev
        self.eletero = eletero
        self.sebzes = sebzes
        self.szint = szint
        self.penz = penz

    def adatok(self):
        print(f"\n---Karakter adatok---")
        print(f"Név: {self.nev}")
        print(f"Életerő: {self.eletero}")
        print(f"Sebzés: {self.sebzes}")
        print(f"Szint: {self.szint}")
        print(f"Pénz: {self.penz}")

class Ellenfel:
    def __init__(self, neve, elet, tamadas):
        self.neve = neve
        self.elet = elet
        self.tamadas = tamadas


ellenfelek = [
    Ellenfel("Csontváz", 500, 50),
    Ellenfel("Zombi", 800, 80),
    Ellenfel("Ork", 1200, 120),
    Ellenfel("Bandita", 900, 100),
    Ellenfel("Óriáspók", 700, 90)
]


boss = Ellenfel("Sötét Lovag", 5000, 300)

def harc(jatekos, ellenfel):
    print(f"\n⚔️ Harc indul! Ellenfél: {ellenfel.neve}")

    while jatekos.eletero > 0 and ellenfel.elet > 0:
        
        sebzes = randint(jatekos.sebzes - 20, jatekos.sebzes + 20)
        ellenfel.elet -= sebzes
        print(f"Te támadsz: {sebzes} sebzés")

        if ellenfel.elet <= 0:
            print(f"Legyőzted: {ellenfel.neve}!")
            jatekos.penz += 100
            jatekos.szint += 1
            return True

        
        sebzes = randint(ellenfel.tamadas - 20, ellenfel.tamadas + 20)
        jatekos.eletero -= sebzes
        print(f"{ellenfel.neve} támad: {sebzes} sebzés")

        print(f"HP: {jatekos.eletero}")

        if jatekos.eletero <= 0:
            print("Meghaltál!")
            return False

def jatek(jatekos):
    legyozott = 0

    while jatekos.eletero > 0:
        print("\n---Játék---")
        print("1 = Harc")
        print("2 = Karakter adatok")
        print("3 = Kilépés")

        valasztas = input("Válassz: ")

        if valasztas == "1":
            
            if legyozott >= 5:
                if harc(jatekos, boss):
                    print("\n🏆 Megölted a BOSST! Nyertél!")
                    break
                else:
                    break
            else:
                ellenfel = choice(ellenfelek)
                if harc(jatekos, ellenfel):
                    legyozott += 1
                else:
                    break

        elif valasztas == "2":
            jatekos.adatok()

        elif valasztas == "3":
            print("Kilépés...")
            break

print("---RPG PROJEKT---")
print("1 = Kezdés")
print("2 = Kilépés")
print("-----------------")

bemenet = input("Válassz (1-3): ")

if bemenet == 1:
    nev = input("Neved: ")
    karakter = Karakter(nev, 1500, 200, 1, 100)
    jatek(karakter)
    
