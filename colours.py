import random

class Colours:

    def __init__(self,constructors):
        self.constructors = constructors
        self.colours = {'mclaren':'#FF8000', 'ferrari':'#E80020', 'red_bull':'#3671C6', 'mercedes':'#27F4D2', 'aston_martin':'#00665E','alpine':'#0090FF',
                        'williams':'#64C4FF','rb':'#6692FF','haas':'#FFFFFF','audi':'#C8CED4','cadillac':'#000000', 'sauber':'#00E701','alphatauri':'#1E5BC6',
                        'renault':'#FFF500','racing_point':'#F596C8','alfa':'#981E32','force_india':'#EC0374','toro_rosso':'#00144A','manor':'#006DC1',
                        'lotus_f1':'#B6995B','caterham':'#005030','marussia':'#B52921','hrt':'#D6C39A','lotus_racing':'#174222'}

    def colours_per_constructor(self):
        #vrati barvu prislusici danemu konstrukterovi
        if self.constructors in self.colours.keys():
            return self.colours[self.constructors]

        else:
            self.colours[self.constructors] = random.choice(['red', 'blue', 'orange', 'green', 'purple', 'yellow', 'cyan', 'magenta'])
            return self.colours[self.constructors]

#TEST
#col = Colours('mclaren')
#print(col.colours_per_constructor())
#print(col.colours)

#col2 = Colours('mclaren1')
#print(col2.colours_per_constructor())
#print(col2.colours)