import json
import sys

# Tässä määritellään funktio keskustelun lataukseen json-tiedostosta
def keskustelupaketin_lataaminen(tiedosto):
    try:
        with open(tiedosto, 'r') as file:
            print("Ladataan keskusteluja...")
            return json.load(file)
    except FileNotFoundError:
        print("Virhe: En löydä haluamaanne tiedostoa, kokeillaas uudestaan.")
    return None
    
# Tässä määritellään funktio joka hoitaa keskustelua ja mahdolliset valinnat seikkailun sisällä
def valinta_ja_tulostus(kohta):
    while kohta:
        print(kohta['teksti'])

        if 'valinnat' in kohta and kohta['valinnat']:
            print("\nVaihtoehdot;")
            for i, valinta in enumerate(kohta['valinnat'], 1):
                print(f"{i}. {valinta['teksti']}")

            while True:
                try:
                    syote = input("Tee valintasi numeroina: ").strip()
                    valittu_numero = int(syote)
                    if 1 <= valittu_numero <= len(kohta['valinnat']):
                        kohta = kohta['valinnat'][valittu_numero - 1]['seuraava']
                        return kohta  # Palautetaan seuraava kohta
                    else:
                        print("Valitse numero olemassa olevista vaihtoehdoista (jotka voivat olla vähissä).")
                except ValueError:
                    print(f"\"{syote}\" tää ei ole kelvollinen syöttö, testataas uudelleen...\n")

# Pääohjelma jossa käyttäjä voi valita tiedoston komentoriviltä ja joka kiittää lopuksi ohjelman käytöstä
def seikkailu():
    if len(sys.argv) != 2:
        print("Virhe: Anna tiedostonimi uusiksi, kiitos.")
        return

    tiedosto = sys.argv[1]
    keskustelu = keskustelupaketin_lataaminen(tiedosto)
    if keskustelu is None:
        return
    
    nykyinen_kohta = keskustelu
    while nykyinen_kohta is not None:
        nykyinen_kohta = valinta_ja_tulostus(nykyinen_kohta)

    print("Olet nyt sijoitusguru. Kiitos käynnistä ja tervetuloa uudelleen.")

if __name__ == "__main__":
    seikkailu()
