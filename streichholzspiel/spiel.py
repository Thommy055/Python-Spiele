import time
import random
print (f"Streichholzspiel: 21!\nRegeln:")
print (f"- Zunächst liegen 21 Streichhölzer auf dem Tisch.\n- Insgesamt sind 2 Spieler zugelassen.\n- Jeder dieser Spieler nimmt abwechselnd zwischen 1 und 4 Streichhölzer.\n- Der Spieler, der das letzte Streichholz nimmt, hat verloren.")
start:str = "ja"

while start == "ja":
    # Schwierigkeit auswählen
    print(f"\nSchwierigkeit: \n1. Leicht \n2. Mittel \n3. Schwer")
    while True:
        try:
            difficulty = int(input("Tippe (1, 2 oder 3): "))
            if 1 <= difficulty <= 3:
                break
            print(f"Fehler! Bitte tippe eine Zahl zwischen 1 und 3 ein.")
        except ValueError:
            print(f"Fehler! Bitte tippe eine richtige Zahl ein.")
    if difficulty == 1:
        print (f"Schwierigkeit: Einfach.")
    elif difficulty == 2:
        print (f"Schwierigkeit: Mittel.")
    else:
        print (f"Schwierigkeit: Schwer.")

    print (f"\nNimm zwischen 1 und 4 Hölzer. Wer das letzte Holz nimmt, hat verloren.")
    streichhoelzer:int = 21
    beginn:int = random.randint(1, 2)
    if beginn == 1:
        print (f"Du beginnst!")
    else:
        print (f"Dein Gegner beginnt!")

    while streichhoelzer > 0:
        if beginn == 1:
        # Spieler zieht Hölzer:
            print (f"\nStreichhölzer auf dem Tisch: {" | " * streichhoelzer} {streichhoelzer}")
            while True:
                try:
                    player = int(input("Wie viele Hölzer nimmst du: "))
                    if 1 <= player <= 4:
                        if player > streichhoelzer:
                            print(f"Du kannst nicht {player} Hölzer nehmen! Es sind nur noch {streichhoelzer} übrig!")
                            continue
                        break
                    print (f"Falsche Zahl. Wiederhole die Eingabe.")
                except ValueError:
                    print (f"Flasche Eingabe! Bitte nur ganze Zahlen eingeben.")

            # Unterschied zwischen 1 "Holz" und mehrere "Hölzer".
            if player == 1:
                print (f"Dann nehme ich {player} Holz.")
            else:
                print (f"Dann nehme ich {player} Hölzer.")
            streichhoelzer = streichhoelzer - player
            beginn = 2

            if streichhoelzer == 0:
                print(f"Tut mir leid, aber du hast verloren.")
                break

        else:
        # Computer zieht Hölzer:
            time.sleep(1)
            print(f"\nStreichhölzer auf dem Tisch: {" | " * streichhoelzer} {streichhoelzer}")
            if streichhoelzer <= 5:
                computer = streichhoelzer - 1
                if computer == 0:
                    computer += 1
            else:
                if difficulty == 1:
                    computer: int = random.randint (1, 4)
                elif difficulty == 2:
                    if streichhoelzer % 5 == 1 or streichhoelzer % 5 == 2:
                        computer: int = random.randint (1, 4)
                    else:
                        computer:int = (streichhoelzer - 1) % 5
                else:
                    if streichhoelzer == 20:
                        computer: int = random.randint(1, 4)
                    elif streichhoelzer % 5 == 1:
                        computer:int = random.randint (1, 4)
                    else:
                        computer:int = (streichhoelzer - 1) % 5
            if computer == 1:
                print (f"Der Computer nimmt {computer} Holz.")
            else:
                print (f"Der Computer nimmt {computer} Hölzer.")
            streichhoelzer = streichhoelzer - computer
            time.sleep(1)
            beginn = 1

            if streichhoelzer == 0:
                print(f"Du hast gewonnen, glückwunsch!")
                break

    while True:
        start =(str(input("\nWillst du nochmal spielen? (ja/nein): ")))
        if start == "ja" or start == "nein":
            break
        else:
            print (f"Fehler! bitte nur \"ja\" oder \"nein\" eintippen!")
