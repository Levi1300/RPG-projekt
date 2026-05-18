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
        print(f"Pénz: {self.penz}$")

    def gyogyitas(self):
        print(f"\n💚 Gyógyítás (1 pénz = 5 HP)")
        print(f"Jelenlegi HP: {self.eletero}/{self.max_eletero}")
        print(f"Pénzed: {self.penz}$")

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

        self.eletero = min(
            self.max_eletero,
            self.eletero + gyogyitas
        )

        self.penz -= koltes

        print(f"💚 Gyógyultál: {gyogyitas} HP-t")
        print(f"Új HP: {self.eletero}/{self.max_eletero}")
        print(f"Maradék pénzed: {self.penz}$")

    def fejlesztes(self):
        while True:
            print("\n---Fejlesztés---")
            print(f"Összes pénzed: {self.penz}$")
            print(f"1 = Életerő növelés (+200 HP) - {self.hp_ar}$")
            print(f"2 = Sebzés növelés (+30) - {self.sebzes_ar}$")
            print("3 = Vissza")

            val = input("Válassz: ")

            if val == "1":

                if self.penz >= self.hp_ar:
                    self.penz -= self.hp_ar
                    self.max_eletero += 200
                    self.eletero += 200
                    self.hp_ar += 15

                    print("❤️ Életerő növelve!")

                else:
                    print("Nincs elég pénzed!")

            elif val == "2":

                if self.penz >= self.sebzes_ar:
                    self.penz -= self.sebzes_ar
                    self.sebzes += 30
                    self.sebzes_ar += 15

                    print("⚔️ Sebzés növelve!")

                else:
                    print("Nincs elég pénzed!")

            elif val == "3":
                break

            else:
                print("Hibás választás!")

    def gambling(self):
        print(f"\nPénzed: {self.penz}$")

        try:
            felrak = int(input("Mennyi pénzt raksz?: "))
        except:
            print("Hibás szám!")
            return

        if felrak <= 0:
            print("Hibás összeg!")
            return

        if felrak > self.penz:
            print("Nincs ennyi pénzed!")
            return

        self.penz -= felrak

        print("1 = Fej")
        print("2 = Írás")

        try:
            sajatszam = int(input("Válassz: "))
        except:
            print("Hibás választás!")
            return

        if sajatszam not in [1, 2]:
            print("Hibás választás!")
            return

        gamblingszam = randint(1, 2)

        if sajatszam == gamblingszam:
            nyeremeny = felrak * 2
            self.penz += nyeremeny

            print(f"🎉 Nyertél! +{nyeremeny}$")

        else:
            print(f"❌ Vesztettél! Maradék pénzed: {self.penz}$")

    def parancsok(self):
        jelszo = "12345689"

        bevitel = input("Add meg a jelszót!: ")

        if bevitel != jelszo:
            print("Rossz jelszó!")
            return

        print("\n---Parancsok---")
        print("1 = Pénz addolás")
        print("2 = Sebzés növelés")
        print("3 = HP növelés")

        try:
            valasztas = int(input("Válassz!: "))
        except:
            print("Hibás választás!")
            return

        if valasztas == 1:
            penzadd = int(input("Mennyi pénzt?: "))
            self.penz += penzadd

        elif valasztas == 2:
            sebzesadd = int(input("Mennyi sebzés?: "))
            self.sebzes += sebzesadd

        elif valasztas == 3:
            hpadd = int(input("Mennyi HP?: "))
            self.max_eletero += hpadd
            self.eletero += hpadd

        else:
            print("Hibás választás!")

    

    def mentes(self, legyozott):

        with open("mentes.txt", "w", encoding="utf-8") as fajl:

            fajl.write(self.nev + "\n")
            fajl.write(str(self.eletero) + "\n")
            fajl.write(str(self.max_eletero) + "\n")
            fajl.write(str(self.sebzes) + "\n")
            fajl.write(str(self.szint) + "\n")
            fajl.write(str(self.penz) + "\n")
            fajl.write(str(self.hp_ar) + "\n")
            fajl.write(str(self.sebzes_ar) + "\n")
            fajl.write(str(legyozott) + "\n")

        print("💾 Játék elmentve!")

    def betoltes(self):
        try:
            with open("mentes.txt", "r", encoding="utf-8") as fajl:
                self.nev = fajl.readline().strip()
                self.eletero = int(fajl.readline())
                self.max_eletero = int(fajl.readline())
                self.sebzes = int(fajl.readline())
                self.szint = int(fajl.readline())
                self.penz = int(fajl.readline())
                self.hp_ar = int(fajl.readline())
                self.sebzes_ar = int(fajl.readline())
                legyozott = int(fajl.readline())

            print("📂 Mentés betöltve!")
            return legyozott
        except:
            print("Nincs mentés!")
            return 0

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
    ("Goblin", 450, 70),
    ("Vérfarkas", 350, 45),
    ("Hegyi Gólem", 1000, 100),
    ("Fekete Mágus", 550, 60),
    ("Iszapjáró", 600, 55)
]

boss_adatok = ("Sötét Lovag", 5000, 300)
boss2_adatok = ("Tűz Sárkány", 9000, 450)
boss3_adatok = ("A Mocsári Rém", 14000, 600)
boss4_adatok = ("Az Örök Sötétség Ura", 20000, 1000)


