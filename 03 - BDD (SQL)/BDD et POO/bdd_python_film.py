#!/usr/bin/env python
# -*- coding: utf-8 -*-
import mysql.connector


class Film:
    def __init__(self, nom, datedesortie):
        self.nom = nom
        self.datedesortie = datedesortie
        self.salledecinema = {}

    def __repr__(self):
        return f'Titre: {self.nom} \n{self.alaffiche()}'

    def alaffiche(self):
        text = ""
        for cine, horaires in self.salledecinema.items():
            truc = ""
            for horaire in horaires:
                truc = f'{truc} {horaire}'
            text = f'{text} {cine} {truc}\n'
        return text


def horaire_film(id):
    connection_params = {
        'host': "localhost",
        'user': "root",
        'password': "160474FGjb",
        'database': "cinema"}

    requete = f'SELECT * \
                FROM film \
 WHERE idFilm = {id}'

    requete_cinema = f'SELECT cinema.nom, cinema.ville, seance.horaire \
                    FROM seance \
                    JOIN cinema ON cinema.idCinema = seance.idCinema\
                    WHERE seance.idfilm = {id}\
                    ORDER BY seance.horaire'

    with mysql.connector.connect(**connection_params) as base_donnee:
        with base_donnee.cursor() as curs:
            curs.execute(requete)
            resultats = curs.fetchall()
            for id, nom, datedesortie in resultats:
                # instanciation de l'objet film
                film = Film(nom, datedesortie)

            curs.execute(requete_cinema)
            resultats_cinema = curs.fetchall()
            for nom_cinema, ville, horaire in resultats_cinema:
                alias = f'{nom_cinema} {ville}'
                if alias in film.salledecinema.keys():
                    film.salledecinema[alias].append(horaire)
                else:
                    film.salledecinema[alias] = [horaire]
    return film
