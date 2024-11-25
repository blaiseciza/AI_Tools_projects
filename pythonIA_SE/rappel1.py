#Declaration des variables
x=10
y=30
print("La valeur ",x+y)

nom,age="JEAN",16
print(nom,"a",age,"ans")

#Les conditions
if(age>=18):
    print(nom,"est majeur")
else:
    print(nom,"est mineur")
#Fonction
#definition de la fonction
def somme(a,b):
    print(a,"+",b,"=",a+b)
#Appel de la fonction
somme(44,5)
#Tableau et boucle
jr_semaine=["lundi","mardi","mercredi","jeudi","vendredi","samedi","dimanche"]
for jr in jr_semaine:
    print(jr)
    