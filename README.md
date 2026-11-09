# Experimental-Duffing-equation-data
Collection of data from experiments on Duffing equations with the objective of mapping areas of chaotic behaviour. 

# French version

# Auteurs & contexte
Auteurs : Flavio Samson & Andy Wong // L2 Mécanique intensif 2025-2026
Stage de mécanique au laboratoire Jean Le Rond d'Alembert de Sorbonne Université 
Date : sep-déc 2025


camera : Sony ZV-1 
mode de la camera : "intelligent auto"
ips : 60
balle : verte
diamètre : 24.5 ±1 mm
masse : non mesurée



Paramètres adimensionnés : 
	G = 0.59
	Omega_n : 10.4819 rad/s



Codes utilisés (en s'appuyant sur ceux du précédent rapport) : 
- matrice_de_test : génère une matrice de test au format python et trace le graphe avec chaque point sous une courbe définie par une fonction affine (le code génère n points puis supprime ceux qui se trouvent au dessus de la courbe) (voir l'exemple dans le code)

- graphe_matrice_test : génère le même graphe mais en prenant en entrée une matrice contenant les coordonnées des points et le régime du mouvement de la balle associé (voir l'exemple dans le code)

- transforme_matrice_rapport : convertit les données de la matrice de test des données du rapport (omega/omegan et amplitude) aux données entrées dans le code Arduino (Période et nombre de rotation)

- Renommer_video : renomme les vidéos rangées dans le bon ordre par 3 (code très spécifique à notre cas)

- Nomenclature_final_3 : effectue le code de détection sur chacune des vidéos et en extrait le fichier texte associé avec les données que l'on souhaîte. 




format des données : 

Titres des fichiers : 
omegaomegan_amplitude_Type_numerodetest_duree_positiondedepart

Avec : 
omagaomegan : un réel, donnant le quotient entre omega choisi pour l'expérience et l'omega_n (≈10.4819rad/s)

amplitude : amplitude du mouvement de forçage en m

Type : type du fichier DATA pour la base de données et VID pour les vidéos brutes.

numerodetest : numéro du test effectué pour les mêmes conditions de départ

duree : durée de l'expérience en oscillations

positiondedepart : puit de gauche (noté G) puit de droite (noté D) ou centre (noté C)




Organisation des fichiers : 

écrit sous le format array python ( ex : [[a,b,c],[d,e,f]]) avec les colonnes suivantes : 

temps| cx_green | cy_green | cx_red | cy_red | cx_red_compensated | cy_red_compensated

Avec : 

temps : instant de la vidéo ou a été capturée l'image dont sont extraites les données

cx_green : la position de la balle selon l'axe x

cy_green : la position de la balle selon l'axe y

cx_red : la position du point de repère rouge associé à la plateforme selon l'axe x

cy_red : la position du point de repère rouge associé à la plateforme selon l'axe y





Perspectives d'amélioration de l'expérience : 
- Tester différents puits de départ
- Faire tourner l'expérience plus longtemps
- Utiliser une balle plus adhérente 
- Rigidifier la plateforme (parfois bancale)
- Réaliser toutes les expérience d'une traite (pas de légers décalages entre différentes sessions de prise vidéo)
