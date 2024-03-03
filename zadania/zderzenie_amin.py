import numpy as np
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.animation as animation
import matplotlib.pyplot as plt

class GasSimulator:
    def __init__(self, width, height, num_atoms):
        self.width = width
        self.height = height
        self.num_atoms = num_atoms
        self.positions = np.random.rand(self.num_atoms, 2) * [width, height]
        self.velocities = np.random.randn(self.num_atoms, 2)

    def update(self):
        self.positions += self.velocities
        for i in range(self.num_atoms):
            if self.positions[i, 0] < 0 or self.positions[i, 0] > self.width:
                self.velocities[i, 0] *= -1
            if self.positions[i, 1] < 0 or self.positions[i, 1] > self.height:
                self.velocities[i, 1] *= -1

    def init_animation(self):
        self.scatter.set_offsets([])  # Czyszczenie punktów przed animacją
        return self.scatter,

    def animate(self, i):
        self.update()
        self.scatter.set_offsets(self.positions)
        return self.scatter,

    def start_animation(self, ax):
        self.scatter = ax.scatter(self.positions[:, 0], self.positions[:, 1], s=50)
        ani = animation.FuncAnimation(fig, self.animate, frames=200, interval=50, blit=True, init_func=self.init_animation)
        return ani

def start_simulation():
    width = int(width_entry.get())
    height = int(height_entry.get())
    num_atoms = int(num_atoms_entry.get())

    simulator = GasSimulator(width, height, num_atoms)
    ani = simulator.start_animation(ax)
    
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.grid(row=1, columnspan=3)

# Tworzenie głównego okna tkinter
window = tk.Tk()
window.title("Animacja Zderzeń Atomów")

# Interfejs użytkownika
tk.Label(window, text="Szerokość pudła:").grid(row=0, column=0)
width_entry = tk.Entry(window)
width_entry.grid(row=0, column=1)

tk.Label(window, text="Wysokość pudła:").grid(row=0, column=2)
height_entry = tk.Entry(window)
height_entry.grid(row=0, column=3)

tk.Label(window, text="Liczba atomów:").grid(row=0, column=4)
num_atoms_entry = tk.Entry(window)
num_atoms_entry.grid(row=0, column=5)

start_button = tk.Button(window, text="Uruchom animację", command=start_simulation)
start_button.grid(row=0, columnspan=6)

# Tworzenie wykresu
fig, ax = plt.subplots(figsize=(6, 4))
ax.set_xlim(0, 100)  # Dla przykładu ustawiamy zakres x i y na 100
ax.set_ylim(0, 100)
ax.set_title('Animacja Zderzeń Atomów')

window.mainloop()
