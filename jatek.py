1 == print("Kezdés")
2 == print("Beállítások")
3 == print("Kilépés")

bemenet = input("Válassz!(1-3)")

if bemenet == 1:
    pass
if bemenet == 2:
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

    