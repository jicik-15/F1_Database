
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def visualisation(laps_lists, speed, gp_name, colors):

    # Parametry pohybu
    R = 3           # Poloměr kružnice
    fps = 60        # Počet snímků za sekundu
    speed_factor = speed   # Zrychleni animace

    # Převod časů z ms na sekundy
    lap_times = [np.array(laps, dtype=float) / 1000 / speed_factor for laps in laps_lists]

    # Celková doba animace
    total_time = max(sum(laps) for laps in lap_times)

    #average_time = sum([np.mean(laps) for laps in lap_times]) / len(lap_times)
    average_time = np.mean(np.concatenate(lap_times))
    print(f'Average: {average_time}')

    #Nastaveni grafu
    fig, ax = plt.subplots()

    fig.set_facecolor('#222222')  #barva pozadi cele vizualizace

    ax.set_title(f'{gp_name['name']} {gp_name['year']}', color='#EEEEEE', fontweight="black")
    ax.set_aspect('equal')
    ax.axis('off')

    # Počáteční úsečka
    ax.plot([R - 0.5, R + 0.5], [0, 0], 'r-', linewidth=5)

    # Kružnice
    theta = np.linspace(0, 2*np.pi, 200) #vytvori 200 bodu v rozmezi 0 az 2pi
    ax.plot(R*np.cos(theta), R*np.sin(theta), '#EEEEEE', linewidth=3) #vytvori kruznici
    
    # Vytvoření bodů
    #colors = ['red', 'blue', 'orange', 'green', 'purple', 'yellow', 'cyan', 'magenta']

    #Vytvoreni bodu
    points = []
    for i in range(len(lap_times)):
        point, = ax.plot([], [], 'o', color=colors[i % len(colors)], markeredgecolor='#FFFFFF', markersize=10)
        points.append(point)
    

    # Aktualizace polohy všech bodů
    def update(frame):
        
        t = frame / fps

        for i, laps in enumerate(lap_times):

            elapsed = 0

            for lap_time in laps:

                #zmena barvy pozadi 
                if i == 0 and t < elapsed + lap_time:
                    print(1.2*average_time, lap_time, average_time)   
                    if lap_time > 2 * average_time:
                        fig.set_facecolor('#CC0000') #barva pozadi cele vizualizace
                        ax.set_title(f'RED FLAG', color='#EEEEEE', fontweight="black")

                    elif lap_time > 1.2 * average_time:
                        print(1.2*average_time, lap_time, average_time)
                        fig.set_facecolor('#F5C71A') #barva pozadi cele vizualizace
                        ax.set_title(f'SAFETY CAR', color='#EEEEEE', fontweight="black")

                                    #DODELAT: pri vypostu average_time je potreba odstranit kola pod cervenou vlajkou !!!!!!
                    else:
                        fig.set_facecolor('#222222')  #barva pozadi cele vizualizace
                        ax.set_title(f'{gp_name['name']} {gp_name['year']}', color='#EEEEEE', fontweight="black") #nastaveni nadpisu

                #---pokracovani kodu---
                
                if t < elapsed + lap_time:
                    time_in_lap = t - elapsed
                    break

                elapsed += lap_time

            else:
                # Bod dokončil všechna kola
                angle = 2 * np.pi
                x = R * np.cos(angle)
                y = R * np.sin(angle)

                points[i].set_data([x], [y])
                continue

            angle = 2 * np.pi * time_in_lap / lap_time

            x = R * np.cos(angle)
            y = R * np.sin(angle)

            points[i].set_data([x], [y])

        return points,

    # Animace
    animation = FuncAnimation(fig, update, frames=int(np.ceil(total_time * fps)) + 1, interval=1000/fps, blit=False, repeat=False)

    plt.show()
    speed_factor = speed   # Zrychleni animace