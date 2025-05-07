import numpy as np
import matplotlib.pyplot as plt

# Параметри симуляції
lam = 0.2
samples = 1000

# Генерація експоненційно розподілених затримок
delays = np.random.exponential(1 / lam, samples)

# Обчислення середнього значення (мат. сподівання) та дисперсії
mean_delay = np.mean(delays)
var_delay = np.var(delays)

# Побудова гістограми
plt.figure(figsize=(8, 4))
plt.hist(delays, bins=30, color='lightgreen', edgecolor='black', density=True)
plt.title(f"Гістограма розподілу затримок (λ={lam}, N={samples})")
plt.xlabel("Затримка")
plt.ylabel("Щільність")
plt.grid(True)
plt.show()

# Побудова лінії середнього значення
plt.figure(figsize=(8, 4))
plt.hist(delays, bins=30, color='lightgrey', edgecolor='black', density=True)
plt.axvline(mean_delay, color='blue', linestyle='dashed', linewidth=2, label=f"E[τ] = {mean_delay:.2f}")
plt.title("Середнє значення (мат. сподівання)")
plt.xlabel("Затримка")
plt.ylabel("Щільність")
plt.legend()
plt.grid(True)
plt.show()

# Побудова розкиду навколо середнього (±σ)
std_dev = np.sqrt(var_delay)
plt.figure(figsize=(8, 4))
plt.hist(delays, bins=30, color='lightgrey', edgecolor='black', density=True)
plt.axvline(mean_delay, color='blue', linestyle='dashed', linewidth=2, label=f"E[τ] = {mean_delay:.2f}")
plt.axvline(mean_delay + std_dev, color='red', linestyle='dotted', linewidth=2, label=f"+σ = {std_dev:.2f}")
plt.axvline(mean_delay - std_dev, color='red', linestyle='dotted', linewidth=2, label=f"-σ = {std_dev:.2f}")
plt.title("Дисперсія (розкиди навколо середнього)")
plt.xlabel("Затримка")
plt.ylabel("Щільність")
plt.legend()
plt.grid(True)
plt.show()
