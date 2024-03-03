'''
Obliczanie liczby PI metodą Monte Carlo
K>K> 2023
'''
from random import uniform 
import matplotlib.pyplot as plt

pi = 0.0
liczbaw = 0

n = int(input("Podaj ilość punktów: "))

fig, ax = plt.subplots()
wx, wy, ox, oy = [], [], [], []
for i in range(n):
    punktx = uniform(-1,1)
    punkty = uniform(-1,1)
    if (punktx**2 + punkty **2) <= 1:
        wx.append(punktx)
        wy.append(punkty)
        liczbaw += 1
    else:
        ox.append(punktx)
        oy.append(punkty)
        
pi = float((4 * liczbaw) / n)
ax.scatter(wx, wy, alpha = 0.3, s=1, color="red")
ax.scatter(ox, oy, color="blue", s=1)

ax.grid(True)
fig.tight_layout()
plt.xticks([-1, 0, 1])
plt.yticks([-1, 0, 1])
ax.set_title(f"Pi dla n={n} wynosi {pi}")
plt.show()

    

