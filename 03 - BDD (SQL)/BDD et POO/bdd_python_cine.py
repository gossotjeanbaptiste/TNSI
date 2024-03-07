#!/usr/bin/env python
# -*- coding: utf-8 -*-
import mysql.connector


class Cinema:
    def __init__(self, id, nom, ville, nbsalle):
        self.id = id
        self.nom = nom
        self.ville = ville
        self.nbsalle = nbsalle
        # modif structure de données : passage dict a list : 'nom_du_film': 'horaire'
        self.films_a_laffiche = {}

    def filmsaffiche(self, film):
        text = ""
        for nom_film, horaires in self.films_a_laffiche.items():
            time = ""
            for horaire in horaires:
                time += f'{horaire} '
            text += f'{nom_film}: {time}\n'
        return text

    def __repr__(self):
        return f'ID: {self.id}, Cinéma: {self.nom}, à {self.ville},  Nombre de salles: {self.nbsalle}\n {self.filmsaffiche(self.films_a_laffiche)}'


connection_params = {
    'host': "localhost",
    'user': "root",
    'password': "160474FGjb",
    'database': "cinema"}

id = int(input("Donnez un cinema de 1 à 5: "))

requete_cine = f"SELECT *  \
            FROM cinema \
 WHERE idCinema = {id}"

requete_film = f'SELECT film.nom, seance.horaire \
                FROM seance \ 
                JOIN film on seance.idFilm = film.idFilm \
                WHERE seance.idCinema = 3 \ 
                ORDER BY seance.horaire'


with mysql.connector.connect(**connection_params) as base_donnee:
    with base_donnee.cursor() as curs:
        curs.execute(requete_cine)
        resultats = curs.fetchall()
        for id, nom, ville, nb_salle in resultats:
            # instanciation obj cinelun
            cinelun = Cinema(id, nom, ville, nb_salle)

        curs.execute(requete_film)
        resultats_film = curs.fetchall()
        for nom, horaire in resultats_film:
            if nom in cinelun.films_a_laffiche.keys():
                cinelun.films_a_laffiche[nom].append(horaire)
            else:
                cinelun.films_a_laffiche[nom] = [horaire]
            # cinelun.films_a_laffiche.append((nom, horaire))

print(cinelun.filmsaffiche(cinelun.films_a_laffiche))
