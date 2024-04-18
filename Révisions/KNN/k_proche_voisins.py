#!/usr/bin/env python
# -*- coding: utf-8 -*-
from math import sqrt

def knn(donnees, point, k):
    pass


def distance_euclidienne(point1, point2):
    pass


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
    print(data[i])
