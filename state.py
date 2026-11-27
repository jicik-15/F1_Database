

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

    def average(self):
        #vypocita prumernou delku daneho kola v zavode z casu vsech jezdcu
        average_per_lap = []
        count = []

        average_per_lap.append(self.race_laps[0])

        for i in range(len(average_per_lap[0])):
            count.append(0)

        for item in self.race_laps:
            for i in range(len(item)):
                average_per_lap[0][i] += item[i]
                count[i] += 1

        print(f'Average: {average_per_lap} :Average END')

        for i in range(len(average_per_lap[0])):
            average_per_lap[0][i] = average_per_lap[0][i] / count[i]

        print(f'Count: {count} :Count END')
        return average_per_lap
    

    def race_state(self):
        #vrati stav zavodu pro kazde kolo
        status = []
        laptimes = self.average()
        average_time = LaptimesCleanup(laptimes).average()
        if laptimes > 2 * average_time:
            laptimes.append('red_flag')
            
        elif laptimes > 1.2 * average_time:
            laptimes.append('yellow_flag')
            #DODELAT: pri vypostu average_time je potreba odstranit kola pod cervenou vlajkou !!!!!!
        else:
            laptimes.append('green_flag')
            

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

    
