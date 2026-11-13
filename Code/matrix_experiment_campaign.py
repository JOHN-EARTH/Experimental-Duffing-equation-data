import numpy as np
import matplotlib.pyplot as plt

def generer_points_sous_courbe(xmin, xmax, a, b, N, ymin=0.01):
    """
    Génère un quadrillage régulier de points et filtre ceux en dessous de la courbe y = a*x + b. / Generates a regular grid of points and filters those below the curve y = a*x + b.
    Args:
        xmin (float): Valeur minimale de x. / Minimum value of x.
        xmax (float): Valeur maximale de x. / Maximum value of x.
        a (float): Coefficient directeur de la droite. / Slope of the line.
        b (float): Ordonnée à l'origine de la droite. / Y-intercept of the line.
        N (int): Nombre de points à retourner. / Number of points to return.
        ymin (float): Valeur minimale de y. / Minimum value of y.
    Returns:
        np.ndarray: Tableau de points (x, y) sous la courbe, régulièrement espacés. / Array of points (x, y) below the curve, evenly spaced.
    """
    # Generate a regular grid of points
    # Générer un quadrillage régulier de points
    nb_points_x = int(np.sqrt(N))  # Racine carrée pour un quadrillage "carré"  # Square root for a "square" grid
    nb_points_y = int(np.sqrt(N))
    x = np.linspace(xmin, xmax, nb_points_x)
    y_max = max(abs(a * xmin + b), abs(a * xmax + b)) * 1.1  # Hauteur du rectangle  # Height of the rectangle (10% margin above the line)
    y = np.linspace(ymin, y_max, nb_points_y)
    xx, yy = np.meshgrid(x, y)
    points = np.column_stack((xx.ravel(), yy.ravel()))  # Flatten the grid into a list of (x, y) points
    # Filter the points located below the curve
    # Filtrer les points sous la courbe
    sous_courbe = points[points[:, 1] <= a * points[:, 0] + b]  # Keep points where y <= a*x + b
    # Resample uniformly in the (x, y) space
    # Rééchantillonner uniformément dans l'espace (x, y)
    if len(sous_courbe) > N:
        # Sort by x then y for a uniform distribution
        # Tri par x puis y pour une répartition uniforme
        sous_courbe = sous_courbe[sous_courbe[:, 0].argsort()]  # Sort points by their x coordinate
        indices = np.linspace(0, len(sous_courbe) - 1, N, dtype=int)  # Pick N evenly spaced indices
        points_finaux = sous_courbe[indices]
    else:
        points_finaux = sous_courbe  # Retourne tous les points si moins que N  # Return all points if fewer than N
    return points_finaux

def transformer_points(points_finaux, omega_n):
    """
    Transforme les coordonnées des points selon les formules :
    Transforms the coordinates of the points according to the formulas:
    X_new = (2*pi)/(x * omega_n)
    Y_new = Y / 0.008
    Args:
        points_finaux (np.ndarray): Matrice de points (x, y). / Matrix of points (x, y).
        omega_n (float): Valeur de omega_n pour la transformation. / Value of omega_n for the transformation.
    Returns:
        np.ndarray: Matrice transformée (X_new, Y_new). / Transformed matrix (X_new, Y_new).
    """
    X = points_finaux[:, 0]
    Y = points_finaux[:, 1]
    # Transform the columns
    # Transformation des colonnes
    X_new = (2 * np.pi) / (X * omega_n)  # Convert the frequency ratio into a period
    Y_new = Y / 0.008  # Normalize the amplitude by a reference value of 0.008
    # Build the new matrix
    # Construction de la nouvelle matrice
    points_transformes = np.column_stack((X_new, Y_new))
    return points_transformes

# Usage example
# Exemple d'utilisation
xmin = 0.6
xmax = 1
a = -0.08
b = 0.14
N = 100
omega_n = 10.48
ymin = 0.06  # Limite basse pour y  # Lower bound for y

points = generer_points_sous_courbe(xmin, xmax, a, b, N, ymin)
print("Matrice des points sous la courbe :")
print(points)
print(np.shape(points))

X = np.linspace(xmin, xmax, 1000)
plt.scatter(points[:, 0], points[:, 1], color="blue", label="Points sous la courbe")
plt.plot(X, (a*X + b), '-r')
plt.xlabel(r'$\frac{\omega}{\omega_n}$')
plt.ylabel('amplitude (m)')
plt.title(r'Points sous la courbe y = -0.08x + 0.14')
plt.legend()
plt.show()