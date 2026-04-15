kezdes = print("Kezdés")
beallitasok = print("Beállítások")
kilepes = print("Kilépés")

bemenet = input("Válassz!")
if bemenet == kezdes:
    pass
if bemenet == beallitasok:
    input("Válassz nehézséget!: ")
    print("Könnyű")
    print("Normál")
    print("Nehéz")

    nehezseg = input("Válassz nehézséget!: ")
    print("Nehézség")


class Karakterek:
    def __init__(self, nev, eletero, sebzes, kepesseg):
        self.nev = nev
        self.eletero = eletero
        self.sebzes = sebzes


karakter1 = Karakterek("Harcos", 150, 30, "Nincs")
karakter2 = Karakterek("Varázsló", 120, 40, "Heal")
karakter3 = Karakterek("Íjász", 80, 45, "Nincs")

karakterek = [karakter1,karakter2,karakter3]

