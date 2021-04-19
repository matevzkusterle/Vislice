from model import Igra, nova_igra

datoteka = open('besede.txt', encoding='utf-8')
bazen_besed = []
for vrstica in datoteka:
    nova_vrstica = vrstica.strip('\n')
    bazen_besed.append(nova_vrstica)

import random
igra = Igra(random.choice(bazen_besed))

def pozdrav():
    print('----------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print('VISLICE')
    print('Pozdravljen v vislicah. Igra je sledeča: Če uganete geslo, ste zmagali, vkolikor pa nanizate več kot 10 nepravilnih ugibov, ste izgubili.')
    print('Geslo: {}'.format(igra.pravilni_del_gesla()))

def izpis_zmage():
    print(':D')
    print('Bravo, zmagal si!')
    
def izpis_poraza():
    print(':(')
    print('Preveč napak, izgubil si!')

def izpis_igre():
    print('')
    print('')
    print('Nepravilni ugibi: {}, ({}/10)'.format(igra.nepravilni_ugibi(), igra.stevilo_napak()))
    print('Uganjeno: {}'.format(igra.pravilni_del_gesla()))

def zahtevaj_vnos():
    print('-----------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print('Ugibaj črko:')
    ugib = input('>')
    return ugib

def pozeni_vmesnik():
    pozdrav()
    while not igra.zmaga() and not igra.poraz():
        igra.ugibaj(zahtevaj_vnos())
        izpis_igre()
    if igra.poraz():
        izpis_poraza()
    else:
        izpis_zmage()

pozeni_vmesnik()



