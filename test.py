import pandas as pd

import database as db
import visualisation as vis
import colours as col
import state as st

circuits_data = pd.read_csv('circuits.csv', sep=',')        # nacteni tabulky pomoci knihovny pandas, separator = ','
races_data = pd.read_csv('races.csv', sep=',')
drivers_data = pd.read_csv('drivers.csv', sep=',')
results_data = pd.read_csv('results.csv', sep=',')
lap_times_data = pd.read_csv('lap_times.csv', sep=',')
constructors_data = pd.read_csv('constructors.csv', sep=',')


year = 2021
round_id = 21
gp = db.GrandPrix(races_data, year, results_data, lap_times_data, round_id)
colours = col.Colours(constructors_data)
constructors = gp.constructors_per_race(True)
drivers = gp.drivers_per_race()
gp_name = {'name': str(gp.race_name()), 'year': year}

lap_times = []
for item in drivers:
    lap_times.append(gp.driver_lap_times(item))

constructor_names = []
constructor_colours = []
for i in range(len(constructors)): #tento if uz neni potreba, nahrazeno vylepsenou metodou constructor_info
    const = db.Constructors(constructors_data, constructors[i])
    constructor_names.append(const.constructor_info('ref'))
    colours = col.Colours(const.constructor_info('ref'))
    constructor_colours.append(colours.colours_per_constructor())

print(lap_times)
cleanup = st.LaptimesCleanup(lap_times)
lap_clean = cleanup.remove_empty_lists()
lap_removed = cleanup.time_remove(2.5)

print(constructors)
#print(lap_clean)
print(lap_removed)
print(type('name'))

#vis.visualisation(lap_times, 100, gp_name, constructor_colours)
#vis.visualisation(lap_clean, 100, gp_name, constructor_colours)

const1 = db.Constructors(constructors_data, 1)
const2 = db.Constructors(constructors_data, 'mclaren')
const3 = db.Constructors(constructors_data, [1, 2])
const4 = db.Constructors(constructors_data, 1.1)

print(const1.constructor_info('ref'))
print(const2.constructor_info('ref'))
print(const3.constructor_info('ref'))
print(const4.constructor_info('ref'))

const_test = db.Constructors(constructors_data, constructors)
print(const_test.constructor_info('ref'))

