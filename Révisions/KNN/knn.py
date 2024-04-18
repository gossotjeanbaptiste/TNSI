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


def knn(donnees:list, point:list, k:int)->list:
    """
    Performs the k-nearest neighbors algorithm on a given dataset.
    Args:
        donnees (list): The dataset containing the training examples.
        point (list): The point for which we want to find the k nearest neighbors.
        k (int): The number of nearest neighbors to find.
    Returns:
        list: A list of the k nearest neighbors.
    """
    resultat = []
    for donnee in donnees:
        resultat.append((distance_euclidienne(donnee, point), donnee))
    resultat.sort()
    return [i for _, i in resultat[0:k]]

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

trois_plus_proches_voisins = knn(data, point, 3) # ! Entier à modifier pour tester le code !

print(trois_plus_proches_voisins)

for i in trois_plus_proches_voisins:
    print(i)


data_color = [
    [220, 54, 54, 'rouge'],
    [255, 0, 0, 'rouge'],
    [27, 41, 180, 'bleu'],
    [55, 180, 27, 'vert'],
    [180, 61, 27, 'rouge'],
    [52, 125, 235, 'bleu'],
    [110, 52, 235, 'bleu'],
    [52, 235, 86, 'vert'],
    [52, 235, 223, "bleu"],
    [14, 230, 96, "vert"],
    [200, 0, 0, 'rouge'],
    [0, 200, 0, 'vert'],
    [0, 0, 200, 'bleu'],
    [150, 0, 0, 'rouge'],
    [0, 150, 0, 'vert'],
    [0, 0, 150, 'bleu'],
    [100, 0, 0, 'rouge'],
    [0, 100, 0, 'vert'],
    [0, 0, 100, 'bleu'],
    [50, 0, 0, 'rouge'],
    [0, 50, 0, 'vert'],
    [0, 0, 50, 'bleu'],
    [25, 0, 0, 'rouge'],
    [0, 25, 0, 'vert'],
    [0, 0, 25, 'bleu'],
    [230, 50, 50, 'rouge'],
    [50, 230, 50, 'vert'],
    [50, 50, 230, 'bleu'],
    [200, 100, 100, 'rouge'],
    [100, 200, 100, 'vert'],
    [100, 100, 200, 'bleu'],
    [150, 50, 50, 'rouge'],
    [50, 150, 50, 'vert'],
    [50, 50, 150, 'bleu'],
    [120, 0, 0, 'rouge'],
    [0, 120, 0, 'vert'],
    [0, 0, 120, 'bleu'],
    [180, 0, 0, 'rouge'],
    [0, 180, 0, 'vert'],
    [0, 0, 180, 'bleu'],
    [210, 100, 100, 'rouge'],
    [100, 210, 100, 'vert'],
    [100, 100, 210, 'bleu'],
    [240, 50, 50, 'rouge'],
    [50, 240, 50, 'vert'],
    [50, 50, 240, 'bleu'],
    [255, 100, 100, 'rouge'],
    [100, 255, 100, 'vert'],
    [100, 100, 255, 'bleu'],
    [255, 0, 0, 'rouge'],
    [0, 255, 0, 'vert'],
    [0, 0, 255, 'bleu']
]

