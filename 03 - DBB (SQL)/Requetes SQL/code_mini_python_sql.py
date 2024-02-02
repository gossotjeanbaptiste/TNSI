#!/usr/bin/env python
# -*- coding: utf-8 -*-
import mysql.connector


connection_params = {
    'host': "localhost",
    'user': "root",
    'password': "**********",
    'database': "MONDE"}


requete = ".............."

with mysql.connector.connect(**connection_params) as db :
    with db.cursor() as c:

        c.execute(requete)
        resultats = c.fetchall()
