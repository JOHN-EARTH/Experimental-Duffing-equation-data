import os

def renommer_videos(dossier, matrice):
    # Liste des fichiers vidéo dans le dossier
    fichiers = [f for f in os.listdir(dossier) if os.path.isfile(os.path.join(dossier, f))]
    extensions_video = ('.mp4', '.avi', '.mov', '.mkv')
    fichiers_video = [f for f in fichiers if f.lower().endswith(extensions_video)]
    fichiers_video.sort()  # Trier les fichiers

    # Vérifier que le nombre de fichiers est un multiple de 3
    if len(fichiers_video) % 3 != 0:
        print("Le nombre de vidéos n'est pas un multiple de 3. Vérifie ta matrice ou tes fichiers.")
        return

    # Parcourir la matrice et renommer les fichiers
    index = 0
    for omega, amplitude in matrice:
        for num_test in range(1, 4):
            if index >= len(fichiers_video):
                break
            nouveau_nom = f"{omega}_{amplitude}_VID_{num_test}_30_G"
            ancien_chemin = os.path.join(dossier, fichiers_video[index])
            extension = os.path.splitext(fichiers_video[index])[1]
            nouveau_chemin = os.path.join(dossier, nouveau_nom + extension)
            os.rename(ancien_chemin, nouveau_chemin)
            print(f"Renommé : {fichiers_video[index]} -> {nouveau_nom}{extension}")
            index += 1

# Exemple d'utilisation
dossier = "C:\\Users\\andy9\\Projet\\Video\\Matrice_2_video"  # Remplace par le chemin de ton dossier
matrice = [[0.6      ,  0.06      ],
 [0.64444444, 0.06      ],
 [0.68888889, 0.06      ],
 [0.73333333, 0.06      ],
 [0.77777778, 0.06      ],
 [0.82222222, 0.06      ],
 [0.86666667, 0.06      ],
 [0.91111111, 0.06      ], 
 [0.95555556, 0.06      ], 
 [1.        , 0.06      ],
 [0.6       , 0.06457778],
 [0.64444444, 0.06457778],
 [0.68888889, 0.06457778],
 [0.73333333, 0.06457778],
 [0.77777778, 0.06457778],
 [0.82222222, 0.06457778],
 [0.86666667, 0.06457778],
 [0.91111111, 0.06457778],
 [0.6       , 0.06915556],
 [0.64444444, 0.06915556],
 [0.68888889, 0.06915556],
 [0.73333333, 0.06915556],  
 [0.77777778, 0.06915556],
 [0.82222222, 0.06915556], 
 [0.86666667, 0.06915556],
 [0.6       , 0.07373333],
 [0.64444444, 0.07373333],
 [0.68888889, 0.07373333],
 [0.73333333, 0.07373333],
 [0.77777778, 0.07373333], 
 [0.82222222, 0.07373333],
 [0.6       , 0.07831111],
 [0.64444444, 0.07831111],
 [0.68888889, 0.07831111],
 [0.73333333, 0.07831111],
 [0.6       , 0.08288889],
 [0.64444444, 0.08288889],
 [0.68888889, 0.08288889],
 [0.6       , 0.08746667],
 [0.64444444, 0.08746667]]

renommer_videos(dossier, matrice)
