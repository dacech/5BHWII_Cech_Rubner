#basic com(j/n)
import random

def stein_papier_schere():
    benutzer = input("Wähle Stein, Papier oder Schere: ").lower()
    computer = random.choice(["stein", "papier", "schere"])

    print(f"Computer hat {computer} gewählt.")

    if benutzer == computer:
        return "Unentschieden!"
    if sieg(benutzer, computer):
        return "Du hast gewonnen!"
    return "Du hast verloren!"

def sieg(spieler, gegner):
    # Stein schlägt Schere, Schere schlägt Papier, Papier schlägt Stein
    if (spieler == "stein" and gegner == "schere") or (spieler == "schere" and gegner == "papier") \
        or (spieler == "papier" and gegner == "stein"):
        return True

def spiel_starten():
    while True:
        ergebnis = stein_papier_schere()
        print(ergebnis)

        nochmal = input("Noch mal spielen? (ja/nein): ").lower()
        if nochmal != "ja":
            break

spiel_starten()
