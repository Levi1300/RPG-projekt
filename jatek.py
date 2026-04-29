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
        self.hp_ar = 100
        self.sebzes_ar = 100

    def adatok(self):
        print(f"\n---Karakter adatok---")
        print(f"Név: {self.nev}")
        print(f"Életerő: {self.eletero}/{self.max_eletero}")
        print(f"Sebzés: {self.sebzes}")
        print(f"Szint: {self.szint}")
        print(f"Pénz: {self.penz}")

    def gyogyitas(self):
        print(f"\n💚 Gyógyítás (1 pénz = 5 HP)")
        print(f"Jelenlegi HP: {self.eletero}/{self.max_eletero}")
        print(f"Pénzed: {self.penz}")

        if self.penz <= 0:
            print("Nincs pénzed!")
            return

        try:
            koltes = int(input("Mennyit költesz gyógyításra?: "))
        except:
            print("Hibás szám!")
            return

        if koltes <= 0:
            print("Adj meg pozitív számot!")
            return

        if koltes > self.penz:
            print("Nincs ennyi pénzed!")
            return

        gyogyitas = koltes * 5
        self.eletero += gyogyitas

        if self.eletero > self.max_eletero:
            self.eletero = self.max_eletero

        self.penz -= koltes

        print(f"💚 Gyógyultál: {gyogyitas} HP-t")
        print(f"Új HP: {self.eletero}/{self.max_eletero}")

    def fejlesztes(self):
        while True:
            print("\n---Fejlesztés---")
            print(f"1 = Életerő növelés (+200 HP) - {self.hp_ar} pénz")
            print(f"2 = Sebzés növelés (+30) - {self.sebzes_ar} pénz")
            print("3 = Vissza")

            val = input("Válassz: ")

            if val == "1":
                if self.penz >= self.hp_ar:
                    self.penz -= self.hp_ar
                    self.max_eletero += 200
                    self.hp_ar += 10
                    print(f"❤️ Életerő növelve! Új ár: {self.hp_ar}")
                else:
                    print("Nincs elég pénzed!")

            elif val == "2":
                if self.penz >= self.sebzes_ar:
                    self.penz -= self.sebzes_ar
                    self.sebzes += 30
                    self.sebzes_ar += 10
                    print(f"⚔️ Sebzés növelve! Új ár: {self.sebzes_ar}")
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
    ("Óriáspók", 700, 90),
    ("Goblin", 450, 70)
]

boss_adatok = ("Sötét Lovag", 5000, 300)
boss2_adatok = ("Tűz Sárkány", 9000, 450)


def uj_ellenfel(legyozott):
    i = randint(0, len(ellenfel_adatok) - 1)
    nev, elet, tamadas = ellenfel_adatok[i]

    # erősödés
    if legyozott >= 15:
        elet = int(elet * 1.5)
        tamadas = int(tamadas * 1.5)

    if legyozott >= 30:
        elet = int(elet * 1.5)
        tamadas = int(tamadas * 1.5)

    return Ellenfel(nev, elet, tamadas)


def uj_boss():
    nev, elet, tamadas = boss_adatok
    return Ellenfel(nev, elet, tamadas)


def uj_boss2():
    nev, elet, tamadas = boss2_adatok
    return Ellenfel(nev, elet, tamadas)


def harc(jatekos, ellenfel):
    print(f"\n⚔️ Harc indul! Ellenfél: {ellenfel.neve}")
    input("Nyomj ENTER-t a kezdéshez...")

    kor = 1

    while jatekos.eletero > 0 and ellenfel.elet > 0:
        print(f"\n--- {kor}. kör ---")

        sebzes = max(0, randint(jatekos.sebzes - 20, jatekos.sebzes + 20))
        ellenfel.elet -= sebzes
        print(f"🧍 Te támadsz: {sebzes} sebzés")
        print(f"{ellenfel.neve} HP: {max(0, ellenfel.elet)}\n")

        if ellenfel.elet <= 0:
            print(f"\n✅ Legyőzted: {ellenfel.neve}!")
            jatekos.penz += randint(150, 450)
            jatekos.szint += 1
            return True

        input("Nyomj ENTERT a folytatáshoz...\n")

        sebzes = max(0, randint(ellenfel.tamadas - 20, ellenfel.tamadas + 20))
        jatekos.eletero -= sebzes
        print(f"👹 {ellenfel.neve} támad: {sebzes} sebzés")
        print(f"❤️ HP-d: {max(0, jatekos.eletero)}\n")

        if jatekos.eletero <= 0:
            print("\n💀 Meghaltál!")
            return False

        input("Nyomj ENTERT a következő körhöz...")
        kor += 1


def jatek(jatekos):
    legyozott = 0

    while jatekos.eletero > 0:
        print("\n---Játék---")
        print("1 = Harc")
        print("2 = Karakter adatok")
        print("3 = Gyógyítás")
        print("4 = Fejlesztés")
        print("5 = Kilépés")

        valasztas = input("Válassz: ")

        if valasztas == "1":

            if legyozott == 15:
                boss = uj_boss()
                if harc(jatekos, boss):
                    print("\n🏆 Megölted a SÖTÉT LOVAGOT! Jutalom: 1500$")
                    jatekos.penz += 1500
                    legyozott += 1

            elif legyozott == 30:
                boss = uj_boss2()
                if harc(jatekos, boss):
                    print("\n🐉 Megölted a TŰZ SÁRKÁNYT! Jutalom: 3000$")
                    jatekos.penz += 3000
                    legyozott += 1

            else:
                ellenfel = uj_ellenfel(legyozott)
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
        print("készítette: Öskü Levente, Máté Szabolcs")

    elif bemenet == "3":
        print("Kilépés...")
        break

    else:
        print("Hibás választás!")