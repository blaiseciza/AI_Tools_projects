import re

b_regle=[(r"fièvre et maux de tête","grippe"),
         (r"toux et éternuements","rhume"),
         (r"mal de gorge et fièvre","angine")]
def diagnostic(symptoms):
    for sympt,maladie in b_regle:
        if re.search(sympt, symptoms, re.IGNORECASE):
            return maladie
    return "Diagnostique inconnu"
#Utilisateur saisi ses symptomes
symptomes_user=input("Entrez vos symptomes (séparés par des virgules):")
diagno=diagnostic(symptomes_user)
print(diagno)