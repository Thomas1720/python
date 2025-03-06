"""Premier programme
Formation Python
appredre la programmation"""

nom = ""
while nom == "":
    nom = input("Quel est votre nom ? ")

age = 0
while age == 0:
    age_str = input("Quel est votre age? ")
    try:
        age = int(age_str)
    except:
        print("ERREUR: vous devez rentrer un nombre pour l'age")

print(f"Vous vous appelez {nom} vous avez {str(age)} ans. ")
print(f"L'an prochain vous aurez {str(age + 1)} ans.")


