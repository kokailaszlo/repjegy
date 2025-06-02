from abc import ABC, abstractmethod

class Jarat(ABC):
    def __init__(self, jaratszam, celallomas, jegyar):
        self.jaratszam = jaratszam
        self.celallomas = celallomas
        self.jegyar = jegyar

    @abstractmethod
    def info(self):
        pass


class Belfoldi(Jarat):
    def __init__(self, jaratszam, celallomas):
        super().__init__(jaratszam, celallomas, jegyar=10000)

    def info(self):
        return f"Belföldi járat: {self.jaratszam} - {self.celallomas} - Ár: {self.jegyar} Ft"


class Nemzetkozi(Jarat):
    def __init__(self, jaratszam, celallomas):
        super().__init__(jaratszam, celallomas, jegyar=40000)

    def info(self):
        return f"Nemzetközi járat: {self.jaratszam} - {self.celallomas} - Ár: {self.jegyar} Ft"
