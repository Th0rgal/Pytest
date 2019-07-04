class Car:
    """Classe définissant une voiture caractérisée par :
    - sa marque
    - son modèle
    - sa couleur
    - son prix"""

    def __init__(self, brand, model, color, price): # Méthode constructeur
        """Pour l'instant, on ne va définir qu'un seul attribut"""
        self.brand = brand
        self.model = model
        self.color = color
        self.price = price


car_of_emma = Car("Tesla", "Roadster", "Red", 250000)
