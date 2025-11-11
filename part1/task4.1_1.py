import matplotlib.pyplot as plt
import numpy as np

x_degrees = np.linspace(-360, 360, 1000)
x_radians = np.radians(x_degrees)

cos_x = np.cos(x_radians)
sin_x = np.sin(x_radians)
cos_06x = np.cos(0.6 * x_radians)

f_x = np.exp(cos_x) + np.log(cos_06x**2 + 1) * sin_x
h_x = -np.log((cos_x + sin_x)**2 + 2.5) + 10

plt.figure(figsize=(14, 10))

plt.subplot(2, 1, 1)
plt.plot(x_degrees, f_x, "b-", linewidth=2)
plt.title("f(x)")
plt.xlabel("Градусы")
plt.ylabel("f(x)")
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(x_degrees, h_x, "r-", linewidth=2)
plt.title("h(x)")
plt.xlabel("Градусы")
plt.ylabel("h(x)")
plt.grid(True)

plt.tight_layout()
plt.savefig('part1/task4..1_1_plot.png')
plt.show()