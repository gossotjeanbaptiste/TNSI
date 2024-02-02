#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import pprint

with open('cinemas.json','r', encoding = 'utf-8') as json_file_1:
    cinemas = json.load(json_file_1)

with open('films.json','r', encoding = 'utf-8') as json_file_2:
    films = json.load(json_file_2)

with open('seances.json','r', encoding = 'utf-8') as json_file_3:
    seances = json.load(json_file_3)

def film_by_id(idfilm):
    for film in films:
        if film['IdFilm'] == idfilm:
            return film
    return None

def cinema_by_id(idcinema):
    for cinema in cinemas:
        if cinema['IdCinema'] == idcinema:
            return cinema
    return None

def seance_by_id(idseance):
    for seance in seances:
        if seance['IdSeance'] == idseance:
            return seance
    return None

#en combinant ces trois fonctions écrire une fonction qui à partir d'un identifiant de séance retourne 
#le nom du film l'heure de la séance le nom du cinéma et la ville ou elle se déroule.

def seance_explicit_by_id(id):
    seance = seance_by_id(id)
    film = film_by_id(seance['IdFilm'])
    cinema = cinema_by_id(seance['IdCinema'])
    return f"{film['Nom']} - {seance['Horaire']} - {cinema['Nom']} - {cinema['Ville']}"

#1)
nb_salles = 0
for cinema in cinemas:
    if cinema['Ville'] == 'Nancy':
        nb_salles += cinema['NombreSalles']
print(f'Il y a {nb_salles} salles à Nancy')

nb_seances_matin = 0
for seance in seances:
    if int(seance['Horaire'][:2]) < 12:
        nb_seances_matin += 1
print(f'Il y a {nb_seances_matin} séances le matin')

"""pp = pprint.PrettyPrinter(width = 72, indent=4)
pp.pprint(cinemas)"""

"""for film in films:
    print(f"{film['Nom']}")"""