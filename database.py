import pandas as pd
import sys

class Circuit:

    def __init__(self, database, id):
        self.database = database
        self.id = id
        self.circuit_id = id + 1    # jelikoz id okruhuu zacina na cisle 1, ale prvni radek ma index 0, pricitam k id +1
        self.name = database.loc[id, 'name']
        self.location = database.loc[id, 'location']
        self.country = database.loc[id, 'country']
        self.elevation = database.loc[id, 'alt']

    def __repr__(self):
        return f"The circuit {self.name} is located in {self.location} in {self.country} at the altitude of {self.elevation} meters."
    

    def altitude(self):
        # metoda najde nadmorskou vysku pro zvoleny okruh
        return self.database.loc[self.id,'alt']

    def max_altitude(self):
        return self.database['alt'].max()

    def min_altitude(self):
        return self.database['alt'].min()

class Season:

    def __init__(self, database, year):
        self.database = database
        self.year = year
        self.circuits_id = []
        self.circuits_name = []


    def race_id_per_season(self):
        #metoda vrati id vsech zavodu v dane sezone
        race_id = []
        count = 0

        for i in range(len(self.database)):
            if count < 25: #aby se nemuselo prochazet cele pole, kdyz uz neni zadna pozadovana hodnota (max pocet zavodu v sezone je 24)
                if self.database.loc[i, 'year'] == self.year:
                    race_id.append(int(self.database.loc[i, 'raceId']))
                    count += 1
                else:
                    pass
        
        return race_id
    

    def season_lenght(self):
        #vrati pocet zavodu v jedne sezone
        lenght = len(self.race_id_per_season())
        return lenght
    

    def race_name_per_season(self):
        #vrati nazev jednotlivych zavodu
        id_list = self.race_id_per_season()
        gp_list = []

        for item in id_list:
            gp_name = self.database.loc[self.database['raceId'] == item, 'name'].iloc[0]
            gp_list.append(str(gp_name))

        return gp_list
    

    def race_info(self, requested_info):
        #vrati hodnoty libovolneho sloupce pro kazdy zavod v danem roce
        id_list = self.race_id_per_season()
        info_list = []

        for item in id_list:
            info = self.database.loc[self.database['raceId'] == item, requested_info].iloc[0]
            info_list.append(info)

        return info_list


class GrandPrix(Season):

    def __init__(self, database, year, results_data, lap_times_data, round):
        super().__init__(database, year)
        self.results_data = results_data
        self.lap_times_data = lap_times_data
        self.round = round
        if self.round > 24:
            print(f'Number of rounds exceeded. Maximum number of rounds in a season is 24.')
            sys.exit()

    def grand_prix_id(self):
        #urci 'raceId' konkretni velke ceny
        if self.round <= self.season_lenght():
            race_id = self.database.loc[(self.database['year'] == self.year) & (self.database['round'] == self.round), 'raceId'].iloc[0]
            return race_id

        else:
            print(f'Number of rounds exceeded. The {self.year} season had only {self.season_lenght()} rounds.')
            sys.exit()

    def lap_count(self):
        #urceni poctu odjetych kol v konkretnim zavode
        race_id = self.grand_prix_id()
        race = self.lap_times_data.loc[self.lap_times_data['raceId'] == race_id]
        
        return race['lap'].max()

    def driver_lap_times(self, driver_id, milliseconds = True):
        #vrati seznam obsahujici jednotlive casy na kolo, a to budto v milisekundach nebo v normalnim zapise casu (string)
        if self.year < 1982:
            print(f'Lap time data befor the year 1982 does not exist.')
            sys.exit()

        race_id = self.grand_prix_id()
        lap_times = []
        race_rows = self.lap_times_data.loc[(self.lap_times_data['raceId'] == race_id) & (self.lap_times_data['driverId'] == driver_id)] #najde radky, kde jsou splneny obe podminky
        for i in range(len(race_rows)):
            if milliseconds:
                lap_times.append(int(race_rows.iloc[i]['milliseconds'])) #prida do seznamu hodnotu 'milliseconds' pro radek 'i'
            
            elif milliseconds == False:
                lap_times.append(str(race_rows.iloc[i]['time'])) #prida do seznamu hodnotu 'time' pro radek 'i'

        return lap_times

    def driver_race_time(self, driver_id):

        return sum(self.driver_lap_times(driver_id))

    def drivers_per_race(self):
        #vrati seznam pilotu v danem zavode
        race_id = self.grand_prix_id()
        drivers = []
        driver_rows = self.results_data.loc[self.results_data['raceId'] == race_id, 'driverId'] #najde sloupec s hodnotou 'driverId'
        for item in driver_rows:
            drivers.append(int(item))
    
        return drivers

    def constructors_per_race(self, repeat = False):
        #vrati seznam konstrukteru v danem zavode, pokud je repeat == False, vrati kazdeho konstruktora pouze jednou, pokud je True, vrati vsechny vyskyty vsech konstruktoru
        race_id = self.grand_prix_id()
        constructors = []
        constructor_rows = self.results_data.loc[self.results_data['raceId'] == race_id, 'constructorId'] #najde sloupec s hodnotou 'constructorId'
        if repeat == False:
            for item in constructor_rows:
                if item not in constructors:
                    constructors.append(int(item))

        elif repeat:
            for item in constructor_rows:
                constructors.append(int(item))

        return constructors

    def race_name(self):
        #vrati nazev konkretniho zavodu
        race_id = self.grand_prix_id()
        gp_name = self.database.loc[self.database['raceId'] == race_id, 'name'].iloc[0]
                
        return gp_name

    def race_info(self, requested_info):
        #vrati zvolenou hodnotu z datasetu
        race_id = self.grand_prix_id()
        info = self.database.loc[self.database['raceId'] == race_id, requested_info].iloc[0]
        return info


