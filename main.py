base_etudiants=[]
base_classes=[]

def menu_principale():
    print("1-Menu classe")
    print("1-Menu Etudiant")
    print("5-Quitter le programme")
    Choix=int(input("Choix = "))
    return Choix

def menu_classe():
    print("1-Créer une classe")
    print("2-Supprimer une classes")
    print("3-Afficher la liste complète des classes")
    print("4-Afficher les détails d'une classe")
    print("5-Quitter le programme")
    Choix=int(input("Choix = "))
    return Choix

def ajouter_classe(base_classes):
    id=input("Donner l'ID de la classe: ")
    nom=input("Donner le nom de la classe: ")
    niveau=input("Donner l'ID de la classe: ")
    base_classes.append(id)
    base_classes.append(nom)
    base_classes.append(niveau)
    print("La classe a été ajouté avec succès.")



def supprimer_classe(base_classes):
    print(base_classes)
    supp=input("Donner l'ID de la classe a supprimer: ")
    if supp in base_classes:
        base_classes.remove(supp)
        print("La classe a été  supprimer avec succès.")
    else:
        print("L'ID de la classe que vous avez donner n'est pas dans la liste.")

def afficher_classe(base_classes):
    print("Voici la liste des classes existante: \n")
    for i in base_classes:
        print(i)

def menu_etudiant():
    print("1-Ajouter un étudiant")
    print("2-Supprimer un étudiant")
    print("3-Afficher la liste complète des étudiants")
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


                


