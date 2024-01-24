import random

# Hilfsfunktionen für die Spiellogik
def sieg_classic(spieler, gegner):
    if (spieler == "stein" and gegner == "schere") or (spieler == "schere" and gegner == "papier") \
        or (spieler == "papier" and gegner == "stein"):
        return True
    return False

def sieg_erweitert(spieler1_wahl, spieler2_wahl):
    siege = {
        "schere": ["papier", "echse"],
        "papier": ["stein", "spock"],
        "stein": ["echse", "schere"],
        "echse": ["spock", "papier"],
        "spock": ["schere", "stein"]
    }
    return spieler2_wahl in siege[spieler1_wahl]

# Spiellogik für beide Modi
def spiellogik(spieler1_wahl, spieler2_wahl, erweitert=False, ist_gegen_computer=True):
    if spieler1_wahl == spieler2_wahl:
        return "Unentschieden!"
    elif (erweitert and sieg_erweitert(spieler1_wahl, spieler2_wahl)) or (not erweitert and sieg_classic(spieler1_wahl, spieler2_wahl)):
        return "Spieler 1 siegt!" if not ist_gegen_computer else "Du hast gewonnen!"
    else:
        return "Spieler 2 siegt!" if not ist_gegen_computer else "Du hast verloren!"

# Spiel gegen Computer
def spiel_gegen_computer(erweitert):
    auswahl = ["stein", "papier", "schere", "echse", "spock"] if erweitert else ["stein", "papier", "schere"]
    benutzerwahl = input(f"Wähle {', '.join(auswahl)}: ").lower()
    computerwahl = random.choice(auswahl)

    print(f"Computer hat {computerwahl} gewählt.")
    return spiellogik(benutzerwahl, computerwahl, erweitert)

# Spiel gegen anderen Spieler
def spiel_gegen_spieler(erweitert):
    auswahl = ["stein", "papier", "schere", "echse", "spock"] if erweitert else ["stein", "papier", "schere"]
    spieler1_wahl = input(f"Spieler 1, wähle {', '.join(auswahl)}: ").lower()
    spieler2_wahl = input(f"Spieler 2, wähle {', '.join(auswahl)}: ").lower()

    return spiellogik(spieler1_wahl, spieler2_wahl, erweitert, ist_gegen_computer=False)

# Hauptfunktionen
def spielmodus_auswahlen():
    while True:
        spielmodus = input("Wähle den Spielmodus: 1 (1 Spieler), 2 (2 Spieler), 3 (Beenden): ")

        if spielmodus in ["1", "2"]:
            spieltyp = input("Wähle den Spieltyp: 1 (Classic), 2 (Erweitert): ")
            if spieltyp == "1":
                return (spiel_gegen_computer if spielmodus == "1" else spiel_gegen_spieler, False)
            elif spieltyp == "2":
                return (spiel_gegen_computer if spielmodus == "1" else spiel_gegen_spieler, True)
            else:
                print("Ungültige Eingabe für den Spieltyp.")
        elif spielmodus == "3":
            print("Spiel beendet.")
            exit()
        else:
            print("Ungültige Eingabe. Bitte wähle 1, 2 oder 3.")

def spiel_starten(spiel, erweitert):
    while True:
        ergebnis = spiel(erweitert)
        print(ergebnis)

        nochmal = input("Noch mal spielen? (ja/nein): ").lower()
        if nochmal != "ja":
            break

def hauptmenu():
    while True:
        spiel, erweitert = spielmodus_auswahlen()
        spiel_starten(spiel, erweitert)

hauptmenu()