class Driver:
    #trida zpracuje databazi drivers.csv a vytahne z ni pozadovane hodnoty

    def __init__(self, database, driver):
        self.database = database
        self.driver = driver

        row = self.database.loc[database['driverId'] == driver].iloc[0] #vrati prvni hodnotu z radku, kde hodnota 'driverId' == driver

        self.driver_id = row['driverId']
        self.driver_ref = row['driverRef']
        self.driver_number = row['number']
        self.driver_code = row['code']
        self.forename = row['forename']
        self.surname = row['surname']
        self.birthday = row['dob']
        self.nationality = row['nationality']

    def __repr__(self):
        return f'{self.forename} {self.surname} is a {self.nationality} driver. Their racing number is {self.driver_number}.'

    def driver_name(self):
        return self.driver_ref

class Constructors:
    #trida zpracuje databazi constructors.csv a vytahne z ni data

    def __init__(self, constructors_data, constructor):
        #init tridy Constructors, jako vstupni promenna constructor muze byt bud id Konstruktora nebo jeho referencni jmeno(viz constructors.csv)
        self.constructors_data = constructors_data
        self.constructor = constructor

    def constructor_info(self, requested_info):
        if isinstance(self.constructor, list): #kontroluje, zdali je promenna self.constructor typu list
            info = []
            for item in self.constructor:
                if requested_info == 'id':
                    info.append(self.constructors_data.loc[(self.constructors_data['constructorId'] == item) | (self.constructors_data['constructorRef'] == item), 'constructorId'].iloc[0])
                
                if requested_info == 'name':
                    info.append(self.constructors_data.loc[(self.constructors_data['constructorId'] == item) | (self.constructors_data['constructorRef'] == item), 'name'].iloc[0])
                
                if requested_info == 'ref':
                    info.append(self.constructors_data.loc[(self.constructors_data['constructorId'] == item) | (self.constructors_data['constructorRef'] == item), 'constructorRef'].iloc[0])

        elif isinstance(self.constructor, (str, int)): #kontroluje, zdali je promenna self.constructor typu str nebo int
            if requested_info == 'id':
                info = self.constructors_data.loc[(self.constructors_data['constructorId'] == self.constructor) | (self.constructors_data['constructorRef'] == self.constructor), 'constructorId'].iloc[0]

            if requested_info == 'name':
                info = self.constructors_data.loc[(self.constructors_data['constructorId'] == self.constructor) | (self.constructors_data['constructorRef'] == self.constructor), 'name'].iloc[0]

            if requested_info == 'ref':
                info = self.constructors_data.loc[(self.constructors_data['constructorId'] == self.constructor) | (self.constructors_data['constructorRef'] == self.constructor), 'constructorRef'].iloc[0]

        else:
            info = []
            print(f'Wrong type')

        return info



class Career(GrandPrix):

    def __init__(self, database, driver_id):
        self.database = database
        self.driver = driver_id