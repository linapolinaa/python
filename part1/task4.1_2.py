import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 1000)

y = 5 / (x**2 - 9)

plt.figure(figsize=(10, 6))
plt.plot(x, y, 'b-', linewidth=2, label=r'$f(x) = \frac{5}{x^2 - 9}$')

plt.title('График функции $f(x) = \\frac{5}{x^2 - 9}$', fontsize=14)
plt.xlabel('x', fontsize=12)
plt.ylabel('f(x)', fontsize=12)
plt.grid(True, alpha=0.3)
plt.legend(fontsize=12)

plt.ylim(-10, 10)

plt.axvline(x=-3, color='red', linestyle='--', alpha=0.7, label='Вертикальные асимптоты')
plt.axvline(x=3, color='red', linestyle='--', alpha=0.7)

plt.legend()
plt.tight_layout()
plt.show()