def penz_jutalom(ellenfel):

    alap = (ellenfel.elet // 10) + (ellenfel.tamadas * 2)

    bonusz = randint(50, 150)

    return alap + bonusz


def uj_ellenfel(legyozott):

    i = randint(0, len(ellenfel_adatok) - 1)

    nev, elet, tamadas = ellenfel_adatok[i]

    szorzo = 1 + (legyozott // 5) * 0.25

    elet = int(elet * szorzo)
    tamadas = int(tamadas * szorzo)

    if legyozott >= 15:
        elet += 500
        tamadas += 80

    if legyozott >= 30:
        elet += 1500
        tamadas += 200

    if legyozott >= 50:
        elet += 3000
        tamadas += 350

    if legyozott >= 100:
        elet += 7000
        tamadas += 700

    return Ellenfel(nev, elet, tamadas)


def uj_boss():
    return Ellenfel(*boss_adatok)


def uj_boss2():
    return Ellenfel(*boss2_adatok)


def uj_boss3():
    return Ellenfel(*boss3_adatok)


def uj_boss4():
    return Ellenfel(*boss4_adatok)


def harc(jatekos, ellenfel):

    print(f"\n⚔️ Harc indul! Ellenfél: {ellenfel.neve}")

    input("Nyomj ENTER-t a kezdéshez...")

    kor = 1

    while jatekos.eletero > 0 and ellenfel.elet > 0:

        print(f"\n--- {kor}. kör ---")

        sebzes = randint(
            max(0, jatekos.sebzes - 20),
            jatekos.sebzes + 20
        )

        ellenfel.elet -= sebzes

        print(f"🧍 Te támadsz: {sebzes} sebzés")
        print(f"{ellenfel.neve} HP: {max(0, ellenfel.elet)}")

        if ellenfel.elet <= 0:

            print(f"\n✅ Legyőzted: {ellenfel.neve}!")

            jutalom = penz_jutalom(ellenfel)

            jatekos.penz += jutalom
            jatekos.szint += 1

            print(f"💰 Jutalom: {jutalom}$")
            print(f"⭐ Szintlépés! Új szint: {jatekos.szint}")

            return True

        input("Nyomj ENTERT a folytatáshoz...")

        sebzes = randint(
            max(0, ellenfel.tamadas - 20),
            ellenfel.tamadas + 20
        )

        jatekos.eletero -= sebzes

        print(f"\n👹 {ellenfel.neve} támad: {sebzes} sebzés")
        print(f"❤️ HP-d: {max(0, jatekos.eletero)}")

        if jatekos.eletero <= 0:
            print("\n💀 Meghaltál!")
            return False

        input("Nyomj ENTERT a következő körhöz...")

        kor += 1


def jatek(jatekos):

    legyozott = 0

    while True:

        if jatekos.eletero <= 0:
            print("\n💀 Meghaltál!")
            break

        print("\n---Játék---")
        print("1 = Harc")
        print("2 = Karakter adatok")
        print("3 = Gyógyítás")
        print("4 = Fejlesztés")
        print("5 = Gambling")
        print("6 = Parancsok")
        print("7 = Mentés")
        print("8 = Betöltés")
        print("9 = Kilépés")

        valasztas = input("Válassz: ")

        if valasztas == "1":

            # Boss figyelmeztetések
            if legyozott == 14:
                print("⚠️ Következő harc: Sötét Lovag! (BOSS)")

            elif legyozott == 29:
                print("⚠️ Következő harc: Tűz Sárkány! (BOSS)")

            elif legyozott == 49:
                print("⚠️ Következő harc: Mocsári Rém! (BOSS)")

            elif legyozott == 99:
                print("⚠️ Következő harc: Az Örök Sötétség Ura! (BOSS)")

            # Bossok
            if legyozott == 15:

                boss = uj_boss()

                if harc(jatekos, boss):
                    print("\n🏆 Legyőzted a SÖTÉT LOVAGOT! Jutalom: 1500$")
                    jatekos.penz += 1500
                    legyozott += 1

                continue

            elif legyozott == 30:

                boss = uj_boss2()

                if harc(jatekos, boss):
                    print("\n🏆 Legyőzted a TŰZ SÁRKÁNYT! Jutalom: 3000$")
                    jatekos.penz += 3000
                    legyozott += 1

                continue

            elif legyozott == 50:

                boss = uj_boss3()

                if harc(jatekos, boss):
                    print("\n🏆 Legyőzted a MOCSÁRI RÉMET! Jutalom: 5000$")
                    jatekos.penz += 5000
                    legyozott += 1

                continue

            elif legyozott == 100:

                boss = uj_boss4()

                if harc(jatekos, boss):

                    print("\n🏆 Legyőzted AZ ÖRÖK SÖTÉTSÉG URÁT! Jutalom: 10000$")
                    print("🔥 A játék folytatódik!")

                    jatekos.penz += 10000
                    legyozott += 1

                continue

            ellenfel = uj_ellenfel(legyozott)

            if harc(jatekos, ellenfel):
                legyozott += 1

        elif valasztas == "2":
            jatekos.adatok()

        elif valasztas == "3":
            jatekos.gyogyitas()

        elif valasztas == "4":
            jatekos.fejlesztes()

        elif valasztas == "5":
            jatekos.gambling()

        elif valasztas == "6":
            jatekos.parancsok()

        elif valasztas == "7":
            jatekos.mentes(legyozott)

        elif valasztas == "8":
            legyozott = jatekos.betoltes()

        elif valasztas == "9":
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

        karakter = Karakter(
            nev,
            2000,
            200,
            1,
            500
        )

        jatek(karakter)

    elif bemenet == "2":

        print("\nEz egy RPG játék fejlesztés rendszerrel.")
        print("Harcolj, fejleszd magad és győzd le a bossokat!")
        print("Készítette: Öskü Levente, Máté Szabolcs")

    elif bemenet == "3":
        print("Kilépés...")
        break

    else:
        print("Hibás választás!")