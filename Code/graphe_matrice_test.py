import matplotlib.pyplot as plt
import numpy as np

def plot_matrix_data(matrix):
    """
    Génère un graphe à partir d'une matrice de taille n*3, avec une couleur distincte pour chaque chaîne de caractères unique.

    Paramètres :
    - matrix : liste de listes ou tableau numpy de taille n*3
               Chaque ligne contient [omega/omegan, amplitude, couleur_str]
    """
    data = np.array(matrix, dtype=object)

    # Extraction des colonnes
    omega_ratio = data[:, 0].astype(float)  # ω/ωn
    amplitude = data[:, 1].astype(float)    # amplitude
    color_labels = data[:, 2]               # chaîne de caractères pour la couleur

    # Détermination des couleurs uniques et association à une couleur fixe
    unique_colors = np.unique(color_labels)
    color_map = {
        unique_colors[0]: 'red',
        #unique_colors[1]: 'blue',
        unique_colors[1]: 'white', #on a que 2 types de données ("cha" et "per") mais Python essaie d'en detecter 3 donc on a crée un point fantôme en bout de matrice qui est tracé en blanc pour préserver l'esthètique du graphe.
        unique_colors[2]: 'green',
    }

    # Création du graphe
    plt.figure(figsize=(10, 6))

    # Tracé des points avec la couleur associée à chaque chaîne
    for label in unique_colors:
        mask = (color_labels == label)
        plt.scatter(omega_ratio[mask]
            ,amplitude[mask]
            ,
            color=color_map[label],
            label=label,
            s=50
        )

    # Légende, labels et titre
    plt.xlabel('ω / ωn')
    plt.ylabel('Amplitude')
    plt.title('Graphe Amplitude vs ω / ωn (couleurs distinctes)')
    plt.legend(title='Catégories')
    plt.grid(True)
    plt.show()

# Exemple d'utilisation
if __name__ == "__main__":
    # Exemple de matrice n*3 avec des chaînes de caractères
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
        [0.40,0.0,"null"] #le point fantôme
        ]

    plot_matrix_data(matrice_mesures_1)
