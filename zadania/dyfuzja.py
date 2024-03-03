import numpy as np
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def initialize_particles(N, L):
    """Inicjalizuje cząstki na losowych pozycjach w sieci o długości L."""
    return np.random.randint(0, L, size=N)

def move_particle(position, L):
    """Przemieszcza cząstkę w lewo lub prawo z równym prawdopodobieństwem."""
    return (position - 1) % L if np.random.rand() < 0.5 else (position + 1) % L

def simulate_diffusion(N, L, num_steps):
    """Symuluje dyfuzję cząstek w sieci."""
    positions = initialize_particles(N, L)
    all_positions = [positions.copy()]
    
    for _ in range(num_steps):
        new_positions = []
        for pos in positions:
            new_positions.append(move_particle(pos, L))
        positions = np.array(new_positions)
        all_positions.append(positions.copy())
    
    return all_positions

def run_simulation():
    """Uruchamia symulację dyfuzji i wyświetla wykres."""
    N = int(num_particles_entry.get())
    L = int(grid_length_entry.get())
    num_steps = int(num_steps_entry.get())
    
    positions_over_time = simulate_diffusion(N, L, num_steps)
    
    # Wykres pozycji cząstek w czasie
    fig, ax = plt.subplots(figsize=(6, 4))
    for i, positions in enumerate(positions_over_time):
        ax.plot(positions, [i]*N, 'bo', markersize=1)
    ax.set_xlabel('Pozycja')
    ax.set_ylabel('Czas')
    ax.set_title('Symulacja dyfuzji w jednowymiarowej sieci')
    
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.grid(row=5, columnspan=3)

# Tworzenie głównego okna tkinter
window = tk.Tk()
window.title("Symulacja Dyfuzji")

# Interfejs użytkownika
tk.Label(window, text="Liczba cząstek:").grid(row=0, column=0)
num_particles_entry = tk.Entry(window)
num_particles_entry.grid(row=0, column=1)

tk.Label(window, text="Długość siatki:").grid(row=1, column=0)
grid_length_entry = tk.Entry(window)
grid_length_entry.grid(row=1, column=1)

tk.Label(window, text="Liczba kroków:").grid(row=2, column=0)
num_steps_entry = tk.Entry(window)
num_steps_entry.grid(row=2, column=1)

run_button = tk.Button(window, text="Uruchom symulację", command=run_simulation)
run_button.grid(row=3, columnspan=2)

window.mainloop()
