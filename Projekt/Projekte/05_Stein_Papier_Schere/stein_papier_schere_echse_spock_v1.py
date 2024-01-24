import random

def stein_papier_schere_echse_spock(spieler1_wahl, spieler2_wahl, ist_gegen_computer=True):
    siege = {
        "schere": ["papier", "echse"],
        "papier": ["stein", "spock"],
        "stein": ["echse", "schere"],
        "echse": ["spock", "papier"],
        "spock": ["schere", "stein"]
    }

    if spieler1_wahl == spieler2_wahl:
        return "Unentschieden!"
    elif spieler2_wahl in siege[spieler1_wahl]:
        return "Spieler 1 siegt!" if not ist_gegen_computer else "Du hast gewonnen!"
    else:
        return "Spieler 2 siegt!" if not ist_gegen_computer else "Du hast verloren!"

def spiel_gegen_computer():
    benutzerwahl = input("Wähle Stein, Papier, Schere, Echse oder Spock: ").lower()
    computerwahl = random.choice(["stein", "papier", "schere", "echse", "spock"])

    print(f"Computer hat {computerwahl} gewählt.")
    return stein_papier_schere_echse_spock(benutzerwahl, computerwahl)

def spiel_gegen_spieler():
    spieler1_wahl = input("Spieler 1, wähle Stein, Papier, Schere, Echse oder Spock: ").lower()
    spieler2_wahl = input("Spieler 2, wähle Stein, Papier, Schere, Echse oder Spock: ").lower()

    return stein_papier_schere_echse_spock(spieler1_wahl, spieler2_wahl, ist_gegen_computer=False)

def spielmodus_auswahlen():
    while True:
        spielmodus = input("Wähle den Spielmodus: 1 (1 Spieler), 2 (2 Spieler), 3 (Beenden): ")

        if spielmodus == "1":
            return spiel_gegen_computer
        elif spielmodus == "2":
            return spiel_gegen_spieler
        elif spielmodus == "3":
            print("Spiel beendet.")
            exit()
        else:
            print("Ungültige Eingabe. Bitte wähle 1, 2 oder 3.")

def spiel_starten(spiel):
    while True:
        ergebnis = spiel()
        print(ergebnis)

        nochmal = input("Noch mal spielen? (ja/nein): ").lower()
        if nochmal != "ja":
            break

def hauptmenu():
    while True:
        gewaehltes_spiel = spielmodus_auswahlen()
        if gewaehltes_spiel:
            spiel_starten(gewaehltes_spiel)

hauptmenu()
