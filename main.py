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
driver_names = []
gp = GrandPrix(races_data, 2012, results_data, lap_times_data, 20)
drivers = gp.drivers_per_race()
gp_name = {'name': str(gp.race_name()), 'year': 2012}

for item in drivers:
    laptimes.append(gp.driver_lap_times(item))

for i in range(len(drivers)):
    driver = Driver(drivers_data, drivers[i])
    driver_names.append(driver.driver_name())

print(driver_names)

visualisation(laptimes, 100, gp_name)