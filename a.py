from random import randrange



class Citation:
    """
    Notre objet Citation est composé de :
    - Le contenu (un texte càd str)
    - Un auteur (le nom de l'auteur càd str)
    - Une origine (titre de l'oeuvre dont elle est extraitre càd str)
    - Année de publication càd int
    """

    def __init__ (self, contenu, auteur, origine, date): #constructeur de notre citation
        self.contenu = contenu
        self.auteur = auteur
        self.origine = origine
        self.date = date

    def version_texte(self):
        if self.date == -1 and not self.origine:
            return "« {0} » par {1}".format(self.contenu, self.auteur)
        return "« {0} » par {1} en {2}, extrait de {3}".format(self.contenu, self.auteur, self.date, self.origine)


recueil = [
    Citation("Je n'ai rien d'autre à offrir que du sang, de la peine, des larmes et de la sueur ", "Winston Churchill", "Discours devant la chambre des communes", 1940),
    Citation("L'argent ne fait pas le bonheur des pauvres", "Coluche", "", -1),
    Citation("Allô! Non mais allô, quoi! T'es une fille, t'as pas d'shampooing? Allô, allô! J'sais pas, vous m'recevez? T'es une fille, t'as pas d'shampooing! C'est comme si j'te dis: t'es une fille, t'as pas d'cheveux", "Nabilla", "les anges de la téléréalité", 2013),
    Citation("C’est un roc ! … c’est un pic ! … c’est un cap ! Que dis-je, c’est un cap ? … C’est une péninsule !", "Edmond Rostand", "Cyrano de Bergerac", 1897),
    Citation("I have a dream", "Martin Luther King", "Marche sur Washington pour l'emploi et la liberté", 1963),
    Citation("La définition de la folie, c’est de refaire toujours la même chose, et d’attendre des résultats différents", "Albert Einstein", "", -1),
    Citation("L'art de la guerre, c'est de soumettre l'ennemi sans combat.", "Sun Tzu", "L'Art de la guerre", 512),
    Citation("Tout le plaisir de l'amour est dans le changement", "Molière", "Dom Juan", 1665),
    Citation("Madame est morte, elle respire plus", "Quentin", "Snapchat", 2019),
    Citation("Maman est morte", "Albert Camus", "L'étranger", 1942),
    Citation("Je crois que deux et deux sont quatre, Sganarelle, et que quatre et quatre sont huit", "Molière", "Dom Juan", 1665),
    Citation("Tous les vices à la mode passent pour vertus", "Molière", "Dom Juan", 1665),
    Citation("Moi je me changerai en chien si peux restersur la Terre et comme réverbère quotidien je m'offrirai Madame Thatcher", "Renaud", "Miss maggie", 1985),
    Citation("May the force be with you", "Georges Lucas", "Star Wars", 1999),
    Citation("Mignonne, allons voir si la rose", "Ronsard", "Les Amours de Cassandre", 1545), 
    Citation("Heureux qui, comme Ulysse, a fait un beau voyage", "Joachim Du Bellay", "Les Regrets", 1558),
    Citation("Plus ils sont petits, plus ils cherchent à paraître grands", "Adolf Hitler", "Mein Kampf", 1934),
    Citation("J'crois que toi et moi, on a un peu le même problème ; c'est qu'on peut pas vraiment tout miser sur notre physique, surtout toi.", "Les bronzés", "Les bronzés font du ski", 1979),
    Citation("Je sure solennellement que mes intentions sont mauvaises", "JK Rowling", "Harry Potter et le prisonnier d'Azkaban", 2004),
    Citation("Non Dobby n'a pas de maître, c'est un elfe LIBRE! Non, Dobby ne voulait pas tuer! blesser très gravement, mutiler... Mais pas tuer!", "JK Rowling", "Harry Potter et la Chambre des Secrets", 1998),
    Citation("Je suis ton père", "Georges Lucas", "Star Wars, épisode V", 1980),
    Citation("J'échangerais toute ma technologie pour un après-midi avec Socrate", "Steve Jobs", "", -1),
    Citation("C'est plus marrant d'être un pirate que de s'engager dans la marine", "Steve Jobs", "", -1),
    Citation("Madame se meurt! Madame est morte!", "Jacques-Bénigne Bossuet", "Oraisons funèbres de Bossuet", 1689),
    Citation("Ô rage ! Ô désespoir ! Ô vieillesse ennemie ! N'ai-je donc tant vécu que pour cette infamie ? ", "Pierre Corneille", "Le Cid", 1637)

]

print(len(recueil))

index = randrange(len(recueil))
citation_a_trouver = recueil[index]
del recueil[index]

print(len(recueil))