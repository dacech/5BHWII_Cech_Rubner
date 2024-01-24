#1p2p
import random

def stein_papier_schere_gegen_computer():
    benutzer = input("Wähle Stein, Papier oder Schere: ").lower()
    computer = random.choice(["stein", "papier", "schere"])

    print(f"Computer hat {computer} gewählt.")

    if benutzer == computer:
        return "Unentschieden!"
    if sieg(benutzer, computer):
        return "Du hast gewonnen!"
    return "Du hast verloren!"

def stein_papier_schere_gegen_spieler():
    spieler1 = input("Spieler 1, wähle Stein, Papier oder Schere: ").lower()
    spieler2 = input("Spieler 2, wähle Stein, Papier oder Schere: ").lower()

    if spieler1 == spieler2:
        return "Unentschieden!"
    if sieg(spieler1, spieler2):
        return "Spieler 1 hat gewonnen!"
    return "Spieler 2 hat gewonnen!"

def sieg(spieler, gegner):
    if (spieler == "stein" and gegner == "schere") or (spieler == "schere" and gegner == "papier") \
        or (spieler == "papier" and gegner == "stein"):
        return True

def spielmodus_auswahlen():
    while True:
        spielmodus = input("Möchtest du gegen den Computer (1) oder einen anderen Spieler (2) spielen? Gib 1 oder 2 ein: ")

        if spielmodus == "1":
            return stein_papier_schere_gegen_computer
        elif spielmodus == "2":
            return stein_papier_schere_gegen_spieler
        else:
            print("Ungültige Eingabe. Bitte wähle 1 oder 2.")

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
        spiel_starten(gewaehltes_spiel)

hauptmenu()
