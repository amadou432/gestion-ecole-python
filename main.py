base_etudiants = [
    "Lucas Bernard", 
    "Emma Petit", 
    "Thomas Lefebvre", 
    "Chloé Moreau", 
    "Adam Garcia"
]
base_classes = [
    {"id": "001", "nom": "Terminale C", "niveau": "Lycée", "etudiants": []},
    {"id": "002", "nom": "BTS SIO 1", "niveau": "Supérieur", "etudiants": []},
    {"id": "003", "nom": "Licence Info", "niveau": "Supérieur", "etudiants": []},
    {"id": "004", "nom": "CM2 B", "niveau": "Primaire", "etudiants": []},
    {"id": "005", "nom": "Classe Prépa", "niveau": "Supérieur", "etudiants": []}
]

def menu_principale():
    print("1-Menu classe")
    print("2-Menu Etudiant")
    print("3-Quitter le programme")
    Choix=int(input("Choix = "))
    return Choix

def menu_classe():
    print("1-Créer une classe")
    print("2-Supprimer une classes")
    print("3-Afficher la liste complète des classes")
    print("4-Afficher les détails d'une classe")
    print("5-Quitter le programme")
    choix=int(input("Choix = "))
    return choix

def ajouter_classe(base_classes):
    id = input("Donner l'ID de la classe: ")
    nom = input("Donner le nom de la classe: ")
    niveau = input("Donner le niveau de la classe: ")
    nouvelle_classe = {
        "id": id,
        "nom": nom,
        "niveau": niveau,
        "etudiants": [] 
    }
    
    base_classes.append(nouvelle_classe)
    print(f"La classe '{nom}' a été ajoutée avec succès.")

def supprimer_classe(base_classes):
    afficher_classe(base_classes)
    supp=input("Donner l'ID de la classe a supprimer: ")
    exist=False
    for i in base_classes:
        if i["id"] == supp:
            base_classes.remove(i)
            print("La classe a été  supprimer avec succès.")
            exist=True
    if not exist :
        print("L'ID de la classe que vous avez donner n'est pas dans la liste.")

def afficher_classe(base_classes):
    print("Voici la liste des classes existante: \n")
    for i in base_classes:
        print("| ID: ",i["id"]," | Nom: ",i["nom"]," |")

def details_classe(base_classes):
    afficher_classe(base_classes)
    c=input("Doneer l'id de la classe dont vous voulez voir les détails: ")
    exist=False
    for i in base_classes:
        if i["id"] == c:
            print("| ID: ",i["id"]," | Nom: ",i["nom"]," | niveau: ",i["niveau"]," |")
            exist=True
    if not exist :
        print("L'ID de la classe que vous avez donner n'est pas dans la liste.")

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

while True:
    choix=menu_principale()    
    match choix:
        case 1:
            choix=menu_classe()
            if choix == 1:
                ajouter_classe(base_classes)
            elif choix == 2:
                supprimer_classe(base_classes)
            elif choix == 3:
                afficher_classe(base_classes)
            elif choix == 4:
                details_classe(base_classes)
            elif choix == 5:
                print("AU revoir!")
                break
                
        case 2:
            choix=menu_etudiant()
            if choix ==1:
                ajouter_etudiant(base_etudiants)
            elif choix == 2:
                supprimer_etudiant(base_etudiants)
            elif choix == 3:
                afficher_etudiant(base_etudiants)
            elif choix == 4:
                rechercher_etudiant(base_etudiants)
            elif choix == 5:
                print("AU revoir!")
                break
        case 3:
            print("Au revoir !")
            break 
                

    
                


