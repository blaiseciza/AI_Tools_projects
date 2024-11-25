import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

#creation des variables linguistiques
temperature=ctrl.Antecedent(np.arange(0,41,1), 'temperature')
chaleur=ctrl.Consequent(np.arange(0,101,1), 'chaleur')
#creation des fonctions d'appartenance
#1. Pour temperature
temperature['froid'] = fuzz.trimf(temperature.universe, [0, 0, 15])
temperature['frais'] = fuzz.trimf(temperature.universe, [10, 20, 30])
temperature['chaud'] = fuzz.trimf(temperature.universe, [25, 40, 40])
#2. Pour chaleur
chaleur['faible'] = fuzz.trimf(chaleur.universe, [0, 0, 50])
chaleur['moyenne'] = fuzz.trimf(chaleur.universe, [40, 50, 60])
chaleur['forte'] = fuzz.trimf(chaleur.universe, [50, 100, 100])

#visualisation des fonctions d'appartenance
fig,(ax0,ax1)=plt.subplots(nrows=2,figsize=(8,6))
temperature.view(ax=ax0)
ax0.set_title('Temperature')
chaleur.view(ax=ax1)
ax1.set_title('Chaleur')

plt.tight_layout()
plt.show()
# Création des règles
rule1 = ctrl.Rule(temperature['froid'], chaleur['forte'])
rule2 = ctrl.Rule(temperature['frais'], chaleur['moyenne'])
rule3 = ctrl.Rule(temperature['chaud'], chaleur['faible'])

# Création du système de contrôle
control_system = ctrl.ControlSystem([rule1, rule2, rule3])

# Simulation du système
sim = ctrl.ControlSystemSimulation(control_system)

# Définition de la température d'entrée
sim.input['temperature'] = 10

# Calcul de la sortie
sim.compute()

# Affichage du résultat
print(sim.output['chaleur'])

# Visualisation de la sortie
fig, ax = plt.subplots(figsize=(8, 6))

chaleur.view(sim=sim, ax=ax)
ax.set_title('Sortie du système')
plt.tight_layout()
plt.show()
