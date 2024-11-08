# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 21:30:37 2024

@author: Veronica Støylen

Arbeidskrav 1 PY1010
"""

# Skalsammenligne kostnader mellom kjøp av elbil og bensinbil

# Antall kjørte km per år
km_per_aar = 10000

# Kostnader for elbil
forsikring_elbil = 5000  # kr/år
trafikkforsikringsavgift = 8.38 * 365  # kr/år for både elbil og bensinbil
drivstoffbruk_elbil = 0.2  # kWh/km
strompris = 2.00  # kr/kWh
bomavgift_elbil = 0.1  # kr/km

# Kostnader for bensinbil
forsikring_bensinbil = 7500  # kr/år
drivstoffpris_bensinbil = 1.0  # kr/km
bomavgift_bensinbil = 0.3  # kr/km

# Beregning av årlige kostnader for elbil
kostnad_elbil = (
    forsikring_elbil +
    trafikkforsikringsavgift +
    (drivstoffbruk_elbil * strompris * km_per_aar) +
    (bomavgift_elbil * km_per_aar)
)

# Beregning av årlige kostnader for bensinbil
kostnad_bensinbil = (
    forsikring_bensinbil +
    trafikkforsikringsavgift +
    (drivstoffpris_bensinbil * km_per_aar) +
    (bomavgift_bensinbil * km_per_aar)
)

# Kostnadsdifferanse
differanse = kostnad_bensinbil - kostnad_elbil

# Utskrift av resultater
print("Årlige kostnader for elbil:", round(kostnad_elbil, 2), "kr")
print("Årlige kostnader for bensinbil:", round(kostnad_bensinbil, 2), "kr")
print("Årlig kostnadsdifferanse:", round(differanse, 2), "kr")
