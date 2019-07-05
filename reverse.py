def reverse(debut):
    fin = ""
    for c in debut:
        fin = c + fin #ajoute une lettre c au bout du mot final
    return fin


mot_depart = input("rentrez le mot de départ: ")
mot_arrivee = reverse(mot_depart)

print(mot_arrivee)