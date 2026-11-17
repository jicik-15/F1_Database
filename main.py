import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from database import Circuit, Season, GrandPrix, Driver, Career
from visualisation import visualisation

circuits_data = pd.read_csv('circuits.csv', sep=',')        # nacteni tabulky pomoci knihovny pandas, separator = ','
races_data = pd.read_csv('races.csv', sep=',')
drivers_data = pd.read_csv('drivers.csv', sep=',')
results_data = pd.read_csv('results.csv', sep=',')
lap_times_data = pd.read_csv('lap_times.csv', sep=',')

#TEST
laptimes = []
drivers = [1, 830, 846, 844, 832, 822]
gp = GrandPrix(races_data, 2021, results_data, lap_times_data, 22)
for item in drivers:
    laptimes.append(gp.driver_lap_times(item))

visualisation(laptimes, 100)