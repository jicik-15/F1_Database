
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def visualisation(laps_lists, speed):

    # Parametry pohybu
    R = 3           # Poloměr kružnice
    fps = 60        # Počet snímků za sekundu
    speed_factor = speed   # Zrychleni animace

    # Převod časů z ms na sekundy
    lap_times = [
        np.array(laps, dtype=float) / 1000 / speed_factor
        for laps in laps_lists
    ]

    # Celková doba animace
    total_time = max(sum(laps) for laps in lap_times)

    fig, ax = plt.subplots()

    ax.set_aspect('equal')
    ax.axis('off')

    # Počáteční úsečka
    ax.plot([R - 0.5, R + 0.5], [0, 0],
            'r-', linewidth=2)

    # Kružnice
    theta = np.linspace(0, 2*np.pi, 200)
    ax.plot(R*np.cos(theta), R*np.sin(theta), 'k-')

    # Vytvoření bodů
    colors = ['red', 'blue', 'orange', 'green', 'purple', 'yellow', 'cyan', 'magenta']

    points = []

    for i in range(len(lap_times)):
        point, = ax.plot([], [], 'o', color=colors[i % len(colors)], markersize=10)
        points.append(point)

    # Aktualizace polohy všech bodů
    def update(frame):

        t = frame / fps

        for i, laps in enumerate(lap_times):

            elapsed = 0

            for lap_time in laps:

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