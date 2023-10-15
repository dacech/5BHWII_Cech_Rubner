import random

kartenwerte = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
symbole = ['♠', '♥', '♦', '♣']

pokerkarten = [wert + symbol for wert in kartenwerte for symbol in symbole]

# Methode, um 2 Indizes zu vertauschen
def vertausche_zwei_index(liste, index1, index2):
    if 0 <= index1 < len(liste) and 0 <= index2 < len(liste):
        liste[index1], liste[index2] = liste[index2], liste[index1]
    else:
        print("Ungültige Indexpositionen")

# Methode für Zufallszahl innerhalb eines Bereichs
def generiere_zufallszahl(minimum, maximum):
    return random.randint(minimum, maximum)

# Methode zur Überprüfung der Pokerhand
def ueberpruefe_pokerhand(hand):
    kartenwert_count = {}
    kartenwert_list = []

    # Zähle die Anzahl der Karten jedes Werts und wandele sie in numerische Werte um
    for karte in hand:
        kartenwert = kartenwerte.index(karte[0]) + 1
        kartenwert_count[kartenwert] = kartenwert_count.get(kartenwert, 0) + 1
        kartenwert_list.append(kartenwert)

    # Sortiere die Kartenwerte in aufsteigender Reihenfolge
    kartenwert_list.sort()

    # Prüfe auf Paar, Zwei Paare, Drilling und Flush
    if 4 in kartenwert_count.values():
        return "Vierling"
    elif 3 in kartenwert_count.values() and 2 in kartenwert_count.values():
        return "Full House"
    elif 3 in kartenwert_count.values():
        return "Drilling"
    elif kartenwert_list == [1, 10, 11, 12, 13]:
        return "Royal Flush"
    elif kartenwert_list[-1] - kartenwert_list[0] == 4:
        return "Straight"
    elif 2 in kartenwert_count.values():
        return "Paar"
    elif 2 in kartenwert_count.values() and len(set(kartenwert_list)) == 3:
        return "Zwei Paare"
    elif len(set(kartenwert_list)) == 4:
        return "High Card"
    elif len(set(kartenwert_list)) == 5 and len(set(kartenwert_list)) == kartenwert_list[-1] - kartenwert_list[0] + 1:
        return "Straight"

# Ziehe 5 Pokerkarten
gezogene_karten = []
for i in range(5):
    zufallsindex = generiere_zufallszahl(0, len(pokerkarten) - 1)
    gezogene_karten.append(pokerkarten[zufallsindex])
    vertausche_zwei_index(pokerkarten, zufallsindex, len(pokerkarten) - 1 - i)

print("Ihre Pokerhand: ", gezogene_karten)
hand_text = ueberpruefe_pokerhand(gezogene_karten)
print("Sie haben einen", hand_text)