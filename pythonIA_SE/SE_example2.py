import csv
#base de faits (initialement vide)
b_faits={}
#base des règles(avec des probabilites)
b_regles=[(("fièvre","maux de tête"),"grippe",0.8),
          (("toux","éternuements"),"rhume",0.7),
          (("mal de gorge","fièvre"),"angine",0.6),
          (("fatigue","vaumissement"),"grossesse",0.5)]
def add_symptom(symptom):
    b_faits[symptom]=True
#on cree la fonction pour le diagnostic
def diagnostic():
    scores={}
    for symptoms,maladie,probabilite in b_regles:
        if all(symptom in b_faits for symptom in symptoms):
            scores[maladie]=scores.get(maladie,0)+probabilite
    if scores:
        return max(scores,key=scores.get)
    else:
        return "Aucun diagnostic concluant"
    
#Saisie de l'utilisateur
symptoms=input("Entrez vos symptomes (séparés par des virgules):").split(",")
for symptom in symptoms:
    add_symptom(symptom)
    
#Effectuer le diagnostic
diagno=diagnostic()
print("les fait:",b_faits)
print("Diagnostic probable: ",diagno)

#On cree une fonction pour enregistrer le diagnostic
def save_diagnostic(symptoms,diagnostic):
    with open('diagnostics.csv','a',newline='') as csvfile:
        fieldnames=['symptoms','Diagnostic']
        writer=csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({'symptoms':', '.join(symptoms),'Diagnostic':diagnostic})
        
#on appel la fonction
save_diagnostic(list(b_faits.keys()),diagno)