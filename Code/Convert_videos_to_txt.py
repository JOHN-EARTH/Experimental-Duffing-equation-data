import os
import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import imutils
from datetime import datetime

def extraire_infos_nom_fichier(nom_fichier):
    nom_sans_extension = os.path.splitext(nom_fichier)[0]
    parties = nom_sans_extension.split('_')
    omega = parties[0]
    amplitude = parties[1]
    numerotest = parties[3]
    durée = parties[4]
    puit = parties[5]
    return omega, amplitude, numerotest, durée, puit

def extraire_coordonnees(video_path):
    # Paramètres de détection
    lower_red = np.array([170, 70, 50])
    upper_red = np.array([180, 255, 255])
    lower_green = np.array([30, 50, 50])
    upper_green = np.array([90, 255, 255])
    MIN_RADIUS = 2

    # Charger la vidéo
    cap = cv2.VideoCapture(video_path)
    framerate = cap.get(cv2.CAP_PROP_FPS)

    # DataFrame pour stocker les données
    data_features = ['time', 'color', 'cx', 'cy']
    data_pts = pd.DataFrame(data=None, columns=data_features, dtype=float)

    while True:
        success, img = cap.read()
        if not success:
            break

        current_time = cap.get(cv2.CAP_PROP_POS_MSEC) / 1000
        img = imutils.resize(img, width=640)
        img_filter = cv2.GaussianBlur(img.copy(), (3, 3), 0)
        img_filter = cv2.cvtColor(img_filter, cv2.COLOR_BGR2HSV)

        # Masques pour les balles rouge et verte
        mask_red = cv2.inRange(img_filter.copy(), lower_red, upper_red)
        mask_green = cv2.inRange(img_filter.copy(), lower_green, upper_green)

        # Érosion et dilatation
        mask_red = cv2.erode(mask_red, None, iterations=2)
        mask_red = cv2.dilate(mask_red, None, iterations=2)
        mask_green = cv2.erode(mask_green, None, iterations=2)
        mask_green = cv2.dilate(mask_green, None, iterations=2)

        # Détection des contours
        for mask, color_name in [ (mask_red, "red"), (mask_green, "green") ]:
            contours = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
            if contours:
                c = max(contours, key=cv2.contourArea)
                ((x, y), radius) = cv2.minEnclosingCircle(c)
                M = cv2.moments(c)
                if M["m00"] > 0 and radius >= MIN_RADIUS:
                    center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
                    data_pts.loc[len(data_pts)] = [current_time, color_name, center[0], center[1]]

    cap.release()
    return data_pts

def creer_fichiers_data(dossier_source, dossier_destination, auteurs="Flavio Samson & Andy Wong"):
    os.makedirs(dossier_destination, exist_ok=True)
    fichiers = [f for f in os.listdir(dossier_source) if os.path.isfile(os.path.join(dossier_source, f))]
    extensions_video = ('.mp4', '.avi', '.mov', '.mkv', '.MOV')  # Ajout de .MOV pour couvrir toutes les extensions possibles
    fichiers_video = [f for f in fichiers if f.lower().endswith(extensions_video)]

    # Vérification des fichiers vidéo
    print(f"Fichiers vidéo détectés : {fichiers_video}")

    for fichier in fichiers_video:
        try:
            omega, amplitude, numerotest, durée, puit = extraire_infos_nom_fichier(fichier)
            nom_data = f"{omega}_{amplitude}_DATA_{numerotest}_{durée}_{puit}.txt"
            chemin_data = os.path.join(dossier_destination, nom_data)

            # Extraire les coordonnées
            data_pts = extraire_coordonnees(os.path.join(dossier_source, fichier))

            # Filtrer les données pour les balles verte et rouge
            green_data = data_pts[data_pts['color'] == 'green']
            red_data = data_pts[data_pts['color'] == 'red']

            # Fusionner les données des deux balles sur le temps
            merged_data = pd.merge(green_data, red_data, on='time', suffixes=('_green', '_red'), how='inner')

            # Calcul des coordonnées compensées
            merged_data['cx_red_compensated'] = merged_data['cx_green'] - merged_data['cx_red']
            merged_data['cy_red_compensated'] = merged_data['cy_green'] - merged_data['cy_red']

            # Préparation des données pour le fichier texte (format array Python)
            header = "temps | cx_green | cy_green | cx_red | cy_red | cx_red_compensated | cy_red_compensated"
            lines = []
            for _, row in merged_data.iterrows():
                line = f"[{row['time']}, {row['cx_green']}, {row['cy_green']}, {row['cx_red']}, {row['cy_red']}, {row['cx_red_compensated']}, {row['cy_red_compensated']}]"
                lines.append(line)

            # Contenu du fichier .txt
            contenu = f"""#date
#{datetime.now().strftime('%Y-%m-%d')}

#auteurs
#{auteurs}

#omegaomegan
#{omega}

#amplitude
#{amplitude}

#numerotest
#{numerotest}

#coordonnées
{header}
[{',\n '.join(lines)}]
"""
            with open(chemin_data, 'w') as f:
                f.write(contenu)

            print(f"Créé : {chemin_data}")

            # Graphique de la position de la balle verte en fonction du temps
            if not merged_data.empty:
                plt.figure()
                plt.plot(merged_data['time'], merged_data['cx_green'], 'g-', label='Position balle verte (cx)')
                plt.xlabel('Temps (s)')
                plt.ylabel('Position cx (pixels)')
                plt.title(f'Position de la balle verte (ω={omega}, A={amplitude})')
                plt.legend()
                plt.grid()
                plt.savefig(os.path.join(dossier_destination, f"{omega}_{amplitude}_graph_{numerotest}_{durée}_{puit}.png"))
                plt.close()
        except Exception as e:
            print(f"Erreur lors du traitement de {fichier}: {e}")

# Chemins des dossiers (à adapter selon ton environnement)
dossier_source = r"C:\path\Video\Matrice_2_video"
dossier_destination = r"C:\path\Video\Matrice_2_texte"

# Appel de la fonction
creer_fichiers_data(dossier_source, dossier_destination)
