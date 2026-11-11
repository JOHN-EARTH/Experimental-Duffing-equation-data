# Détermination du taux d’amortissement d’un oscillateur
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

# --------------------------------------------
# 1. Importation et préparation des données
# --------------------------------------------
# Exemple : chargement d'un fichier CSV contenant les colonnes [time, position]
data = np.loadtxt('oscillateur_libre.csv', delimiter=',', skiprows=1)
t = data[:, 0]        # temps (s)
x = data[:, 1]        # position (m)

# --------------------------------------------
# 2. Détection des maxima successifs
# --------------------------------------------
# Recherche des pics de la courbe x(t)
peaks, _ = find_peaks(x)
t_peaks = t[peaks]
x_peaks = x[peaks]

# --------------------------------------------
# 3. Calcul du taux d’amortissement
# --------------------------------------------
# Méthode : logarithmic decrement
# δ = (1/n) * ln(x_i / x_{i+n})
# ζ = δ / sqrt(4π² + δ²)
n = 1  # nombre d’oscillations entre deux pics
delta_vals = np.log(x_peaks[:-n] / x_peaks[n:])
delta_mean = np.mean(delta_vals)

# Calcul du taux d’amortissement ζ
zeta = delta_mean / np.sqrt(4 * np.pi**2 + delta_mean**2)

print(f"Décrément logarithmique moyen δ = {delta_mean:.4f}")
print(f"Taux d’amortissement ζ = {zeta:.4f}")

# --------------------------------------------
# 4. Visualisation
# --------------------------------------------
plt.figure()
plt.plot(t, x, label="Signal mesuré")
plt.plot(t_peaks, x_peaks, 'ro', label="Pics détectés")
plt.xlabel("Temps (s)")
plt.ylabel("Amplitude (m)")
plt.title("Détermination du taux d’amortissement")
plt.legend()
plt.grid(True)
plt.show()
