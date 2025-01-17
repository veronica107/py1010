# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 22:04:43 2025

@author: vstoy

Arbeidskrav 2
Oppgave 3
"""

import numpy as np  # Importer numpy-biblioteket for matematiske beregninger

# Be brukeren om å skrive inn gradtallet
v_grad = float(input("Skriv inn gradtallet: "))

# Regn om fra grader til radianer
v_rad = v_grad * np.pi / 180

# Skriv ut resultatet
print(f"Radiantallet til vinkelen er {v_rad:.2f}.")