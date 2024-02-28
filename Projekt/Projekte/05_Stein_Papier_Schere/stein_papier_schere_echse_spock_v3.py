#scoreboard
import random
import os

SCOREBOARD_FILE = "scoreboard.txt"

# Initialisierung des Scoreboards
def init_scoreboard():
    if not os.path.exists(SCOREBOARD_FILE):
        with open(SCOREBOARD_FILE, "w") as file:
            file.write("0 0 0\n")  # Standard-Scores (Spieler 1, Spieler 2, Unentschieden)

# Laden des Scoreboards aus der Datei
def load_scoreboard():
    init_scoreboard()  # Sicherstellen, dass das Scoreboard initialisiert ist
    with open(SCOREBOARD_FILE, "r") as file:
        lines = file.readlines()
        if lines:
            scores = [int(score) for score in lines[0].split()]
            return scores
        else:
            #print("Die Scoreboard-Datei ist leer.")
            return [0, 0, 0]  # Standard-Scores zurückgeben, wenn die Datei leer ist


# Speichern des Scoreboards in die Datei
def save_scoreboard(scores):
    with open(SCOREBOARD_FILE, "w") as file:
        file.write(f"{scores[0]} {scores[1]} {scores[2]}\n")

# Funktion zum Aktualisieren des Scoreboards basierend auf dem Ergebnis
def update_scoreboard(ergebnis):
    scores = load_scoreboard()
    if ergebnis == "Spieler 1 siegt!" or ergebnis == "Du hast gewonnen!":
        scores[0] += 1
    elif ergebnis == "Spieler 2 siegt!" or ergebnis == "Du hast verloren!":
        scores[1] += 1
    elif ergebnis == "Unentschieden!":
        scores[2] += 1
    save_scoreboard(scores)

# Funktion zum Anzeigen des Scoreboards
def show_scoreboard():
    scores = load_scoreboard()
    print("\nScoreboard:")
    print(f"Spieler 1: {scores[0]}")
    print(f"Spieler 2: {scores[1]}")
    print(f"Unentschieden: {scores[2]}")

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
    ergebnis = spiellogik(benutzerwahl, computerwahl, erweitert)
    update_scoreboard(ergebnis)
    return ergebnis

# Spiel gegen anderen Spieler
def spiel_gegen_spieler(erweitert):
    auswahl = ["stein", "papier", "schere", "echse", "spock"] if erweitert else ["stein", "papier", "schere"]
    spieler1_wahl = input(f"Spieler 1, wähle {', '.join(auswahl)}: ").lower()
    spieler2_wahl = input(f"Spieler 2, wähle {', '.join(auswahl)}: ").lower()

    ergebnis = spiellogik(spieler1_wahl, spieler2_wahl, erweitert, ist_gegen_computer=False)
    update_scoreboard(ergebnis)
    return ergebnis

# Hauptfunktionen
def spielmodus_auswahlen():
    while True:
        spielmodus = input("Wähle den Spielmodus: 1 (1 Spieler), 2 (2 Spieler), 3 (Scoreboard), 4 (Beenden): ")

        if spielmodus == "1":
            spieltyp = input("Wähle den Spieltyp: 1 (Classic), 2 (Erweitert): ")
            if spieltyp == "1":
                return (spiel_gegen_computer, False)
            elif spieltyp == "2":
                return (spiel_gegen_computer, True)
            else:
                print("Ungültige Eingabe für den Spieltyp.")
        elif spielmodus == "2":
            spieltyp = input("Wähle den Spieltyp: 1 (Classic), 2 (Erweitert): ")
            if spieltyp == "1":
                return (spiel_gegen_spieler, False)
            elif spieltyp == "2":
                return (spiel_gegen_spieler, True)
            else:
                print("Ungültige Eingabe für den Spieltyp.")
        elif spielmodus == "3":
            show_scoreboard()
        elif spielmodus == "4":
            print("Spiel beendet.")
            exit()
        else:
            print("Ungültige Eingabe. Bitte wähle 1, 2, 3 oder 4.")

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

# Starten des Programms
if __name__ == "__main__":
    hauptmenu()
