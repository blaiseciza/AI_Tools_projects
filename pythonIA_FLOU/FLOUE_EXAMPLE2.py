import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

#creation des variables linguistiques
vitesse=ctrl.Antecedent(np.arange(0,110,1), 'vitesse')
acceleration=ctrl.Consequent(np.arange(0,101,1), 'acceleration')

#Définition des fonctions d'appartenance
#1. Pour vitesse
vitesse['lente']=fuzz.trimf(vitesse.universe, [0,0,30])
vitesse['moyenne']=fuzz.trimf(vitesse.universe, [20,50,80])
vitesse['rapide']=fuzz.trimf(vitesse.universe, [70,100,100])

#2. Pour l'acceleration
acceleration['faible']=fuzz.trimf(acceleration.universe, [0,0,50])
acceleration['moyenne']=fuzz.trimf(acceleration.universe, [40,50,60])
acceleration['forte']=fuzz.trimf(acceleration.universe, [50,100,100])

#Visualisation des fonctions d'appartenance
fig,(ax0,ax1)=plt.subplots(nrows=2,figsize=(8,6))
vitesse.view(ax=ax0)
ax0.set_title('vitesse')
acceleration.view(ax=ax1)
ax1.set_title('acceleration')
plt.tight_layout()
plt.show()

#creation des regles
rule1=ctrl.Rule(vitesse['lente'],acceleration['forte'])
rule2=ctrl.Rule(vitesse['moyenne'],acceleration['moyenne'])
rule3=ctrl.Rule(vitesse['rapide'],acceleration['faible'])

#Creation du systeme de controle
ctrl_sys=ctrl.ControlSystem([rule1,rule2,rule3])

#Creation de la simulation
sim=ctrl.ControlSystemSimulation(ctrl_sys)

#Test
#Definition de la vitesse d'entree
sim.input['vitesse']=80

#Calcul de la sortie
sim.compute()
# Affichage du résultat
print(sim.output['acceleration'])

#On visualise sur un graphique
acceleration.view(sim=sim)
plt.title("Acceleration en fonction de la vitesse")
plt.show()
