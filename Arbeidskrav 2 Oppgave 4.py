# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 22:05:59 2025

@author: vstoy
Arbeidskrav 2
Oppgave 4 a, b og c
"""

# Oppretter dictionary med land som nøkkel
data = {
    "England": {"hovedstad": "London", "innbyggere": 8.982},
    "Frankrike": {"hovedstad": "Paris", "innbyggere": 11.017},
    "Japan": {"hovedstad": "Tokyo", "innbyggere": 37.4},
}

# Be brukeren om å skrive inn et land
land = input("Skriv inn et land: ")

# Sjekk om landet finnes i dictionaryen
if land in data:
    hovedstad = data[land]["hovedstad"]
    innbyggere = data[land]["innbyggere"]
    print(f"{hovedstad} er hovedstaden i {land} og det er {innbyggere} mill. innbyggere i {hovedstad}.")
else:
    print(f"{land} finnes ikke i listen.")

# Be brukeren om å legge inn informasjon om et nytt land
nytt_land = input("Skriv inn et nytt land: ")
hovedstad = input("Skriv inn hovedstaden: ")
innbyggere = float(input("Skriv inn antall innbyggere i mill.: "))

# Oppdater dictionaryen med den nye informasjonen
data[nytt_land] = {"hovedstad": hovedstad, "innbyggere": innbyggere}

# Skriv ut den oppdaterte dictionaryen
print("Oppdatert dictionary:")
for land, info in data.items():
    print(f"{land}: Hovedstad: {info['hovedstad']}, Innbyggere: {info['innbyggere']} mill.")

