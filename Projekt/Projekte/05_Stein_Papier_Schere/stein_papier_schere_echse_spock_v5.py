#server
import random
import os
import requests

# BÖSE VARIABLEN
SCOREBOARD_FILE = "scoreboard.txt"
ANZ_FILE = "anz.txt"

# Funktion zum Lesen der Daten aus der 'anz.txt'-Datei und Senden an den Webserver
def sende_anzahlen_an_server():
    with open(ANZ_FILE, "r") as file:
        anzahlen = file.readline().strip().split()
    # URL des Webservers, an den die Daten gesendet werden sollen
    url = 'http://url.com/speichere_anzahlen'
    # Daten, die an den Webserver gesendet werden
    data = {'anzahlen': anzahlen}

    # Anfrage an den Webserver senden
    response = requests.post(url, json=data)

    # Antwort des Servers anzeigen
    print(response.text)

def init_scoreboard():
    if not os.path.exists(SCOREBOARD_FILE):
        with open(SCOREBOARD_FILE, "w") as file:
            file.write("0 0 0\n")

def load_scoreboard():
    init_scoreboard()
    with open(SCOREBOARD_FILE, "r") as file:
        lines = file.readlines()
        scores = [int(score) for score in lines[0].split()]
        return scores

def save_scoreboard(scores):
    with open(SCOREBOARD_FILE, "w") as file:
        file.write(f"{scores[0]} {scores[1]} {scores[2]}\n")

def update_scoreboard(ergebnis):
    scores = load_scoreboard()
    if ergebnis in ["Spieler 1 siegt!", "Du hast gewonnen!"]:
        scores[0] += 1
    elif ergebnis in ["Spieler 2 siegt!", "Du hast verloren!"]:
        scores[1] += 1
    elif ergebnis == "Unentschieden!":
        scores[2] += 1
    save_scoreboard(scores)

def init_anzahlen():
    if not os.path.exists(ANZ_FILE):
        with open(ANZ_FILE, "w") as file:
            file.write("0 0 0 0 0\n")

def load_anzahlen():
    init_anzahlen()
    with open(ANZ_FILE, "r") as file:
        lines = file.readlines()
        anzahlen = [int(anz) for anz in lines[0].split()]
        return anzahlen

def save_anzahlen(anzahlen):
    with open(ANZ_FILE, "w") as file:
        file.write(" ".join(str(anz) for anz in anzahlen) + "\n")

def update_anzahlen(auswahl):
    anzahlen = load_anzahlen()
    auswahl_index = {"schere": 0, "stein": 1, "papier": 2, "echse": 3, "spock": 4}
    if auswahl in auswahl_index:
        anzahlen[auswahl_index[auswahl]] += 1
    save_anzahlen(anzahlen)

def show_scoreboard():
    scores = load_scoreboard()
    anzahlen = load_anzahlen()
    print("\nScoreboard:")
    print(f"Spieler 1: {scores[0]}")
    print(f"Spieler 2: {scores[1]}")
    print(f"Unentschieden: {scores[2]}")
    print(f"Anz Scheren: {anzahlen[0]}")
    print(f"Anz Steine: {anzahlen[1]}")
    print(f"Anz Papiere: {anzahlen[2]}")
    print(f"Anz Echsen: {anzahlen[3]}")
    print(f"Anz Spocks: {anzahlen[4]}")

def sieg_classic(spieler, gegner):
    return (spieler == "stein" and gegner == "schere") or (spieler == "schere" and gegner == "papier") or (spieler == "papier" and gegner == "stein")

def sieg_erweitert(spieler1_wahl, spieler2_wahl):
    siege = {"schere": ["papier", "echse"], "papier": ["stein", "spock"], "stein": ["echse", "schere"], "echse": ["spock", "papier"], "spock": ["schere", "stein"]}
    return spieler2_wahl in siege[spieler1_wahl]

def spiellogik(spieler1_wahl, spieler2_wahl, erweitert=False, ist_gegen_computer=True):
    update_anzahlen(spieler1_wahl)
    update_anzahlen(spieler2_wahl)
    if spieler1_wahl == spieler2_wahl:
        return "Unentschieden!"
    elif (erweitert and sieg_erweitert(spieler1_wahl, spieler2_wahl)) or (not erweitert and sieg_classic(spieler1_wahl, spieler2_wahl)):
        return "Spieler 1 siegt!" if not ist_gegen_computer else "Du hast gewonnen!"
    else:
        return "Spieler 2 siegt!" if not ist_gegen_computer else "Du hast verloren!"

def spiel_gegen_computer(erweitert):
    auswahl = ["stein", "papier", "schere", "echse", "spock"] if erweitert else ["stein", "papier", "schere"]
    benutzerwahl = input(f"Wähle {', '.join(auswahl)}: ").lower()
    computerwahl = random.choice(auswahl)
    print(f"Computer hat {computerwahl} gewählt.")
    ergebnis = spiellogik(benutzerwahl, computerwahl, erweitert)
    update_scoreboard(ergebnis)
    return ergebnis

def spiel_gegen_spieler(erweitert):
    auswahl = ["stein", "papier", "schere", "echse", "spock"] if erweitert else ["stein", "papier", "schere"]
    spieler1_wahl = input(f"Spieler 1, wähle {', '.join(auswahl)}: ").lower()
    spieler2_wahl = input(f"Spieler 2, wähle {', '.join(auswahl)}: ").lower()
    ergebnis = spiellogik(spieler1_wahl, spieler2_wahl, erweitert, ist_gegen_computer=False)
    update_scoreboard(ergebnis)
    return ergebnis

def spielmodus_auswahlen():
    while True:
        spielmodus = input("Wähle den Spielmodus: 1 (1 Spieler), 2 (2 Spieler), 3 (Scoreboard), 4 (Beenden): ")
        if spielmodus == "1":
            spieltyp = input("Wähle den Spieltyp: 1 (Classic), 2 (Erweitert): ")
            if spieltyp == "1":
                return (spiel_gegen_computer, False)
            elif spieltyp == "2":
                return (spiel_gegen_computer, True)
        elif spielmodus == "2":
            spieltyp = input("Wähle den Spieltyp: 1 (Classic), 2 (Erweitert): ")
            if spieltyp == "1":
                return (spiel_gegen_spieler, False)
            elif spieltyp == "2":
                return (spiel_gegen_spieler, True)
        elif spielmodus == "3":
            show_scoreboard()
        elif spielmodus == "4":
            print("Spiel beendet.")
            exit()

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
        if spiel:
            spiel_starten(spiel, erweitert)

if __name__ == "__main__":
    hauptmenu()
