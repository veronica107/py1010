# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 12:15:40 2024

@author: Veronica Støylen

Arbeidskrav 1 PY1010
"""

# Program for å sammenligne årlige kostnader for elbil og bensinbil

# Antar kjørelengde per år
kjoreLengde = 10000  # km per år

# Drivstoffkostnader per km
ElDrivstoff = 0.2 * 2.0  # Elbil (kWh per km * pris per kWh)
BensinDrivstoff = 1.0  # Bensinbil (kr per km)

# Forsikringskostnader
ElForsikring = 5000
BensinForsikring = 7500

# Bomkostnader per km
ElBomKm = 0.1
BensinBomKm = 0.3

# Trafikkforsikringsavgift (lik for begge biler)
trafikkforsikringsavgift = int(365 * 8.38)  # omregnet til årlig kostnad

# Beregner kostnader for elbil
drivstoffEl = int(kjoreLengde * ElDrivstoff)
bomEl = int(kjoreLengde * ElBomKm)
ElTotalKost = drivstoffEl + trafikkforsikringsavgift + bomEl + ElForsikring

# Beregner kostnader for bensinbil
drivstoffBensin = int(kjoreLengde * BensinDrivstoff)
bomBensin = int(kjoreLengde * BensinBomKm)
BensinTotalKost = drivstoffBensin + trafikkforsikringsavgift + bomBensin + BensinForsikring

# Skriver ut alle kostnader
print("Årlig kjørelengde er:", kjoreLengde, "km per år\n")

print("Drivstoffkostnader per år:")
print("Elbil:", drivstoffEl, "kr")
print("Bensinbil:", drivstoffBensin, "kr\n")

print("Årlig trafikkforsikringsavgift, lik for begge:", trafikkforsikringsavgift, "kr\n")

print("Bompenger per år:")
print("Elbil:", bomEl, "kr")
print("Bensinbil:", bomBensin, "kr\n")

print("Totalkostnad per år:")
print("Elbil:", ElTotalKost, "kr")
print("Bensinbil:", BensinTotalKost, "kr\n")

# Beregner prisdifferansen
prisDiff = abs(BensinTotalKost - ElTotalKost)

# Skriver ut prisdifferansen
print("Prisdifferanse mellom bensinbil og elbil:", prisDiff, "kr")
