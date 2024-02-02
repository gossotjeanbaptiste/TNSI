#!/usr/bin/env python
# -*- coding: utf-8 -*-
import mysql.connector



connection_params = {
    'host': "localhost",
    'user': "root",
    'password': "160474FGjb",
    'database': "TEST"}

requete = f"SELECT FILM.nom, SEANCE.horaire, CINEMA.nom, CINEMA.ville FROM SEANCE \
        JOIN film ON SEANCE.idfilm = FILM.idfilm \
        JOIN cinema on SEANCE.idCinema = CINEMA.idCinema \
        WHERE horaire < '12:00';"

with mysql.connector.connect(**connection_params) as base_donnee :
    with base_donnee.cursor() as curs:
        curs.execute(requete)
        resultats = curs.fetchall()
        for seance in resultats:
            print(seance)
