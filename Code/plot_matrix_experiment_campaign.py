import matplotlib.pyplot as plt
import numpy as np

def plot_matrix_data(matrix):
    """
    Génère un graphe à partir d'une matrice de taille n*3, avec une couleur distincte pour chaque chaîne de caractères unique.
    Generates a plot from an n*3-sized matrix, with a distinct color for each unique string.

    Paramètres / Parameters :
    - matrix : liste de listes ou tableau numpy de taille n*3 / list of lists or numpy array of size n*3
               Chaque ligne contient [omega/omegan, amplitude, couleur_str]
               Each row contains [omega/omegan, amplitude, color_str]
    """
    data = np.array(matrix, dtype=object)

    # Extraction des colonnes / Column extraction
    omega_ratio = data[:, 0].astype(float)  # ω/ωn
    amplitude = data[:, 1].astype(float)    # amplitude
    color_labels = data[:, 2]               # chaîne de caractères pour la couleur / string for the color
    
    # Association d'une couleur fixe à chaque étiquette connue / Mapping a fixed color to each known label
    color_map = {"per" : "green", "cha": "red"}
    # Association d'une légende à chaque étiquette connue / Mapping a legend to each known label
    label_map = {"per" : "periodic", "cha": "chaotic"}

    # Création du graphe / Creating the plot
    plt.figure(figsize=(10, 6))

    # Tracé des points avec la couleur associée à chaque chaîne / Plotting the points with the color associated to each string
    for label in np.unique(color_labels):
        mask = (color_labels == label)
        plt.scatter(omega_ratio[mask], amplitude[mask],
                    color=color_map.get(label, "gray"),  # gris pour une étiquette inconnue / gray for an unknown label
                    label=label_map.get(label, "unknown"),
                    s=50)

    # Légende, labels et titre / Legend, labels and title
    plt.xlabel('ω / ωn')
    plt.ylabel('Amplitude')
    plt.title('Graphe Amplitude vs ω / ωn (couleurs distinctes) / (distinct colors)')
    plt.legend(title='Catégories / Categories')
    plt.grid(True)
    plt.show()

# Exemple d'utilisation / Usage example
if __name__ == "__main__":
    # Exemple de matrice n*3 avec des chaînes de caractères
    # Example of an n*3 matrix with strings
    matrice_mesures_1 = [
        [0.40,0.01,"per"],
        [0.53,0.01,"per"],
        [0.66,0.01,"per"],
        [0.8,0.01,"per"],
        [0.93,0.01,"per"],
        [1.06,0.01,"per"],
        [1.2,0.01,"per"],
        [0.4,0.028,"per"],
        [0.53,0.028,"per"],
        [0.66,0.028,"per"],
        [0.8,0.028,"per"],
        [0.93,0.028,"per"],
        [1.06,0.028,"per"],
        [1.2,0.028,"per"],
        [0.4,0.046,"per"],
        [0.53,0.046,"per"],
        [0.66,0.046,"per"],
        [0.8,0.046,"per"],
        [0.93,0.046,"per"],
        [1.06,0.046,"per"],
        [0.40,0.064,"per"],
        [0.53,0.064,"per"],
        [0.66,0.064,"cha"],
        [0.80,0.064,"per"],
        [0.93,0.064,"cha"],
        [0.40,0.082,"per"],
        [0.53,0.082,"per"],
        [0.66,0.082,"cha"],
        [0.40,0.1,"per"],
        ]

    plot_matrix_data(matrice_mesures_1)
