Ruta del Metro de Barcelona

Aquest projecte implementa algorismes de cerca per calcular rutes en un sistema de metro. Utilitza estructures de dades per representar el mapa del metro i permet la cerca d'itineraris de forma eficient.

Descripció

L'objectiu principal del projecte és trobar la millor ruta entre estacions dins d'una xarxa de metro simulada. Implementa diferents estratègies de cerca, com ara:

Cerca en profunditat (DFS)

Cerca en amplada (BFS)

A (A estrella)*

El projecte utilitza dades de dues ciutats simulades ("Lyon_bigCity" i "Lyon_smallCity") per validar el correcte funcionament dels algorismes.

Requisits previs

Dependències necessàries

És necessari tenir Python 3.9 (o superior) instal·lat.

Biblioteques utilitzades (ja incloses en Python per defecte):

os

math

Instruccions d'ús

1. Estructura del projecte

Assegura't que el projecte segueix aquesta estructura de directoris:

Ruta-metro-Barcelona-main/
├── CityInformation/
│    ├── Lyon_bigCity/
│    └── Lyon_smallCity/
├── SearchAlgorithm.py
├── SubwayMap.py
├── TestCases.py
├── utils.py
└── .idea/

2. Executar el projecte

Navega al directori arrel del projecte:

cd Ruta-metro-Barcelona-main

Executa el fitxer TestCases.py per provar els diferents algorismes:

python TestCases.py

3. Funcionalitats principals

Trobar la millor ruta entre estacions: Els algorismes implementats permeten calcular l'itinerari més eficient segons la metètrica definida.

Suport per a diferents ciutats: Pots utilitzar diferents jocs de dades dins del directori CityInformation/.

4. Exemple d'ús de l'algorisme

Per executar una cerca personalitzada, utilitza el fitxer SearchAlgorithm.py i crida a les funcions corresponents. Per exemple:

from SearchAlgorithm import *
from SubwayMap import *

# Carregar el mapa del metro
metro_map = SubwayMap("CityInformation/Lyon_bigCity")

# Executar cerca A*
result = A_star(metro_map, 'S1', 'S10')
print(result)

Contacte

Per a dubtes o suggeriments:

Nom: [David Araujo]

Email: [Davidaraujogarcia12@gmail.com]
