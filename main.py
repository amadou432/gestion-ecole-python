base_etudiants = [
        {"id": "001", "nom": "Emma Petit", "note": "10", "classe": "Terminale C"},
        {"id": "002", "nom": "Thomas Lefebvre", "note": "10", "classe": "BTS SIO 1"},
        {"id": "003", "nom": "Chloé Moreau", "note": "10", "classe": "Licence Info"},
        {"id": "004", "nom": "Adam Garcia", "note": "10", "classe": "Classe Prépa"},
        {"id": "005", "nom": "Papa Mambaye" , "note": "10", "classe": "Terminale D"}
    
]

base_classes = [
    {"id": "001", "nom": "Terminale C", "niveau": "Lycée", "etudiants": ["Emma Petit"]},
    {"id": "002", "nom": "BTS SIO 1", "niveau": "Supérieur", "etudiants": ["Thomas Lefebvre"]},
    {"id": "003", "nom": "Licence Info", "niveau": "Supérieur", "etudiants": ["Chloé Moreau"]},
    {"id": "004", "nom": "Terminale D", "niveau": "Primaire", "etudiants": ["Papa Mambaye"]},
    {"id": "005", "nom": "Classe Prépa", "niveau": "Supérieur", "etudiants": ["Adam Garcia"]}
]

def menu_principale():
    print("------------------------------------------")
    print("|        1-Menu classe                   |")
    print("|        2-Menu Etudiant                 |")
    print("|        3-Quitter le programme          |")
    print("------------------------------------------")

    Choix=int(input("Choix = "))
    return Choix

def menu_classe():
    print("----------------------------------------------------")
    print("|        1-Créer une classe                        |")
    print("|        2-Supprimer une classes                   |")
    print("|        3-Afficher la liste complète des classes  |")
    print("|        4-Afficher les détails d'une classe       |")
    print("|        5-Ajouter un étudiant dans une classe     |")
    print("|        6-Quitter le programme                    |")
    print("----------------------------------------------------")

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
    c=input("Donner l'id de la classe dont vous voulez voir les détails: ")
    exist=False
    for i in base_classes:
        if i["id"] == c:
            n = len(i["etudiants"])
            print("| ID: ",i["id"]," | Nom: ",i["nom"]," | niveau: ",i["niveau"]," | Etudiants: ",i["etudiants"]," | Nombre d'étudiants: ",n)
            exist=True
    if not exist :
        print("L'ID de la classe que vous avez donner n'est pas dans la liste.")

def ajouter_etudiant_classe():  
    afficher_etudiant()
    id = input("Donner l'id de l'etudiant a ajouter dans une classe: ")
    trouve_etudiant=False
    trouve_classe=False
    for i in base_etudiants:
        if i["id"] == id:
            trouve_etudiant=True
            id_et=i
            break
    if  trouve_etudiant==False:
        print("L'Id de l'etudiant que vous avez donner n'est pas sur la liste!")
           
    afficher_classe(base_classes)
    classe = input("Donner l'id de la classe a ajouter: ")      
    for j in base_classes:
        if  j["id"] == classe:
            trouve_classe=True
            if i["nom"] in j["etudiants"]:
                print("l'etudiant que vous avez choisis est deja dans la classe que vous avez choisis!")
            else:
                j["etudiants"].append(id_et["nom"]) 
                id_et["classe"] = j["nom"]
                print("L'etudiant a été ajouté à la classe avec succès.")
    if  trouve_classe==False:
        print("L'Id de la classe que vous avez donner n'est pas sur la liste!")
            
def menu_etudiant():
    print("----------------------------------------------------------")
    print("|        1-Ajouter un étudiant                           |")
    print("|        2-Supprimer un étudiant                         |")
    print("|        3-Afficher la liste des étudiants d’une classe  |")
    print("|        4-Afficher la liste complète des étudiants      |")
    print("|        5-chercher un étudiant par son nom              |")
    print("|        6-Afficher les informations d’un étudiant       |")
    print("|        7-Gerer les notes d'un étudiant                 |")
    print("|        8-Modifier les informations d'un étudiant       |")
    print("|        9-Quitter le programme                          |")
    print("----------------------------------------------------------")

    Choix=int(input("Choix = "))
    
    return Choix

def ajouter_etudiant():
    id=input("Donner l'id de l'etudiant: ")
    nom=input("Donner le nom complet de l'etudiant: ")
    note = None
    classe = None
    trouve=False
    for et in base_etudiants:
        if et["id"] == id:
            trouve=True
    if trouve==False:
        base_etudiants.append({
            "id": id,
            "nom": nom,
            "note": note,
            "classe": classe
        })
        print("L'etudiant a été ajouté avec succès.")
    else:
        print("Cet etudiant existe déjà.") 
    
    

