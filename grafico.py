import matplotlib.pyplot as plt

# Dados
L = [25, 50, 75, 100, 120, 140, 150]  # cm
T = [1.01, 1.43, 1.70, 2.02, 2.19, 2.35, 2.44]  # s

# Gráfico
plt.figure(figsize=(7, 5))
plt.scatter(T, L, color='blue', label='Experimental')
plt.plot(T, L, color='magenta', label='Potência (Experimental)')
plt.title("Gráfico de T em função de L")
plt.xlabel("T (seg)")
plt.ylabel("L (cm)")
plt.legend()
plt.grid(True)
plt.show()
