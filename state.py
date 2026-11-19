

class RaceState:

    def __init__(self, circuit):
        self.circuit = circuit
        self.safetycar_factor = {'jeddah': 1.15} #slovnik obsahujici o kolik se zvetsi cas kola pri safetycaru na danem okruhu

    def safetycar_time(self):
        #pokud je circuit ve slovniku, vrati jeho hodnotu nasobku casu, jinak vrati hodnotu 1.4
        if self.circuit in self.safetycar_factor.keys():
            return self.safetycar_factor[self.circuit]

        else:
            return 1.4

