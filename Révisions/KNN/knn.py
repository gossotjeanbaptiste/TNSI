# -*- coding: utf-8 -*-
#!/usr/bin/env python
from math import sqrt


def distance_euclidienne(point1: list, point2: list) -> float:
    """
    Calculates the Euclidean distance between two points.
    Args:
        point1 (list): The coordinates of the first point.
        point2 (list): The coordinates of the second point.
    Returns:
        float: The Euclidean distance between the two points.
    """
    distance_carre = 0
    for a, b in zip(point1, point2):
        distance_carre += (b - a) ** 2
    return sqrt(distance_carre)


def knn(donnees, point, k):
    resultat = []
    for donnee in donnees:
        resultat.append((distance_euclidienne(donnee, point), donnee))
    resultat.sort()
    return resultat[0:k]

data = [[65.75, 112.99],
         [71.52, 136.49],
         [69.40, 153.03],
         [68.22, 142.34],
         [67.79, 144.30],
         [68.70, 123.30],
         [69.80, 141.49],
         [70.01, 136.46],
         [67.90, 112.37],
         [66.49, 127.45],
        ]
point = [70, 140]

trois_plus_proches_voisins = knn(data, point, 3)

print(trois_plus_proches_voisins)

for i in trois_plus_proches_voisins:
    print(i)
