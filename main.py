import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk


def run_simulation():
    try:
        lam = float(entry_lambda.get())
        samples = int(entry_samples.get())
        delays = np.random.exponential(1 / lam, samples)

        plt.figure(figsize=(8, 4))
        plt.hist(delays, bins=30, color='lightgreen', edgecolor='black', density=True)
        plt.title(f"Розподіл затримок (λ={lam}, N={samples})")
        plt.xlabel("Затримка")
        plt.ylabel("Щільність")
        plt.grid(True)
        plt.show()
    except ValueError:
        print("Неправильні вхідні дані")


# GUI
root = tk.Tk()
root.title("Модель затримки Монте-Карло")

tk.Label(root, text="λ (інтенсивність):").grid(row=0, column=0)
entry_lambda = ttk.Entry(root)
entry_lambda.insert(0, "0.5")
entry_lambda.grid(row=0, column=1)

tk.Label(root, text="Кількість симуляцій:").grid(row=1, column=0)
entry_samples = ttk.Entry(root)
entry_samples.insert(0, "1000")
entry_samples.grid(row=1, column=1)

btn = ttk.Button(root, text="Побудувати графік", command=run_simulation)
btn.grid(row=2, column=0, columnspan=2)

root.mainloop()
