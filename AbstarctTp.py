from abc import ABC, abstractmethod
class Produit(ABC):
    def __init__(self, nom, code):
        self.__nom = nom
        self.__code = code

    @property
    def nom(self):
        return self.__nom

    @property
    def code(self):
        return self.__code

    @abstractmethod
    def getPrixHT(self):
        pass
class Composition:
    def __init__(self, produit, quantite):
        self.__produit = produit
        self.__quantite = quantite

    @property
    def produit(self):
        return self.__produit

    @property
    def quantite(self):
        return self.__quantite


class ProduitElementaire(Produit):
    def __init__(self, nom, code, prixAchat):
        super().__init__(nom, code)
        self.__prixAchat = prixAchat

    def __str__(self):
        return f"{self.nom} ({self.code}) - Prix d'achat: {self.__prixAchat} Dh"

    def getPrixHT(self):
        return self.__prixAchat

class ProduitCompose(Produit):
    tauxTVA = 0.18

    def __init__(self, nom, code, fraisFabrication, listeConstituants):
        super().__init__(nom, code)
        self.__fraisFabrication = fraisFabrication
        self.__listeConstituants = listeConstituants

    @property
    def fraisFabrication(self):
        return self.__fraisFabrication

    @property
    def listeConstituants(self):
        return self.__listeConstituants

    def __str__(self):
        return f"{self.nom} ({self.code}) - Frais de fabrication: {self.__fraisFabrication}"

    def getPrixHT(self):
        prix_total_ht = sum(comp.produit.getPrixHT() * comp.quantite for comp in self.__listeConstituants)
        return prix_total_ht + self.__fraisFabrication


p1 = ProduitElementaire("P1", "001", 10.0)
p2 = ProduitElementaire("P2", "002", 15.0)
p3 = ProduitCompose("P3", "003", 5.0, [Composition(p1, 2), Composition(p2, 4)])
p4 = ProduitCompose("P4", "004", 8.0, [Composition(p2, 3), Composition(p1, 2)])

print(p1)
print(p2)
print(p3)
print(p4)

print(f"Prix hors taxe de P3: {p3.getPrixHT()}")
print(f"Prix hors taxe de P4: {p4.getPrixHT()}")
