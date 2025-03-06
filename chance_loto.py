import random

random_pourcentage = random.randint(1 , 100)
name_1 = ""

while name_1 == "":
    name_1 = input("Entrez au moins un prenom ")

name_2 = input("entrez un second prenom ")

if name_2 == "":
    print(f"{name_1} vous avez {random_pourcentage}% de chance de gagner au loto")
else:
    print(f"{name_1} et {name_2} vous avez {random_pourcentage}% de chance de gagnez au loto")








