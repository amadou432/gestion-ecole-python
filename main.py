etudiant=[]

def menu():
    print("1-Ajouter un étudiant")
    print("2-Supprimer un étudiant")
    print("3-afficher la liste complète des étudiants")
    print("4-chercher un étudiant par son nom")
    print("5-Quitter le programme")
    Choix=int(input("Choix = "))
    return Choix

def ajouter_etudiant(etudiant):
    nom=input("Donner le nom de l'etudiant: ")
    etudiant.append(nom)
    print("L'etudiant a été ajouté avec succès.")
    exit

def supprimer_etudiant(etudiant):
    print(etudiant)
    supp=input("Donner le nom de l'etudiant qui doit sauter: ")
    if supp in etudiant:
        etudiant.remove(supp)
        print("l'etudiant a ete supprimmer avec succes.")
    else:
        print("Le nom de l'etudiant que vous avez donner n'est pas dans la liste.")

def afficher_etudiant(etudiant):
    print("Voici les noms des etudiants inscrit: \n")
    for et in etudiant:
        print(et)

def rechercher_etudiant(etudiant):
    rech=input("Donner le nom de l'etudiant a rechercher: ")
    
    if rech in etudiant :
        print("Le nom de l'etudiant que vous rechercher est dans la liste.")
    else:
        print("Le nom de l'etudiant que vous rechercher n'est pas dans la liste.")



Choix=0

while Choix != 5:
    Choix=menu()
    match Choix:
        case 1:
            ajouter_etudiant(etudiant)
            
        case 2:
            afficher_etudiant(etudiant)
            supprimer_etudiant(etudiant)
           

        case 3:
            afficher_etudiant(etudiant)
            

        case 4:
            rechercher_etudiant(etudiant)
            

        case 5:
            break
    
                


