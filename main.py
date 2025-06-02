# -*- coding: utf-8 -*-

from jarat import BelfoldiJarat, NemzetkoziJarat
from legitarsasag import LegiTarsasag
from foglalasok import JegyFoglalas

def main():
    legitarsasag = LegiTarsasag("SkyFly")
    foglalas = JegyFoglalas()

    legitarsasag.hozzaad(BelfoldiJarat("b001", "Budapest"))
    legitarsasag.hozzaad(BelfoldiJarat("b002", "Debrecen"))
    legitarsasag.hozzaad(NemzetkoziJarat("n001", "London"))

    foglalas.foglal("Alka Ida", legitarsasag.keres("b001"))
    foglalas.foglal("Bak Ancsa", legitarsasag.keres("n001"))
    foglalas.foglal("Bor Ivó", legitarsasag.keres("b002"))
    foglalas.foglal("Csin Csilla", legitarsasag.keres("b001"))
    foglalas.foglal("Ebéd Elek", legitarsasag.keres("n001"))
    foglalas.foglal("Git Áron", legitarsasag.keres("b002"))

    while True:
        print("\n"+"-"*29)
        print("Repülőjegy Foglalási Rendszer")
        print("-"*29+"\n")
        print("a. Jegy foglalása")
        print("s. Foglalások listázása")
        print("d. Foglalás lemondása")
        print("q. Kilépés")

        valasztas = input("\nVálasszon egy műveletet: ")

        if valasztas == "a":
            print("\nElérhető járatok:")
            print("{:<11} {:<10} {:<11} {:<15}".format("Típus", "Járatszám", "Célállomás", "Jegyár (Ft)"))
            print("-" * 46)
            for jarat in legitarsasag.jaratok:
              tipus = "Belföldi" if isinstance(jarat, BelfoldiJarat) else "Nemzetközi"
              print("{:<11} {:<10} {:<11} {:<15}".format(tipus, jarat.jaratszam, jarat.celallomas, jarat.jegyar))

            nev = input("\nUtas neve: ")
            jaratszam = input("Járatszáma: ")
            jarat = legitarsasag.keres(jaratszam)
            print(foglalas.foglal(nev, jarat))

        elif valasztas == "d":
            nev = input("Utas neve: ")
            print(foglalas.lemond(nev))

        elif valasztas == "s":
            print("\nAktív foglalások:")
            foglalasok = foglalas.listaz()
            if not foglalasok:
                print("Nincs aktív foglalás.")
            else:
                print("{:<20} {:<12} {:<15} {:<10}".format("Név", "Járatszám", "Célállomás", "Jegyár (Ft)"))
                print("-" * 60)
                for nev, jaratszam, celallomas, jegyar in foglalasok:
                    print("{:<20} {:<12} {:<15} {:<10}".format(nev, jaratszam, celallomas, jegyar))
        elif valasztas == "q":
            print("Kilépés...")
            break

        else:
            print("\nHiba: Nem létező opció.\n")

if __name__ == "__main__":
    main()

