class Tarsasag:
    def __init__(self, nev):
        self.nev = nev
        self.jaratok = []

    def hozzaad(self, jarat):
        self.jaratok.append(jarat)

    def keres(self, jaratszam):
        for j in self.jaratok:
            if j.jaratszam == jaratszam:
                return j
        return None

#    def listaz(self):
#        return [jarat.info() for jarat in self.jaratok]
