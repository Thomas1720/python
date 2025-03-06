annee = int(input("Entrez une année: "))

if annee % 4 ==0:
    if annee % 100 ==0:
        if annee % 400 ==0:
            print("l'année est bissextile")
        else:
            print("l'année n'est pas bissextile")
    else:
        print("l'année est bissextile")
else:
    print("l'année n'est pas bissextile")


