

class RaceState:

    def __init__(self, race_laps, circuit = 'test'):
        self.circuit = circuit
        self.race_laps = race_laps
        self.safetycar_factor = {'jeddah': 1.15} #slovnik obsahujici o kolik se zvetsi cas kola pri safetycaru na danem okruhu

    def safetycar_time(self):
        #pokud je circuit ve slovniku, vrati jeho hodnotu nasobku casu, jinak vrati hodnotu 1.4
        if self.circuit in self.safetycar_factor.keys():
            return self.safetycar_factor[self.circuit]

        else:
            return 1.4

    def average(self): #NEFUNGUJE!!!
        avrage_per_lap = []
        for i in range(len(self.race_laps)):
            sum = 0
            count = 0
            for item in self.race_laps[i]:
                sum += item
                count += 1

            avrage_per_lap.append(sum/count)
        return avrage_per_lap
    

    def race_state(self):
        if self.race_laps > 2 * average_time:
            fig.set_facecolor('#CC0000') #barva pozadi cele vizualizace
            ax.set_title(f'RED FLAG', color='#EEEEEE', fontweight="black")
        
        elif self.race_laps > 1.2 * average_time:
            fig.set_facecolor('#F5C71A') #barva pozadi cele vizualizace
            ax.set_title(f'SAFETY CAR', color='#EEEEEE', fontweight="black")
        
                #DODELAT: pri vypostu average_time je potreba odstranit kola pod cervenou vlajkou !!!!!!
        else:
            fig.set_facecolor('#222222')  #barva pozadi cele vizualizace
            ax.set_title(f'{gp_name['name']} {gp_name['year']}', color='#EEEEEE', fontweight="black") #nastaveni nadpisu
        ...

class LaptimesCleanup:

    def __init__(self, laptimes):
        self.laptimes = laptimes #laptimes je list listů

    def remove_empty_lists(self):
        clean_laptimes = []
        for item in self.laptimes:
            if len(item) > 0:
                clean_laptimes.append(item)

        return clean_laptimes
                
    
    def average(self):
        sum = 0
        length = 0
        for i in range(len(self.laptimes)):
            for item in self.laptimes[i]:
                sum += item
                length += 1

        return (sum / length)
        
            
    def time_remove(self, time_multiplication):
        #odstrani z laptimes vybrane casy na kolo podle velikosti time_multiplication
        laptimes = self.remove_empty_lists()
        print(f'\nTEST:{laptimes}:END_TEST\n')
        average_time = self.average()
        for i in range(len(laptimes)):
            for j in range(len(laptimes[i])):
                if laptimes[i][j] > time_multiplication * average_time: #DODELAT!!!
                    laptimes[i][j] = int(average_time)

        return laptimes

    
