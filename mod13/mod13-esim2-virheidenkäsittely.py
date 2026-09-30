# virheidenkäsittely
import json

class Player:
    def __init__(self, age):
        self.age = age
        self.points = 0
    def go_forward(self):
        print("Pelaaja etenee ja saa yhden pisteen.")
        self.points += 1
        print(f"Pisteitä kasassa nyt {self.points}")



    ## pelitilanteen lataus ja tallennus
    def save_game(self):
        try:
            with open("mod13/save.txt", "w") as file:
                data = {"age": self.age, "points": self.points}
                json.dump(data, file)
        except FileNotFoundError:
            print("Tiedostoa ei löydy.")
        except IOError:
            print("Tiedoston käsittelyssä tapahtui virhe.")

    def info(self):
        print(f"Pelaajan ikä on {self.age} ja pisteet {self.points}")

    def load_game(self):
        try:
            with open("mod13/save.txt", "r") as file:
                data = json.load(file)
                #print("Ladattu tallennusdata: ", data)
                self.points = data["points"]
                self.age = data["age"]
        except FileNotFoundError:
            print("Tiedostoa ei löydy.")
        except IOError:
            print("Tiedoston käsittelyssä tapahtui virhe.")


# Main loop
def start_game():
    game_running = True
    while game_running:
        command = input("Anna komento: ")
        if command == "tallenna":
            player.save_game()
        elif command == "lataa":
            player.load_game()
            player.info()
        elif command == "etene":
            player.go_forward()
        elif command == "lopeta":
            game_running = False
        else:
            print("Virheellinen komento")


# Pääohjelma, suoritus alkaa tästä
print("Peli alkaa")
age = 0 # ei pakollinen

while True:
    try:
        age = int(input("Anna pelaajan ikä: "))
        break
    except ValueError:
        print("Virheellinen syöte: ei ole kokonaisluku.")



print(f"Pelaajan ikä on: {age}")




if age > 11:
    player = Player(age)
    start_game()
else:
    print("Pelaaja liian nuori!")



print("Ohjelma suoritus loppui.")