def supprimer_etudiant():
    afficher_etudiant()
    supp = input("Donner l'ID de l'étudiant à supprimer : ")
    trouver=False
    for et in base_etudiants:
        if et["id"] == supp:
            trouver=True
            base_etudiants.remove(et)
            print("L'etudiant a été supprimé avec succès.")
    if trouver==False:
        print("L'id de l'etudiant que vous avez donné n'est pas valide!")

def afficher_etudiant():
    print("Voici les noms des etudiants inscrit: \n")
    for et in base_etudiants:
        print("| ID: ",et["id"]," | Nom: ",et["nom"]," |  Note: ",et["note"]," |  classe: ",et["classe"]," |")

def afficher_etudiant_classe():
    afficher_classe(base_classes)
    id=input("Donner l'id de la classe où vous voulez voir les étudiants qui la constitue: ")
    trouver=False
    for cl in base_classes:
        if id == cl["id"]:
            trouver=True
            print("Voici les noms des etudiants inscrit dans cette classe: \n")
            print(cl["etudiants"])
    if not trouver:
        print("L'id que vous aver donner est incorrect!")
    
        

def afficher_info_etudiant():
    print("Voici la liste des étudiants: ")
    for et in base_etudiants:
        print("| ID: ",et["id"]," | Nom: ",et["nom"]," | ")
    id=input("Donner l'id de l'etudiant dont vous voulez voir les informations: ")
    trouver=False
    for et in base_etudiants:
        if id == et["id"]:
            trouver=True
            print("Voici les informations de l'etudiant choisi: \n")
            print("| ID: ",et["id"]," | Nom: ",et["nom"]," | Note: ",et["note"]," | classe: ",et["classe"]) 
    if not trouver:
        print("L'id que vous aver donner est incorrect!")
    
             

def rechercher_etudiant(etudiant):
    id = input("Donner l'ID de l'étudiant a rechercher : ")
    for et in base_etudiants:
        if et["id"] == id:
            print(et)
            return
    print("Étudiant introuvable.")

def gerer_notes_etudiant():
    afficher_etudiant()
    id = input("Donner l'ID de l'étudiant dont vous vouler gerer la note: ")
    trouve=False



    for et in base_etudiants:
        if et["id"] == id:
            trouve=True
            id_note=id
            print("Étudiant :", et["nom"])
            print("Note actuelle :", et["note"])
            print("Voulez vous modifier la note de l'étudiant?")
            print("1-Oui")
            print("2-Non")
            choix=int(input("Choix: "))
            if choix == 1:
                
                try:
                    note = float(input("Entrer une nouvelle note : "))
                    if note < 0 or note > 20:
                        print("La note doit être entre 0 et 20.")
                        return
                    str(note)
                    et["note"] = note
                    print("Note ajoutée avec succès.")
                    return
                except ValueError:
                    print("Veuillez entrer un nombre valide.")
                    return
            if choix == 2:
                break
    if not trouve:
        print("etudiant introuvable!")

def modifier_etudiant():
    afficher_etudiant()
    id = input("Donner l'ID de l'étudiant à modifier : ")

    for et in base_etudiants:
        if et["id"] == id:
            print("l'etudiant a été trouvé :", et)

            print("\nQue voulez-vous modifier ?")
            print("1 - Nom")
            print("2 - Note")
            print("3 - Classe")
            print("4 - Tout modifier")

            choix = input("Votre choix : ")

            if choix == "1":
                nouveau_nom = input("Nouveau nom : ")
                et["nom"] = nouveau_nom

            elif choix == "2":
                nouvelle_note = input("Nouvelle note : ")
                et["note"] = nouvelle_note

            elif choix == "3":
                nouvelle_classe = input("Nouvelle classe : ")
                et["classe"] = nouvelle_classe

            elif choix == "4":
                et["nom"] = input("Nouveau nom de l'etudiant: ")
                et["note"] = input("Nouvelle note de l'etudiant: ")
                et["classe"] = input("Nouvelle classe de l'etudiant: ")

            else:
                print("Choix invalide.")
                return

            print("Les informations de l'étudiant ont été mises à jour avec succès.")
            print("Voici les nouvelles informations de l'étudiant :", et)
            return

    print("Aucun étudiant trouvé avec cet ID.")

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
                ajouter_etudiant_classe()
            elif choix == 6:
                print("Au revoir!")
                break    
            
                
        case 2:
            choix=menu_etudiant()
            if choix ==1:
                ajouter_etudiant()
            elif choix == 2:
                supprimer_etudiant()
            elif choix == 3:
                afficher_etudiant_classe()
            elif choix == 4:
                afficher_etudiant()
            elif choix == 5:
                rechercher_etudiant(base_etudiants)
            elif choix == 6:
                afficher_info_etudiant()
            elif choix == 7:
                modifier_etudiant()
            elif choix == 8:
                gerer_notes_etudiant()
            elif choix == 9:
                print("Au revoir !")
                break     
                
                
        case 3:
            print("Au revoir !")
            break     
                

    
                


