# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 22:09:27 2025

@author: vstoy
Arbeidskrav 2
Oppgave 5
"""

import math  # Importerer bibliotek for matematiske beregninger

# Funksjon for å beregne areal og ytre omkrets
def beregn_figurer(a, b):
    # Beregn arealet
    trekant_areal = (a * b) / 2
    halvsirkel_areal = (math.pi * (a / 2)**2) / 2
    total_areal = trekant_areal + halvsirkel_areal

    # Beregn omkretsen
    hypotenus = math.sqrt(a**2 + b**2)  # Pythagoras for hypotenusen
    halvsirkel_bue = math.pi * (a / 2)
    total_omkrets = b + hypotenus + halvsirkel_bue

    return total_areal, total_omkrets

# Be brukeren om input for a og b
a = float(input("Skriv inn lengden på a (katetet): "))
b = float(input("Skriv inn lengden på b (katetet): "))

# Beregn resultatene
areal, omkrets = beregn_figurer(a, b)

# Skriv ut resultatene
print(f"Arealet er {areal:.2f} kvadratmeter.")
print(f"Ytre omkrets er {omkrets:.2f} meter.")

