class Car:
    """Classe définissant une voiture caractérisée par :
    - sa marque
    - son modèle
    - sa couleur
    - son prix (en €)"""

    def __init__(self, brand, model, color, price): # Méthode constructeur
        """Pour l'instant, on ne va définir qu'un seul attribut"""
        self.brand = brand
        self.model = model
        self.color = color
        self.price = price


voiture_de_thomas = Car("Tesla", "Roadster", "Blanche", 45+10)
voiture_d_emma = Car("Audi", "Lidl", "caca de pigeon", 55)

if voiture_de_thomas.price < voiture_d_emma.price : 
    prix_manquant = voiture_d_emma.price - voiture_de_thomas.price
    print ("il te manque", str(prix_manquant), "€")

elif voiture_d_emma.price < voiture_de_thomas.price :
    prix_restant = voiture_de_thomas.price - voiture_d_emma.price
    print ("il te reste", str(prix_restant), "€")

else :
    print("il ne te reste plus d'argent")