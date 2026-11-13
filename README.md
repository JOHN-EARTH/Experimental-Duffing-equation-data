# Experimental-Duffing-equation-data

**ENG :** Collection of data from experiments on Duffing equations[^1], with the objective of "mapping" the different response regimes (periodic or chaotic).

**FR :** Ensemble de mesures récoltées lors d'expériences sur les équations de Duffing[^1], dans l'objectif de « cartographier » les différents régimes de réponse (périodiques ou chaotiques).

---

# Auteurs &amp; contexte / Authors &amp; context

**FR :**

Auteurs : Flavio Samson &amp; Andy Wong // L2 Mécanique intensif 2025-2026  
Stage de mécanique au laboratoire Jean Le Rond d'Alembert de Sorbonne Université  
Date : septembre–décembre 2025

**ENG :**

Authors: Flavio Samson &amp; Andy Wong // L2 Intensive Mechanics 2025-2026  
Mechanics internship at the Jean Le Rond d'Alembert laboratory, Sorbonne Université  
Date: September–December 2025

## Méthodologie / Methodology

**FR :**

Notre objectif était d'étudier, pour quels paramètres de départ, une expérience modélisant les équations de Duffing[^1] suivait un régime d'évolution chaotique ou, au contraire, périodique. Nous avons tout d'abord réalisé un maillage « large » (matrix\_experiment\_campaign\_wide\_net.png) afin de définir dans quelles « zones » de l'espace des paramètres se trouvaient les comportements chaotiques, puis nous avons « affiné » l'étude (matrix\_experiment\_campaign\_narrow\_net.png). Le dispositif expérimental a été construit par d'autres stagiaires, ainsi que quelques études de « preuve de concept ».

**ENG :**

Our goal was to determine for which initial parameters an experiment modelling the Duffing equations[^1] followed a chaotic evolution regime, or, on the contrary, a periodic one. We first carried out a "wide" mesh (matrix\_experiment\_campaign\_wide\_net.png) to identify in which "zones" of the parametric space chaotic behaviour was located, then we "refined" the study (matrix\_experiment\_campaign\_narrow\_net.png). The experimental apparatus was built by other interns, along with a few "proof of concept" studies.

## Paramètres de l'étude / Study parameters

**FR :**

- caméra : Sony ZV-1
- mode de la caméra : « intelligent auto »
- images par seconde : 60
- couleur de la balle : verte
- diamètre de la balle : 24,5 ± 1 mm
- masse de la balle : non mesurée

**ENG :**

- Camera: Sony ZV-1
- Camera mode: "intelligent auto"
- Frames per second: 60
- Ball colour: green
- Ball diameter: 24.5 ± 1 mm
- Ball mass: not measured

## Paramètres adimensionnés du dispositif expérimental / Dimensionless parameters of the experimental setup

\(G = 0.59\)  
\(\Omega_n = 10.4819 \,\mathrm{rad}\cdot\mathrm{s}^{-1}\)

## Dossier « Code » / "Code" folder

**FR :**

- matrix\_experiment\_campaign.py : génère une matrice de tests au format Python et trace le graphe avec chaque point sous une courbe définie par une fonction affine -fonction définie par les limites de performance de notre moteur- Le code génère n points puis supprime ceux qui se trouvent au-dessus de la courbe.— voir l'exemple dans le code.
- plot\_matrix\_experiment\_campaign.py : génère le graphe de la même matrice, mais en prenant en entrée une matrice contenant les coordonnées des points et le régime du mouvement de la balle associé — voir l'exemple dans le code.
- matrix\_data\_convert.py : convertit les données de la matrice de tests du rapport ($\\frac{\\omega}{\\omega\_n}$ et amplitude) en données entrées dans le code Arduino (période et nombre de rotations).
- Rename\_video.py : renomme les vidéos rangées dans le bon ordre par groupes de 3 (code très spécifique à notre cas).
- Convert\_data\_to\_txt.py : passe toutes les vidéos dans le code de détection et en extrait le fichier texte associé avec les données que l'on souhaite.
- experimental\_duffing\_study.py : code alternatif utilisé pour l'étude de l'espace des phases d'une expérience, avant l'écriture de « phase\_numerical\_study\_Duffing.py ». Trace la transformée de Fourier, l'espace des phases (x et y), la réponse temporelle (x et y) et la position (x ; y).
- phase\_numerical\_study\_Duffing.py : code utilisé pour produire des représentations graphiques de la réponse temporelle (en x), de l'espace des phases (en x) et de la section de Poincaré du système.

**ENG :**

- matrix\_experiment\_campaign.py: generates a test matrix in Python format and plots the graph with each point below a curve defined by an affine function. - the function corresponds to the limits of the motor- The code generates n points then discards those above the curve. — see the example in the code.
- plot\_matrix\_experiment\_campaign.py: generates the same graph, but takes as input a matrix containing the point coordinates and the associated ball motion regime — see the example in the code.
- matrix\_data\_convert.py: converts the test-matrix data from the report ($\\frac{\\omega}{\\omega\_n}$ and amplitude) into the data entered in the Arduino code (period and number of rotations).
- Rename\_video.py: renames the videos sorted in the correct order in groups of 3 (very case-specific code).
- Convert\_data\_to\_txt.py: runs all the videos through the detection code and extracts the associated text file with the desired data.
- experimental\_duffing\_study.py: alternative code used to study the phase space of an experiment before "phase\_numerical\_study\_Duffing.py" was written. Plots the Fourier transform, the phase space (x and y), the time response (x and y), and the (x, y) position.
- phase\_numerical\_study\_Duffing.py: code used to produce graphical representations of the time response (in x), the phase space (in x), and the Poincaré section of the system.

