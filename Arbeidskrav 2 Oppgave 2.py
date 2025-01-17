# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 22:02:17 2025

@author: vstoy

Arbeidskrav 2
Oppgave 2
"""

import math  # Importer biblioteket for å bruke funksjoner som avrunding

# Be brukeren om å skrive inn antall elever
antall_elever = int(input("Skriv inn antall elever: "))

# Regn ut hvor mange pizzaer som trengs
# Hver elev spiser 1/4 pizza, så vi deler antall elever på 4 og runder opp
antall_pizzaer = math.ceil(antall_elever / 4)

# Skriv ut resultatet
print(f"Det må handles inn {antall_pizzaer} pizzaer til festen.")