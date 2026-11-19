
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

    average_time = sum([np.mean(laps) for laps in lap_times]) / len(lap_times)
    print(f'Average: {average_time}')

    #Nastaveni grafu
    fig, ax = plt.subplots()

    fig.set_facecolor('#222222')  #barva pozadi cele vizualizace

    ax.set_title(f'{gp_name['name']} {gp_name['year']}', color='#EEEEEE', fontweight="bold")
    ax.set_aspect('equal')
    ax.axis('off')

    # Počáteční úsečka
    ax.plot([R - 0.5, R + 0.5], [0, 0], 'r-', linewidth=5)

    # Kružnice
    theta = np.linspace(0, 2*np.pi, 200)
    ax.plot(R*np.cos(theta), R*np.sin(theta), '#EEEEEE', linewidth=3)
    
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
                if i == 0:   
                    if lap_time > 5 * average_time:
                        fig.set_facecolor('red')  #barva pozadi cele vizualizace
                    else:
                        fig.set_facecolor('#222222')  #barva pozadi cele vizualizace

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

        return points

    # Animace
    animation = FuncAnimation(fig, update, frames=int(np.ceil(total_time * fps)) + 1, interval=1000/fps, blit=True, repeat=False)

    plt.show()
    speed_factor = speed   # Zrychleni animace