print("1 = Kezdés")
print("2 = Beállítások")
print("3 = Kilépés")

bemenet = int(input("Válassz!(1-3): "))

if bemenet == 2:
    print("1 = Könnyű")
    print("2 = Normál")
    print("3 = Nehéz")
    nehezseg = int(input("Válassz nehézséget!(1-3): "))
    
    if nehezseg == 1:
        print("Nehézség beállítva!(Könnyű)")
    if nehezseg == 2:
        print("Nehézség beállítva!(Normál)")
    if nehezseg == 3:
        print("Nehézség beállítva!(Nehéz)")
        
        
        
        
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
