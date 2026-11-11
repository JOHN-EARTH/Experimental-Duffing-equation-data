# Étude numérique de l'équation de Duffing
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# ------------------------------
# 1. Paramètres physiques
# ------------------------------
delta = 0.3       # coefficient d'amortissement
alpha = -1.0      # coefficient du terme linéaire
beta = 1.0        # coefficient du terme cubique
gamma = 0.37      # amplitude de la force excitatrice
omega = 1.2       # pulsation de la force excitatrice

# ------------------------------
# 2. Définition de l’équation différentielle
# ------------------------------
def duffing(X, t):
    """
    Équation différentielle du mouvement :
        x'' + δx' + αx + βx³ = γ cos(ωt)
    """
    x, dx = X
    ddx = -delta * dx - alpha * x - beta * x**3 + gamma * np.cos(omega * t)
    return [dx, ddx]

# ------------------------------
# 3. Conditions initiales et intégration
# ------------------------------
X0 = [0.0, 0.0]  # conditions initiales : x(0)=0, x'(0)=0
tmax = 200       # durée de la simulation
N = 10000        # nombre de points
t = np.linspace(0, tmax, N)

# Intégration de l'équation différentielle
sol = odeint(duffing, X0, t)

x = sol[:, 0]
dx = sol[:, 1]

# ------------------------------
# 4. Tracés
# ------------------------------
# a) Réponse temporelle
plt.figure()
plt.plot(t, x, color='royalblue')
plt.title("Équation de Duffing – Réponse temporelle")
plt.xlabel("Temps t")
plt.ylabel("Déplacement x(t)")
plt.grid(True)

# b) Portrait de phase
plt.figure()
plt.plot(x, dx, color='darkred')
plt.title("Portrait de phase du système de Duffing")
plt.xlabel("x(t)")
plt.ylabel("x'(t)")
plt.grid(True)

# c) Représentation de Poincaré
# (échantillonnage à chaque période de forçage)
T = 2 * np.pi / omega
indices = np.arange(int(10*T / (t[1]-t[0])), N, int(T / (t[1]-t[0])))
plt.figure()
plt.plot(x[indices], dx[indices], 'o', color='darkgreen', markersize=3)
plt.title("Section de Poincaré (système de Duffing)")
plt.xlabel("x(t)")
plt.ylabel("x'(t)")
plt.grid(True)

plt.show()
