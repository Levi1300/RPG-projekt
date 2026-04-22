from random import randint

class Karakter:
    def __init__(self, nev, eletero, sebzes, szint, penz):
        self.nev = nev
        self.eletero = eletero
        self.sebzes = sebzes
        self.szint = szint
        self.penz = penz

class Ellenfel:
    def __init__(self, neve, elet, tamadas):
        self.neve = neve
        self.elet = elet
        self.tamadas = tamadas


ellenfelek = [
    Ellenfel("Csontváz", 1500, 100),
    Ellenfel("Zombi", 1212, 340),
    Ellenfel("Sötét Lovag", 3000, 500)
]


def harc(karakter):
    ellenfel = ellenfelek[randint(0, 2)]
    print(f"Az ellenfeled: {ellenfel.neve}")

    while ellenfel.elet > 0 and karakter.eletero > 0:
        print("\n1 = támadás")
        valasztas = int(input())

        if valasztas == 1:
            ellenfel.elet -= karakter.sebzes
            print(f"Sebzés: {karakter.sebzes}")

        if ellenfel.elet > 0:
            karakter.eletero -= ellenfel.tamadas
            print(f"Az ellenfél visszatámad: {ellenfel.tamadas}")

        print(f"Te HP: {karakter.eletero} | Ellenfél HP: {ellenfel.elet}")

    if karakter.eletero <= 0:
        print("Meghaltál!")
    else:
        print("Győztél!")


def jatek(karakter):
    while True:
        print("\n1 = Harc")
        print("2 = Kilépés")

        valasztas = int(input())

        if valasztas == 1:
            harc(karakter)
        elif valasztas == 2:
            break


# Főprogram
print("1 = Kezdés")
print("2 = Kilépés")

bemenet = int(input())

if bemenet == 1:
    nev = input("Neved: ")
    karakter = Karakter(nev, 1500, 200, 1, 100)
    jatek(karakter)