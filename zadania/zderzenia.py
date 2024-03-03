import numpy as np
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

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

    def simulate(self, num_steps):
        all_positions = [self.positions.copy()]
        for _ in range(num_steps):
            self.update()
            all_positions.append(self.positions.copy())
        return all_positions

def run_simulation():
    width = int(width_entry.get())
    height = int(height_entry.get())
    num_atoms = int(num_atoms_entry.get())
    num_steps = int(num_steps_entry.get())

    simulator = GasSimulator(width, height, num_atoms)
    positions_over_time = simulator.simulate(num_steps)

    fig, ax = plt.subplots(figsize=(6, 4))
    for positions in positions_over_time:
        ax.scatter(positions[:, 0], positions[:, 1], s=10)
        ax.set_xlim(0, width)
        ax.set_ylim(0, height)
    ax.set_title('Symulacja zderzeń atomów w pudle')
    
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.grid(row=5, columnspan=3)

# Tworzenie głównego okna tkinter
window = tk.Tk()
window.title("Symulacja Zderzeń Atomów")

# Interfejs użytkownika
tk.Label(window, text="Szerokość pudła:").grid(row=0, column=0)
width_entry = tk.Entry(window)
width_entry.grid(row=0, column=1)

tk.Label(window, text="Wysokość pudła:").grid(row=1, column=0)
height_entry = tk.Entry(window)
height_entry.grid(row=1, column=1)

tk.Label(window, text="Liczba atomów:").grid(row=2, column=0)
num_atoms_entry = tk.Entry(window)
num_atoms_entry.grid(row=2, column=1)

tk.Label(window, text="Liczba kroków:").grid(row=3, column=0)
num_steps_entry = tk.Entry(window)
num_steps_entry.grid(row=3, column=1)

run_button = tk.Button(window, text="Uruchom symulację", command=run_simulation)
run_button.grid(row=4, columnspan=2)

window.mainloop()
