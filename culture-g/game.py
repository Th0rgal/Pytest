import time
import json
from random import choice, randrange, shuffle


class Citation:
    """
    Notre objet Citation est composé de :
    - Le contenu (un texte càd str)
    - Un auteur (le nom de l'auteur càd str)
    - Une origine (titre de l'oeuvre dont elle est extraitre càd str)
    - Année de publication càd int
    """

    def __init__ (self, dict): #constructeur de notre citation
        self.__dict__.update(dict)

    def version_texte(self):
        if self.date == -1 and not self.origine:
            return "« {0} » par {1}".format(self.contenu, self.auteur)
        return "« {0} » par {1} en {2}, extrait de {3}".format(self.contenu, self.auteur, self.date, self.origine)


recueil = []
#lit le fichier data.json et convertit son contenu en Citations
for json_citation in json.load(open('data.json')):
    recueil.append(Citation(json_citation))


#supprime les doublons (un set ne peut pas avoir d'élément en double)
set_auteurs = set()
for citation in recueil:
    set_auteurs.add(citation.auteur)

score = 0

#game loop
for i in range (20):

    #tire au hasard une citation et la supprime du recueil
    index = randrange(len(recueil))
    citation_a_trouver = recueil[index]
    del recueil[index]

    #génère une liste d'auteurs et un texte stylisé
    six_authors = {citation_a_trouver.auteur}
    while len(six_authors) < 6:
        fake_author = choice(list(set_auteurs))
        six_authors.add(fake_author)

    result = list(six_authors)
    shuffle(result)

    right_author_index = result.index(citation_a_trouver.auteur)

    designed_authors = "\n"
    for author_index in range (len(result)):
        designed_authors += "\n{0} - {1}".format(str(author_index+1), result[author_index])


    #énoncé
    print("---[Question {0}/20]---".format(i+1))
    print ("\n> Citation : « {0} »".format(citation_a_trouver.contenu))
    print ("\n> Liste d'auteurs possibles : " + designed_authors)

    proposition = input("\n> Donne le numéro correspondant : ")

    if not proposition:
        print("Tu as sauté la question")
    elif int(proposition)-1 == right_author_index: 
        print("Tu as trouvé, tu gagnes 1 point")
        score += 1
    else:
        print("Tu t'es trompé, tu perds 2 points")
        score -= 2

    input("\nVoici la citation et ses informations complémentaires : {0}, pour passer à la question suivante appuie sur entrer !\n\n".format(citation_a_trouver.version_texte()))

#affiche le message final
print("Ton score est de: " + str(score))