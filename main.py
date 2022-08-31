class Irasymas:
    def __init__(self, tipas, suma):
        self.tipas = tipas
        self.suma = suma

    def __str__(self):
        return f"{self.tipas}: {self.suma}"

class Biudzetas:
    def __init__(self):
        self.zurnalas = []

    def pajamu_pridejimas(self, suma):
        irasas = Irasymas("Pajamos: ", suma)
        self.zurnalas.append(irasas)

    def pajamu_atemimas(self, suma):
        irasas = Irasymas("Islaidos: ", suma)
        self.zurnalas.append(irasas)

    def balansas(self):
        bendra_suma = 0
        for irasas in self.zurnalas:
            if irasas.tipas == "Pajamos":
                bendra_suma += irasas.suma
            if irasas.tipas == "Islaidos":
                bendra_suma -= irasas.suma
        print(bendra_suma)
        return bendra_suma

    def ataskaita(self):
        print("Ataskaita: ")
        for irasas in self.zurnalas:
            print(irasas)
        print("            ")

biudzetas = Biudzetas()

while True:
    veiksmas = int(input("1.iveskite pajamas"
                         "\n2.iveskite islaidas"
                         "\n3.balansas"
                         "\n4.ataskaita"
                         "\n5.baigti operacija"
                         "\n "))

    if veiksmas == 1:
        suma = float(input("Iveskite pajamu suma: "))
        biudzetas.pajamu_pridejimas(suma)
    if veiksmas == 2:
        suma = float(input("Iveskite islaidu suma: "))
        biudzetas.pajamu_atemimas(suma)
    if veiksmas == 3:
        biudzetas.balansas()
    if veiksmas == 4:
        biudzetas.ataskaita()
    if veiksmas == 5:
        print("Operacija baigta.")
        break
