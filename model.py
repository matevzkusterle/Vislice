
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
# Spremenljivke na začetnih vrednostih
STEVILO_DOVOLJENIH_NAPAK = 10

PRAVILNA_CRKA = '+'
PONOVLJENA_CRKA = 'o'
NAPACNA_CRKA = '-'

ZMAGA = 'W'
PORAZ = 'X'

#----------------------------------------------------------------------------------------------------------------------------------------------------------------
# Razred Igra
class Igra:
    def __init__(self, geslo, crke=[]):
        self.geslo = geslo.upper()
        self.crke = crke

    def napacne_crke(self):
        seznam = []
        for crka in self.crke:
            if crka not in self.geslo:
                seznam.append(crka)
        return seznam
    
    def pravilne_crke(self):
        seznam = []
        for crka in self.crke:
            if crka in self.geslo:
                seznam.append(crka)
        return seznam

    def stevilo_napak(self):
        return len(self.napacne_crke())
    
    def zmaga(self):
        for crka in self.geslo:
            if crka not in self.crke:
                return False
        return True

    def poraz(self):
        if len(self.napacne_crke()) > STEVILO_DOVOLJENIH_NAPAK:
            return True
        return False
    
    def pravilni_del_gesla(self):
        niz = ''
        for crka in self.geslo:
            if crka in self.crke:
                niz += ' ' + crka
            else:
                niz += ' _'
        return niz

    def nepravilni_ugibi(self):
        niz = ''
        for crka in self.napacne_crke():
            niz += crka + ' '
        return niz
    
    def ugibaj(self, crka):
        velika_crka = crka.upper()
        if velika_crka in self.crke:
            return PONOVLJENA_CRKA
        else:
            self.crke.append(velika_crka)
            if self.zmaga():
                return ZMAGA
            elif self.poraz():
                return PORAZ
            else:
                if velika_crka in self.napacne_crke():
                    return NAPACNA_CRKA
                else:
                    return PRAVILNA_CRKA

    def pravilen_odgovor(self):
        return str(self.geslo())

#----------------------------------------------------------------------------------------------------------------------------------------------------------------
# Tukaj ustvarimo vse možne besede
datoteka = open('besede.txt')
bazen_besed = []
for vrstica in datoteka:
    bazen_besed.append(vrstica)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------
# Funkcija, ki ustvari novo igro
import random

def nova_igra():
    geslo = random.choice(bazen_besed)
    return Igra(geslo)  
              