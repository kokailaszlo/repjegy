class JegyFoglalas:
    def __init__(self):
        self.foglalasok = {}

    def foglal(self, utas_nev, jarat):
        if not jarat:
            return "Hiba: A megadott járat nem található."
        self.foglalasok[utas_nev] = jarat
        return f"Sikeres foglalás, ár: {jarat.jegyar} Ft"

    def lemond(self, utas_nev):
        if utas_nev in self.foglalasok:
            del self.foglalasok[utas_nev]
            return f"{utas_nev} foglalása sikeresen törölve."
        return "Hiba: Nem található ilyen néven foglalás."

    def listaz(self):
        return [
            (nev, jarat.jaratszam, jarat.celallomas, jarat.jegyar)
            for nev, jarat in self.foglalasok.items()
        ]


