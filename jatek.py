from random import randint

print("\n---RPG Projekt---")

class Karakter:
    def __init__(self, nev, eletero, sebzes, szint, penz):
        self.nev = nev
        self.max_eletero = eletero
        self.eletero = eletero
        self.sebzes = sebzes
        self.szint = szint
        self.penz = penz

    def adatok(self):
        print(f"\n---Karakter adatok---")
        print(f"Név: {self.nev}")
        print(f"Életerő: {self.eletero}/{self.max_eletero}")
        print(f"Sebzés: {self.sebzes}")
        print(f"Szint: {self.szint}")
        print(f"Pénz: {self.penz}")

    def gyogyitas(self):
        if self.penz >= 50:
            self.eletero = self.max_eletero
            self.penz -= 50
            print("💚 Teljesen meggyógyultál!")
        else:
            print("Nincs elég pénzed!")

    def fejlesztes(self):
        while True:
            print("\n---Fejlesztés---")
            print("1 = Életerő növelés (+200 HP) - 100 pénz")
            print("2 = Sebzés növelés (+30) - 100 pénz")
            print("3 = Vissza")

            val = input("Válassz: ")

            if val == "1":
                if self.penz >= 100:
                    self.max_eletero += 200
                    self.eletero = self.max_eletero
                    self.penz -= 100
                    print("❤️ Életerő növelve!")
                else:
                    print("Nincs elég pénzed!")

            elif val == "2":
                if self.penz >= 100:
                    self.sebzes += 30
                    self.penz -= 100
                    print("⚔️ Sebzés növelve!")
                else:
                    print("Nincs elég pénzed!")

            elif val == "3":
                break
            else:
                print("Hibás választás!")


class Ellenfel:
    def __init__(self, neve, elet, tamadas):
        self.neve = neve
        self.elet = elet
        self.tamadas = tamadas



ellenfel_adatok = [
    ("Csontváz", 500, 50),
    ("Zombi", 800, 80),
    ("Ork", 1200, 120),
    ("Bandita", 900, 100),
    ("Óriáspók", 700, 90)
]

boss_adat = ("Sötét Lovag", 5000, 300)


def uj_ellenfel():
    i = randint(0, len(ellenfel_adatok) - 1)
    nev, elet, tamadas = ellenfel_adatok[i]
    return Ellenfel(nev, elet, tamadas)


def uj_boss():
    nev, elet, tamadas = boss_adat
    return Ellenfel(nev, elet, tamadas)


def harc(jatekos, ellenfel):
    print(f"\n⚔️ Harc indul! Ellenfél: {ellenfel.neve}")

    while jatekos.eletero > 0 and ellenfel.elet > 0:

        sebzes = max(0, randint(jatekos.sebzes - 20, jatekos.sebzes + 20))
        ellenfel.elet -= sebzes
        print(f"Te támadsz: {sebzes}")

        if ellenfel.elet <= 0:
            print(f"Legyőzted: {ellenfel.neve}!")
            jatekos.penz += 100
            jatekos.szint += 1
            return True

        sebzes = max(0, randint(ellenfel.tamadas - 20, ellenfel.tamadas + 20))
        jatekos.eletero -= sebzes
        print(f"{ellenfel.neve} támad: {sebzes}")
        print(f"HP: {max(0, jatekos.eletero)}")

        if jatekos.eletero <= 0:
            print("💀 Meghaltál!")
            return False


def jatek(jatekos):
    legyozott = 0

    while jatekos.eletero > 0:
        print("\n---Játék---")
        print("1 = Harc")
        print("2 = Karakter adatok")
        print("3 = Gyógyítás (50 pénz)")
        print("4 = Fejlesztés")
        print("5 = Kilépés")

        valasztas = input("Válassz: ")

        if valasztas == "1":
            if legyozott >= 5:
                boss = uj_boss()
                if harc(jatekos, boss):
                    print("\n🏆 Megölted a BOSST! Nyertél!")
                    break
                else:
                    break
            else:
                ellenfel = uj_ellenfel()
                if harc(jatekos, ellenfel):
                    legyozott += 1
                else:
                    break

        elif valasztas == "2":
            jatekos.adatok()

        elif valasztas == "3":
            jatekos.gyogyitas()

        elif valasztas == "4":
            jatekos.fejlesztes()

        elif valasztas == "5":
            print("Kilépés...")
            break

        else:
            print("Hibás választás!")



while True:
    print("\n---Főmenü---")
    print("1 = Kezdés")
    print("2 = Információk")
    print("3 = Kilépés")

    bemenet = input("Válassz (1-3): ")

    if bemenet == "1":
        nev = input("Add meg a hősöd nevét: ")
        karakter = Karakter(nev, 2000, 200, 1, 500)
        jatek(karakter)

    elif bemenet == "2":
        print("\nEz egy RPG játék fejlesztés rendszerrel.")
        print("Menj a '4 = Fejlesztés' menübe játék közben!")

    elif bemenet == "3":
        print("Kilépés...")
        break

    else:
        print("Hibás választás!")