## Dossier « Vidéos » / "Vidéos" folder

**FR :**

« Vidéos » contient trois dossiers : « Graphs », « Matrice\_2\_texte » et « Matrice\_2\_video ».

**ENG :**

"Vidéos" contains three folders: "Graphs", "Matrice\_2\_texte" and "Matrice\_2\_video".

## Dossier « Graphs » / "Graphs" folder

**FR :**

Ce dossier contient les graphes de réponse temporelle (axe x) pour chaque essai de la campagne de mesure « fine ». Il contient également des représentations des deux maillages (« large » et « fin ») dans l'espace des paramètres de l'expérience.

**ENG :**

This folder contains the time-response (x axis) plots for each run of the "fine" measurement campaign. It also contains representations of both meshes ("wide" and "fine") in the experiment's parameter space.

## Dossier « Matrice\_2\_texte » / "Matrice\_2\_texte" folder

**FR :**

Contient les données de chaque expérience au format .txt, selon l'organisation ci-dessous.

Organisation des fichiers :

écrites au format array Python (ex. : \[\[a,b,c\],\[d,e,f\]\]) avec les colonnes suivantes :

temps | cx\_green | cy\_green | cx\_red | cy\_red | cx\_red\_compensated | cy\_red\_compensated

Avec :

- temps : instant de la vidéo où a été capturée l'image dont sont extraites les données
- cx\_green : position de la balle selon l'axe x
- cy\_green : position de la balle selon l'axe y
- cx\_red : position du point de repère rouge associé à la plateforme selon l'axe x
- cy\_red : position du point de repère rouge associé à la plateforme selon l'axe y

**ENG :**

Contains the data of each experiment in .txt format, organised as described below.

File organisation:

Written in Python array format (e.g. \[\[a,b,c\],\[d,e,f\]\]) with the following columns:

time | cx\_green | cy\_green | cx\_red | cy\_red | cx\_red\_compensated | cy\_red\_compensated

Where:

- time: instant in the video at which the frame the data is extracted from was captured
- cx\_green: position of the ball along the x axis
- cy\_green: position of the ball along the y axis
- cx\_red: position of the red reference marker attached to the platform along the x axis
- cy\_red: position of the red reference marker attached to the platform along the y axis

## Dossier « Matrice\_2\_video » / "Matrice\_2\_video" folder

**FR :**

Vidéos brutes de chaque expérience au format .mp4.

**Format des données :**

Nomenclature des fichiers pour les données textuelles et les vidéos :

omegaomegan\_amplitude\_Type\_numerodetest\_duree\_positiondedepart

- omegaomegan : un réel donnant le quotient entre le \(\Omega\) choisi pour l'expérience et \(\Omega_n\)
- amplitude : amplitude du mouvement de forçage, en m
- Type : type du fichier — DATA pour la base de données (.txt) et VID pour les vidéos brutes (.MP4)
- numerodetest : numéro du test effectué pour les mêmes conditions de départ (3 tests par condition de départ donnée)
- duree : durée de l'expérience, en oscillations
- positiondedepart : puits de gauche (noté G), puits de droite (noté D) ou centre (noté C)

**ENG :**

Raw videos of each experiment in .mp4 format.

**Data format:**

File naming convention for text data and videos:

omegaomegan\_amplitude\_Type\_numerodetest\_duree\_positiondedepart

- omegaomegan: a real number giving the ratio between the \(\Omega\) chosen for the experiment and \(\Omega_n\)
- amplitude: amplitude of the forcing motion, in m
- Type: file type — DATA for the database (.txt) and VID for the raw videos (.MP4)
- numerodetest: test number for the same initial conditions (3 tests per given set of initial conditions)
- duree: duration of the experiment, in oscillations
- positiondedepart: left well (G), right well (D), or centre (C)

## Perspectives d'amélioration / Possible improvements

**FR :**

- Étudier la périodicité dans le maillage « fin » de la base de données constituée.
- Tester différents puits de départ (nous n'avons testé que le puits de gauche).
- Faire tourner l'expérience plus longtemps (théoriquement, il faudrait un temps infini pour avoir la certitude que le signal est réellement chaotique).
- Utiliser une balle plus adhérente (nous avons rencontré des problèmes de glissement, qui ne permettent pas de faire l'hypothèse du roulement sans glissement).
- Rigidifier la plateforme (parfois bancale).
- Réaliser toutes les expériences d'une traite (pas de légers décalages entre les différentes sessions de prise de vidéo).

**ENG :**

- Study periodicity in the "fine" mesh of the assembled database.
- Test different starting wells (we only tested the left well).
- Run the experiment for longer (theoretically, an infinite amount of time would be needed to be certain the signal is truly chaotic).
- Use a ball with better grip (we encountered slipping problems, which make the rolling-without-slipping assumption invalid).
- Stiffen the platform (it was sometimes wobbly).
- Record all experiments in one go (avoiding slight offsets between the different video-recording sessions).

---

[^1]: J.A. Gottwald, L.N. Virgin, E.H. Dowell, *Experimental mimicry of Duffing's equation*, Journal of Sound and Vibration, Volume 158, Issue 3, 1992, Pages 447-467, ISSN 0022-460X.
