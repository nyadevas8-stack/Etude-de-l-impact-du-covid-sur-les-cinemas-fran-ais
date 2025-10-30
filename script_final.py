# # -*- coding: utf-8 -*-
# """
# Created on Mon Mar 24 07:28:45 2025

# @author: Nya Devas et Antoine Lépinay
# """
     
import csv
      
def charger_donnees(file,debut=0,fin=None):
    """
    Charge un fichier CSV et retourne une liste de dictionnaires.

    Parameters
    ----------
    file : str
        Nom du fichier CSV.

    Returns
    -------
    list of dict
        Liste de dictionnaires où les clés sont les en-têtes du CSV.
    """
    
    with open(file, "r",encoding="windows-1252") as fich:
     reader = csv.DictReader(fich, delimiter=";")
     data=list(reader)
    return data if not fin else data[debut:fin]

def charger_donnees_2018(file, debut=0, fin=None):
    """
    Charge un fichier CSV et retourne une liste de dictionnaires valides.

    Parameters
    ----------
    file : str
        Nom du fichier CSV.

    Returns
    -------
    list of dict
        Liste de dictionnaires où les clés sont les en-têtes du CSV.
    """
    with open(file, "r", encoding="UTF-8-SIG") as fich:
        reader = csv.DictReader(fich, delimiter=";")
        data=list(reader)
    
    return data if not fin else data[debut:fin]

       

# def charger_fileS(*files, debut=0, fin=None):
#     """
#     Charge plusieurs fichiers CSV et retourne une liste de données par fichier.

#     Chaque fichier peut avoir une structure différente.

#     Parameters
#     ----------
#     *files : chemins des fichiers CSV
#     debut : ligne de début (optionnel)
#     fin : ligne de fin (optionnel)

#     Returns
#     -------
#     list of list of dict
#     """
#     liste = []

#     for file in files:
#         with open(file, "r",encoding="windows-1252") as fich:
#             reader = csv.DictReader(fich, delimiter=";")  # on ne force pas les fieldnames
#             data = list(reader)
#             data = data[debut:fin] if fin else data[debut:]
#             liste.append(data)

#     return liste
    
    

    
# def charger_donnees_var(file, *args):
#     """
#     Charge un fichier CSV et sélectionne certaines colonnes spécifiées.

#     Parameters
#     ----------
#     file : str
#     *args : colonnes à garder

#     Returns
#     -------
#     list of dict
#     """
#     resultat = []
#     data = charger_donnees(file)

#     for ligne in data:
#         ligne_filtrée = {}
#         for var in args:
#             if var in ligne:
#                 ligne_filtrée[var] = ligne[var]
#         resultat.append(ligne_filtrée)

#     return resultat


# def charger_donnees_selection(file, **kwargs):
#     """
#     Charge un fichier CSV et filtre les lignes selon les critères donnés.

#     Parameters
#     ----------
#     file : str
#     kwargs : ex : ville="Paris"

#     Returns
#     -------
#     list of dict
#     """
#     data = charger_donnees(file)
#     resultat = []

#     for ligne in data:
#         correspond = True
#         for cle in kwargs:
#             if cle in ligne and ligne[cle] != str(kwargs[cle]):
#                 correspond = False
#                 break
#         if correspond:
#             resultat.append(ligne)

#     return resultat

def selection_donnees(data, **kwargs):
    """
    Charge un fichier CSV et filtre les lignes selon les critères donnés.

    Parameters
    ----------
    file : str
    kwargs : ex : ville="Paris"

    Returns
    -------
    list of dict
    """
    resultat=[]
    for ligne in data:
        correspond = True
        for cle in kwargs:
            if cle in ligne and ligne[cle] != str(kwargs[cle]):
                correspond = False
                break
        if correspond:
            resultat.append(ligne)

    return resultat

# #visualisation :
    


def afficher(data_dict,limite=10) :
    """
    Affiche les données sous forme de tableau avec les en-têtes. premiere ligne

    Parameters
    ----------
    data_dict : list of dict
        Liste de dictionnaires représentant les données à afficher.

    Returns
    -------
    None
    """
    head = list(data_dict[0].keys())  # Extraction des en-têtes
    print('\t'.join(head))  # Affichage des en-têtes

    for i, ligne in enumerate(data_dict): #permet de delimiter le nombre de dictionnaire dond de ligne(i) à afficher puisque chaque dictionnaore represente un i de la liste de dictionnaire
        if limite is not None and i >= limite :
            break
        print('\t'.join([str(ligne[key]) for key in head]))
        
        
# # Pré-traitements des données


# def renommer_variable(data,lastname,newname):
#     """
#     Permet de renommer une variable  variables dans un dictionnaire.

#     Parameters
#     ----------
#     data_dict : dict
#         Dictionnaire contenant les données.

#     Returns
#     -------
#     None
#     """
#     for ligne in data:
#      ligne[newname]=ligne[lastname]
#      del ligne[lastname]
    
# def renommer_variables(data,lastnames,newnames):#**kwargs,pop
#     """
#     Permet de renommer plusieurs   variables dans un dictionnaire.

#     Parameters
#     ----------
#     data_dict : dict
#         Dictionnaire contenant les données.

#     Returns
#     -------
#     None
#     """
#     for ligne in data:
#      for i in range(len(lastnames)):
#          ligne[newnames[i]] = ligne[lastnames[i]]
#          del ligne[lastnames[i]]

# def keep(data,*args):
#     """
    

#     Parameters
#     ----------
#     data : TYPE
#         DESCRIPTION.
#     *args : TYPE
#         DESCRIPTION.

#     Returns
#     -------
#     None.

#     """
#     resultat=[]
#     for ligne in data:
#         ligne_filtrée = {}
#         for var in args:
#             if var in ligne:
#                 ligne_filtrée[var] = ligne[var]
#         resultat.append(ligne_filtrée)
#     return resultat   
      

# def drop(data,*args):
#     """
    

#     Parameters
#     ----------
#     data : TYPE
#         DESCRIPTION.
#     *args : TYPE
#         DESCRIPTION.

#     Returns
#     -------
#     None.

#     """
#     resultat=[]
#     for ligne in data:
#         for var in args:
#             if var in ligne:
#                 del ligne[var]
#         resultat.append(ligne)
#     return resultat

# def modalités(data,var):# plustot decrire  une variable le nombre de valeur manqiueta le taux de valeur manquante te le nombre de modalités 
#     """   
#     retourne les modalités des variables entrée par l'utilisateur 

#     Parameters
#     ----------
#     data : TYPE
#         DESCRIPTION.

#     Returns
#     -------
#     None.

#     """
    
#     modalités=set()
#     for ligne in data :
#         modalités.add(ligne[var])
#     return list(modalités)


# #Gestion des anomalies :
    
# def nombre_NA(data,var) :
#     """
#     retourne le nombre de valeur manquante d'une variable entrée par l'utilisateur

#     Parameters
#     ----------
#     data : TYPE
#         DESCRIPTION.
#     var : TYPE
#         DESCRIPTION.

#     Returns
#     -------
#     None.

#     """
#     n=0
#     for ligne in data:
#         if ligne[var]=="":
#             n=n+1
    
#     return n 

# def taux_na(data,var):
#     """
#     retourne le taux de valeurs manquante d'une variable'

#     Parameters
#     ----------
#     data : TYPE
#         DESCRIPTION.
#     var : TYPE
#         DESCRIPTION.

#     Returns
#     -------
#     None.
     
#     """
#     taux=nombre_NA(data, var)/len(data)
#     return taux

# from datetime import datetime

# def description_variable(data, *args):
#     tableau = [["Variable", "Type", "Nombre de NA", "Taux de NA", "Nombre Modalités","Moyenne", "Correction proposée"]]

#     for var in args:
#         n_na = nombre_NA(data, var)
#         taux = round(taux_na(data, var), 4)
#         mod = modalités(data, var)

#         type_var = "Inconnu"
#         for ligne in data:
#             val = ligne.get(var, "")
#             if val not in ["", None, "NA"]:
#                 try:
#                     float(val)
#                     type_var = "Numérique"
#                 except:
#                     try:
#                         datetime.strptime(val, "%Y-%m-%d")  # Format YYYY-MM-DD
#                         type_var = "Date"
#                     except:
#                         type_var = "Texte"
#                 break

#         if type_var == "Inconnu":
#             type_var = "Texte"

#         if type_var == "Numérique":
#             total = 0
#             n = 0
#             for ligne in data:
#                 val = ligne.get(var, "")
#                 if val not in ["", None, "NA"]:
                    
#                         total = total + float(val)
#                         n= n + 1
                    
#             moyenne = round(total /n, 2)
#         else:
#             moyenne = "---"
#         if taux >= 0.8:
#             correction = "Suppression de la variable"
#         elif 0<taux<0.8:
#             if type_var=="Texte":
#               correction = "Imputation par le mode"
#             else:
#               correction = "Imputation par la moyenne"
#         else:
#             correction = "Aucune"
#         ligne = [var, type_var, n_na, taux, len(mod),moyenne, correction]
#         tableau.append(ligne)

#     return tableau

  

# def verification_identifiant(data, var):
#     """
#     Vérifie si un identifiant est unique, non nul et indexé.

#     Parameters
#     ----------
#     data : list of dict
#         Données sous forme de liste de dictionnaires.
#     var : str
#         Le nom de la variable à vérifier.

#     Returns
#     -------
#     tuple
#         (lignes en erreur, valeurs en erreur)
#     """
#     identifiants = set()  
#     erreurs = []
#     lignes_erreur = []
    
#     for i, ligne in enumerate(data):
#         valeur = ligne.get(var, "")
        
#         if valeur == "" or valeur in identifiants:
#             lignes_erreur.append(i)
#             erreurs.append(valeur)
#         else:
#             identifiants.add(valeur)  
    
#     return lignes_erreur, erreurs


# # rechercher les valeurs aberante selon un intervalle pour la variable semaine d'activitée
# def valeur_aberrante_limite (data,var,debut,fin):
#     """
    

#     Parameters
#     ----------
#     data : TYPE
#         DESCRIPTION.
#     var : TYPE
#         DESCRIPTION.

#     Returns
#     -------
#     None.

#     """
#     erreurs=[]
#     ligne_erreur=[]
#     for i,ligne in enumerate(data):
#         if not debut<=float(ligne[var])<=fin :
#             ligne_erreur.append(i)
#             erreurs.append(ligne[var])
#     return ligne_erreur,erreurs
# #verifier les calculs d'evoluation  renvoyer la ligne et la valeur si c'est mal calculee 

# def verfication_calcul (data,var_calculé,*parametres_calculs):
#     """
    

#     Parameters
#     ----------
#     data : TYPE
#         DESCRIPTION.
#     var_calculé : TYPE
#         DESCRIPTION.
#     *parametre_calculs : TYPE
#         DESCRIPTION.

#     Returns
#     -------
#     None.

#     """
#     if len(parametres_calculs) < 2:
#         raise ValueError("Au moins deux paramètres sont nécessaires pour effectuer le calcul.")

#     ligne_erreur = []
#     erreurs = []

#     for i, ligne in enumerate(data):
#         val1 = ligne[parametres_calculs[0]]
#         val2 = ligne[parametres_calculs[1]]
#         resultat_attendu = (float(val2)-float(val1))*100  

#         if float(ligne[var_calculé]) != resultat_attendu:
#             ligne_erreur.append(i)
#             erreurs.append((ligne[var_calculé], resultat_attendu))

#     return ligne_erreur, erreurs

# #utiliser les exception pour gerer  les types de variables (numeriue entier,date...)


# from datetime import datetime

# def verification_type(data, var, type_attendu):
#     """
#     Vérifie que toutes les valeurs de la variable `var` respectent le type attendu.

#     Parameters
#     ----------
#     data : list[dict]
#         Données à vérifier.
#     var : str
#         Nom de la variable à vérifier.
#     type_attendu : type | str
#         Type attendu (int, float, 'date', etc.).

#     Returns
#     -------
#     erreurs : list[tuple]
#         Liste des tuples (indice, valeur_fautive).
#     """
#     erreurs = []

#     for i, ligne in enumerate(data):
#         valeur = ligne.get(var)  # ici on s'assure que la variable existe, sinon valeur = None par défaut

#         try:
#             if type_attendu == int:
#                 int(valeur)
#             elif type_attendu == float:
#                 float(valeur)
#             elif type_attendu == 'date':
#                 datetime.strptime(valeur, "%Y/%m/%d")  
#             else:
#                 raise ValueError(f"Type non pris en charge : {type_attendu}")
#         except (ValueError, TypeError):
#             erreurs.append((i, valeur))

#     return erreurs


# #crrer et ameliorer les programme our qu'il gere l'anomalie (imputation ,supprimer, ne pas travailler sur la liste de bases )

# def corriger_anomalies(data, *args):
#     """
#     Applique les corrections proposées par description_variable :
#     - Suppression si taux de NA >= 0.8
#     - Imputation par moyenne (quantitatif) ou mode (qualitatif)
#     """
#     data_clean = [dict(dico) for dico in data]
#     description = description_variable(data_clean, *args)[1:]  # on ignore l'en-tête
    

#     for ligne in description:
#         var = ligne[0]
#         correction = ligne[-1]

#         if correction == "Suppression de la variable":
#             for dico in data_clean:
#                 if var in dico:
#                     del dico[var]

#         elif correction == "Imputation":
#             valeurs_non_nulles = []
#             for dico in data_clean:
#                 if var in dico and dico[var]!="":
#                     valeurs_non_nulles.append(dico[var])

#             # Détection du type (quanti ou quali)
#             est_quanti = True
#             for val in valeurs_non_nulles:
#                 try:
#                    float(val)
#                 except:
#                    est_quanti = False

#                 #if type(val) != int and type(val) != float:
#                     #est_quanti = False

#             if est_quanti:
#                 somme = 0
#                 compteur = 0
#                 for val in valeurs_non_nulles:
#                     somme = somme + val
#                     compteur = compteur + 1

#                 if compteur > 0:
#                     moyenne = somme / compteur
#                 else:
#                     moyenne = 0

#                 for dico in data_clean:
#                     if var in dico and dico[var]=="":
#                         dico[var] = moyenne

#             else:
#                 frequence = {}
#                 for val in valeurs_non_nulles:
#                     if val in frequence:
#                         frequence[val] = frequence[val] + 1
#                     else:
#                         frequence[val] = 1
             
#                 max_freq = 0
#                 mode_val = None
#                 for cle in frequence:
#                     if frequence[cle] > max_freq:
#                         max_freq = frequence[cle]
#                         mode_val = cle

#                 for dico in data_clean:
#                     if var in dico and dico[var] is None:
#                         dico[var] = mode_val

#     return data_clean

def to_float(val):
    """
    Convertit une valeur en float après avoir retiré les espaces et remplacé les virgules par des points.
    Si la conversion échoue, retourne 0.

    Paramètres
    ----------
    val : str ou float ou int
        Valeur à convertir.

    Retourne
    --------
    float
        La valeur convertie ou 0 si erreur.
    """
    try:
        return float(str(val).replace(" ", "").replace(",", "."))
    except (ValueError, TypeError):
        return 0


    


# # statistique 
# #agreger les indicateurs statistique par exemple moyen par region ...

# #Tableau sur les differents cinema de tel sorte qu'on puisse avoir les cinema peut etre par region avec des indicateurs 

def taux_frequentation_par_fauteuil_select(data, annee, **kwargs):
    """
    

    Parameters
    ----------
    data : TYPE
        DESCRIPTION.
    annee : TYPE
        DESCRIPTION.
    **kwargs : TYPE
        DESCRIPTION.

    Returns
    -------
    resultats : TYPE
        DESCRIPTION.

    """
    data_select = selection_donnees(data, **kwargs)
    resultats = []
    colonne_entrees = f"entrées {annee}"

    for cinema in data_select:
        try:
            entrees = to_float(cinema.get(colonne_entrees, 0))
            fauteuils = to_float(cinema.get("fauteuils", 1))
            taux = entrees / fauteuils if fauteuils else 0
            resultats.append(round(taux, 2))
        except (ValueError, TypeError):
            continue
    return resultats


def entrees_par_seance_select(data, annee, **kwargs):
    """
    

    Parameters
    ----------
    data : TYPE
        DESCRIPTION.
    annee : TYPE
        DESCRIPTION.
    **kwargs : TYPE
        DESCRIPTION.

    Returns
    -------
    resultats : TYPE
        DESCRIPTION.

    """
    data_select = selection_donnees(data, **kwargs)
    resultats = []
    colonne_entrees = f"entrées {annee}"

    for cinema in data_select:
        try:
            entrees = to_float(cinema.get(colonne_entrees, 0))
            seances = to_float(cinema.get("séances", 1))
            ratio = entrees / seances if seances else 0
            resultats.append(round(ratio, 2))
        except (ValueError, TypeError):
            continue
    return resultats


def taux_rotation_fauteuils_select(data, annee, **kwargs):
    """
    

    Parameters
    ----------
    data : TYPE
        DESCRIPTION.
    annee : TYPE
        DESCRIPTION.
    **kwargs : TYPE
        DESCRIPTION.

    Returns
    -------
    resultats : TYPE
        DESCRIPTION.

    """
    data_select = selection_donnees(data, **kwargs)
    colonne_entrees = f"entrées {annee}"
    resultats = []

    for cinema in data_select:
        try:
            entrees = to_float(cinema.get(colonne_entrees, 0))
            fauteuils = to_float(cinema.get("fauteuils", 1))
            semaines = to_float(cinema.get("semaines d'activité", 1))
            taux_rotation = entrees / (fauteuils * semaines) if fauteuils and semaines else 0
            resultats.append(round(taux_rotation, 2))
        except (ValueError, TypeError):
            continue
    return resultats


def entrees_par_habitant_commune_select(data, annee, **kwargs):
    """
    

    Parameters
    ----------
    data : TYPE
        DESCRIPTION.
    annee : TYPE
        DESCRIPTION.
    **kwargs : TYPE
        DESCRIPTION.

    Returns
    -------
    resultats : TYPE
        DESCRIPTION.

    """
    data_select = selection_donnees(data, **kwargs)
    colonne_entrees = f"entrées {annee}"
    resultats = []

    for cinema in data_select:
        try:
            entrees = to_float(cinema.get(colonne_entrees, 0))
            population = to_float(cinema.get("population de la commune", 1))
            ratio = entrees / population if population else 0
            resultats.append(round(ratio, 4))
        except (ValueError, TypeError):
            continue
    return resultats


def taux_rotation_films_inédits_select(data, **kwargs):
    """
    

    Parameters
    ----------
    data : TYPE
        DESCRIPTION.
    **kwargs : TYPE
        DESCRIPTION.

    Returns
    -------
    resultats : TYPE
        DESCRIPTION.

    """
    data_select = selection_donnees(data, **kwargs)
    resultats = []

    for cinema in data_select:
        try:
            ecrans = to_float(cinema.get("écrans", 0))
            films = to_float(cinema.get("nombre de films inédits", 0))
            taux_rotation = films / ecrans if ecrans and films else 0
            resultats.append(round(taux_rotation, 2))
        except (ValueError, TypeError):
            continue
    return resultats


def taux_rotation_films_programmés_select(data, **kwargs):
    """
    

    Parameters
    ----------
    data : TYPE
        DESCRIPTION.
    **kwargs : TYPE
        DESCRIPTION.

    Returns
    -------
    resultats : TYPE
        DESCRIPTION.

    """
    data_select = selection_donnees(data, **kwargs)
    resultats = []

    for cinema in data_select:
        try:
            ecrans = to_float(cinema.get("écrans", 0))
            films = to_float(cinema.get("nombre de films programmés", 0))
            taux_rotation = films / ecrans if ecrans and films else 0
            resultats.append(round(taux_rotation, 2))
        except (ValueError, TypeError):
            continue
    return resultats



#Tableau sur plusieurs années (faudra concatener les resultats pour les differentes années) et c'est aussi possible par commune 
def total_indicateurs_select(data, annee, **kwargs):
    """
    Calcule les indicateurs globaux pour une année donnée :
    total d'écrans, fauteuils, séances, films, entrées, etc.

    Paramètres
    ----------
    data : list[dict]
        Données des cinémas.
    annee : str
        Année à analyser.
    **kwargs : filtres éventuels (commune, région, etc.)

    Retourne
    --------
    list[dict]
        Dictionnaire contenant les totaux globaux.
    """
    data_select = selection_donnees(data,**kwargs)
    colonne_entrees = f"entrées {annee}"
    resultats = []
    ecrans = []
    fauteuils = []
    entrees = []
    seances = []
    films = []

    for cinema in data_select:
        try:
            ecrans.append(to_float(cinema.get("écrans", 0)))
            fauteuils.append(to_float(cinema.get("fauteuils", 0)))
            entrees.append(to_float(cinema.get(colonne_entrees, 0)))
            seances.append(to_float(cinema.get("séances", 0)))
            films.append(to_float(cinema.get("nombre de films programmés", 0)))
        except (ValueError, TypeError):
            continue

    resultats.append({
        "Annee": annee,
        "Nombre de cinémas": len(data_select),
        "Nombre d'écrans": sum(ecrans),
        "Nombre de fauteuils": sum(fauteuils),
        "Nombre de films": sum(films),
        "Nombre de séances": sum(seances),
        "Nombre d'entrées": sum(entrees)
    })

#     return resultats

# def exporter_list(datalist,fichier) :
#     """
    

#     Parameters
#     ----------
#     datalist : TYPE
#         DESCRIPTION.
#     fichier : TYPE
#         DESCRIPTION.

#     Returns
#     -------
#     list of list 

#     """
    
#     with open(fichier,"w") as fich :
#         writer=csv.writer(fich,delimiter=";",lineterminator="\n")
#         writer.writerows(datalist)
#     return fichier


     

import csv

def exporter_resultats_dict_csv(data, nom_fichier="resultats.csv"):
    """
    Exporte une liste de dictionnaires dans un fichier CSV, compatible avec Excel français.

    Paramètres
    ----------
    data : list of dict
        Liste des résultats à exporter. Chaque dictionnaire correspond à une ligne.
    nom_fichier : str
        Nom du fichier CSV à créer (par défaut : 'resultats.csv').

    Retour
    ------
    Aucun. Le fichier CSV est écrit dans le répertoire courant.
    """
    if not data:
        print("Aucune donnée à exporter.")
        return

    # Encodage UTF-8 BOM pour compatibilité avec Excel
    with open(nom_fichier, "w", newline="", encoding="utf-8-sig") as fich:
        fieldnames = list(data[0].keys())
        writer = csv.DictWriter(fich, fieldnames=fieldnames, delimiter=";")
        writer.writeheader()

        for ligne in data:
            ligne_formattee = {}
            for k, v in ligne.items():
                if isinstance(v, float):
                    # Convertir le float en string avec virgule au lieu de point
                    ligne_formattee[k] = str(v).replace('.', ',')
                elif isinstance(v, str):
                    # Nettoyer les caractères invisibles ou extra blancs
                    ligne_formattee[k] = v.strip()
                else:
                    ligne_formattee[k] = v
            writer.writerow(ligne_formattee)

    print(f"✅ Fichier exporté avec succès : {nom_fichier}")



# #materiel

def tableau_materiel_par_region(data, annee):
    """
    Calcule les indicateurs globaux de matériel cinéma pour chaque région présente dans les données.

    Paramètres
    ----------
    data : list[dict]
        Liste des données des cinémas.
    annee : str
        Année à analyser (ex : "2022").

    Retourne
    --------
    list[dict]
        Liste de résultats avec les indicateurs pour chaque région.
    """
    colonne_entrees = f"entrées {annee}"
    regions_vues = []
    resultats = []

    for cinema in data:
        region = cinema.get("région administrative", "Inconnu")

        # Si on a déjà traité cette région, on saute
        if region in regions_vues:
            continue

        regions_vues.append(region)
        nb_cinemas = 0
        nb_ecrans = 0
        nb_fauteuils = 0
        nb_seances = 0
        nb_entrees = 0
        nb_multiplexes = 0
        population_totale = 0

        for c in data:
            if c.get("région administrative", "Inconnu") == region:
                nb_cinemas += 1
                nb_ecrans += to_float(c.get("écrans", 0))
                nb_fauteuils += to_float(c.get("fauteuils", 0))
                nb_seances += to_float(c.get("séances", 0))
                nb_entrees += to_float(c.get(colonne_entrees, 0))
                population_totale += to_float(c.get("population de la commune", 0))
                if c.get("multiplexe", "").upper() == "OUI":
                    nb_multiplexes += 1

        taux_fauteuils_par_habitant = (
            round((nb_fauteuils / population_totale)*100, 2)
            if population_totale else 0
        )

        resultats.append({
            "Région": region,
            "Année": annee,
            "Nombre de cinémas": nb_cinemas,
            "Nombre d'écrans": nb_ecrans,
            "Nombre de fauteuils": nb_fauteuils,
            "Nombre de séances": nb_seances,
            "Nombre d'entrées": nb_entrees,
            "Nombre de multiplexes": nb_multiplexes,
            "Taux de fauteuils par habitant": taux_fauteuils_par_habitant
        })

    return resultats

# def tableau_materiel_par_commune(data, annee):
#     """
#     Calcule les indicateurs globaux de matériel cinéma pour chaque région présente dans les données.

#     Paramètres
#     ----------
#     data : list[dict]
#         Liste des données des cinémas.
#     annee : str
#         Année à analyser (ex : "2022").

#     Retourne
#     --------
#     list[dict]
#         Liste de résultats avec les indicateurs pour chaque région.
#     """
#     colonne_entrees = f"entrées {annee}"
#     communes_vues = []
#     resultats = []

#     for cinema in data:
#         commune = cinema.get("commune", "Inconnu")

#         # Si on a déjà traité cette région, on saute
#         if commune in communes_vues:
#             continue

#         communes_vues.append(commune)
#         nb_cinemas = 0
#         nb_ecrans = 0
#         nb_fauteuils = 0
#         nb_seances = 0
#         nb_entrees = 0
#         nb_multiplexes = 0
#         population_totale = 0

#         for c in data:
#             if c.get("commune", "Inconnu") == commune:
#                 nb_cinemas += 1
#                 nb_ecrans += to_float(c.get("écrans", 0))
#                 nb_fauteuils += to_float(c.get("fauteuils", 0))
#                 nb_seances += to_float(c.get("séances", 0))
#                 nb_entrees += to_float(c.get(colonne_entrees, 0))
#                 population_totale += to_float(c.get("population de la commune", 0))
#                 if c.get("multiplexe", "").upper() == "OUI":
#                     nb_multiplexes += 1

#         taux_fauteuils_par_habitant = (
#             round((nb_fauteuils / population_totale)*100, 2)
#             if population_totale else 0
#         )

#         resultats.append({
#             "Commune": commune,
#             "Année": annee,
#             "Nombre de cinémas": nb_cinemas,
#             "Nombre d'écrans": nb_ecrans,
#             "Nombre de fauteuils": nb_fauteuils,
#             "Nombre de séances": nb_seances,
#             "Nombre d'entrées": nb_entrees,
#             "Nombre de multiplexes": nb_multiplexes,
#             "Taux de fauteuils par habitant": taux_fauteuils_par_habitant
#         })

#     return resultats


# def tableau_materiel_par_dep(data, annee):
#     """
#     Calcule les indicateurs globaux de matériel cinéma pour chaque région présente dans les données.

#     Paramètres
#     ----------
#     data : list[dict]
#         Liste des données des cinémas.
#     annee : str
#         Année à analyser (ex : "2022").

#     Retourne
#     --------
#     list[dict]
#         Liste de résultats avec les indicateurs pour chaque région.
#     """
#     colonne_entrees = f"entrées {annee}"
#     deps_vues = []
#     resultats = []

#     for cinema in data:
#         dep = cinema.get("DEP", "Inconnu")

#         # Si on a déjà traité cette région, on saute
#         if dep in deps_vues:
#             continue

#         deps_vues.append(dep)
#         nb_cinemas = 0
#         nb_ecrans = 0
#         nb_fauteuils = 0
#         nb_seances = 0
#         nb_entrees = 0
#         nb_multiplexes = 0
#         population_totale = 0

#         for c in data:
#             if c.get("DEP", "Inconnu") == dep:
#                 nb_cinemas += 1
#                 nb_ecrans += to_float(c.get("écrans", 0))
#                 nb_fauteuils += to_float(c.get("fauteuils", 0))
#                 nb_seances += to_float(c.get("séances", 0))
#                 nb_entrees += to_float(c.get(colonne_entrees, 0))
#                 population_totale += to_float(c.get("population de la commune", 0))
#                 if c.get("multiplexe", "").upper() == "OUI":
#                     nb_multiplexes += 1

#         taux_fauteuils_par_habitant = (
#             round((nb_fauteuils / population_totale)*100, 2)
#             if population_totale else 0
#         )

#         resultats.append({
#             "Départements": dep,
#             "Année": annee,
#             "Nombre de cinémas": nb_cinemas,
#             "Nombre d'écrans": nb_ecrans,
#             "Nombre de fauteuils": nb_fauteuils,
#             "Nombre de séances": nb_seances,
#             "Nombre d'entrées": nb_entrees,
#             "Nombre de multiplexes": nb_multiplexes,
#             "Taux de fauteuils par habitant": taux_fauteuils_par_habitant
#         })

#     return resultats


# def tableau_materiel_par_zone(data, annee):
#     """
#     Calcule les indicateurs globaux de matériel cinéma pour chaque région présente dans les données.

#     Paramètres
#     ----------
#     data : list[dict]
#         Liste des données des cinémas.
#     annee : str
#         Année à analyser (ex : "2022").

#     Retourne
#     --------
#     list[dict]
#         Liste de résultats avec les indicateurs pour chaque région.
#     """
#     colonne_entrees = f"entrées {annee}"
#     zones_vues = []
#     resultats = []

#     for cinema in data:
#         zone = cinema.get("zone de la commune", "Inconnu")

#         # Si on a déjà traité cette région, on saute
#         if zone in zones_vues:
#             continue

#         zones_vues.append(zone)
#         nb_cinemas = 0
#         nb_ecrans = 0
#         nb_fauteuils = 0
#         nb_seances = 0
#         nb_entrees = 0
#         nb_multiplexes = 0
#         population_totale = 0

#         for c in data:
#             if c.get("zone de la commune", "Inconnu") == zone:
#                 nb_cinemas += 1
#                 nb_ecrans += to_float(c.get("écrans", 0))
#                 nb_fauteuils += to_float(c.get("fauteuils", 0))
#                 nb_seances += to_float(c.get("séances", 0))
#                 nb_entrees += to_float(c.get(colonne_entrees, 0))
#                 population_totale += to_float(c.get("population de la commune", 0))
#                 if c.get("multiplexe", "").upper() == "OUI":
#                     nb_multiplexes += 1

#         taux_fauteuils_par_habitant = (
#             round((nb_fauteuils / population_totale)*100, 2)
#             if population_totale else 0
#         )

#         resultats.append({
#             "Zone de la commune": zone,
#             "Année": annee,
#             "Nombre de cinémas": nb_cinemas,
#             "Nombre d'écrans": nb_ecrans,
#             "Nombre de fauteuils": nb_fauteuils,
#             "Nombre de séances": nb_seances,
#             "Nombre d'entrées": nb_entrees,
#             "Nombre de multiplexes": nb_multiplexes,
#             "Taux de fauteuils par habitant": taux_fauteuils_par_habitant
#         })

#     return resultats



# #programmation:

 

def tableau_programmation_par_region(data, annee):
    regions_vues = []
    resultats = []

    for cinema in data:
        region = cinema.get("région administrative", "Inconnu")
        if region in regions_vues:
            continue
        regions_vues.append(region)

        nb_cinemas = 0
        nb_semaines = 0
        nb_seances = 0
        nb_films = 0
        nb_inedits = 0

        for c in data:
            if c.get("région administrative", "Inconnu") == region:
                nb_cinemas += 1
                nb_semaines += to_float(c.get("semaines d'activité", 0))
                nb_seances += to_float(c.get("séances", 0))
                nb_films += to_float(c.get("nombre de films programmés", 0))
                nb_inedits += to_float(c.get("nombre de films inédits", 0))

        inedits_taux = taux_rotation_films_inédits_select(data, **{"région administrative": region})
        programmes_taux = taux_rotation_films_programmés_select(data, **{"région administrative": region})

        taux_rotation_inedit = round(sum(inedits_taux) / len(inedits_taux), 2) if inedits_taux else 0
        taux_rotation_pro = round(sum(programmes_taux) / len(programmes_taux), 2) if programmes_taux else 0

        resultats.append({
            "Région": region,
            "Année": annee,
            "Nombre de cinémas": nb_cinemas,
            "Semaines d'activité": nb_semaines,
            "Nombre de séances": nb_seances,
            "Nombre de films programmés": nb_films,
            "Nombre de films inédits": nb_inedits,
            "Taux de rotation de film inédit sur écran": taux_rotation_inedit,
            "Taux de rotation de film programmés sur écran": taux_rotation_pro
        })

    return resultats



# def tableau_programmation_par_commune(data, annee):
#     communes_vues = []
#     resultats = []

#     for cinema in data:
#         commune = cinema.get("commune", "Inconnu")
#         if commune in communes_vues:
#             continue
#         communes_vues.append(commune)

#         nb_cinemas = 0
#         nb_semaines = 0
#         nb_seances = 0
#         nb_films = 0
#         nb_inedits = 0

#         for c in data:
#             if c.get("commune", "Inconnu") == commune:
#                 nb_cinemas += 1
#                 nb_semaines += to_float(c.get("semaines d'activité", 0))
#                 nb_seances += to_float(c.get("séances", 0))
#                 nb_films += to_float(c.get("nombre de films programmés", 0))
#                 nb_inedits += to_float(c.get("nombre de films inédits", 0))

#         inedits_taux = taux_rotation_films_inédits_select(data, **{"commune": commune})
#         programmes_taux = taux_rotation_films_programmés_select(data, **{"commune": commune})

#         taux_rotation_inedit = round(sum(inedits_taux) / len(inedits_taux), 2) if inedits_taux else 0
#         taux_rotation_pro = round(sum(programmes_taux) / len(programmes_taux), 2) if programmes_taux else 0

#         resultats.append({
#             "Commune": commune,
#             "Année": annee,
#             "Nombre de cinémas": nb_cinemas,
#             "Semaines d'activité": nb_semaines,
#             "Nombre de séances": nb_seances,
#             "Nombre de films programmés": nb_films,
#             "Nombre de films inédits": nb_inedits,
#             "Taux de rotation de film inédit sur écran": taux_rotation_inedit,
#             "Taux de rotation de film programmés sur écran": taux_rotation_pro
#         })

#     return resultats


# def tableau_programmation_par_zone(data, annee):
#     zones_vues = []
#     resultats = []

#     for cinema in data:
#         zone = cinema.get("zone de la commune", "Inconnu")
#         if zone in zones_vues:
#             continue
#         zones_vues.append(zone)

#         nb_cinemas = 0
#         nb_semaines = 0
#         nb_seances = 0
#         nb_films = 0
#         nb_inedits = 0

#         for c in data:
#             if c.get("zone de la commune", "Inconnu") == zone:
#                 nb_cinemas += 1
#                 nb_semaines += to_float(c.get("semaines d'activité", 0))
#                 nb_seances += to_float(c.get("séances", 0))
#                 nb_films += to_float(c.get("nombre de films programmés", 0))
#                 nb_inedits += to_float(c.get("nombre de films inédits", 0))

#         inedits_taux = taux_rotation_films_inédits_select(data, **{"zone de la commune": zone})
#         programmes_taux = taux_rotation_films_programmés_select(data, **{"zone de la commune": zone})

#         taux_rotation_inedit = round(sum(inedits_taux) / len(inedits_taux), 2) if inedits_taux else 0
#         taux_rotation_pro = round(sum(programmes_taux) / len(programmes_taux), 2) if programmes_taux else 0

#         resultats.append({
#             "Zone de la commune": zone,
#             "Année": annee,
#             "Nombre de cinémas": nb_cinemas,
#             "Semaines d'activité": nb_semaines,
#             "Nombre de séances": nb_seances,
#             "Nombre de films programmés": nb_films,
#             "Nombre de films inédits": nb_inedits,
#             "Taux de rotation de film inédit sur écran": taux_rotation_inedit,
#             "Taux de rotation de film programmés sur écran": taux_rotation_pro
#         })

#     return resultats


# #frequentation :

def tableau_frequentation_par_region(data, annee):
    colonne_entrees = f"entrées {annee}"
    regions_vues = []
    resultats = []

    for cinema in data:
        region = cinema.get("région administrative", "Inconnu")
        if region in regions_vues:
            continue
        regions_vues.append(region)

        total_entrees = 0
        for c in data:
            if c.get("région administrative", "Inconnu") == region:
                total_entrees += to_float(c.get(colonne_entrees, 0))

        taux_freq_fauteuils = taux_frequentation_par_fauteuil_select(data, annee, **{"région administrative": region})
        entree_par_habitant = entrees_par_habitant_commune_select(data, annee, **{"région administrative": region})
        rotation_fauteuils = taux_rotation_fauteuils_select(data, annee, **{"région administrative": region})
        entrees_par_seance = entrees_par_seance_select(data, annee, **{"région administrative": region})

        resultats.append({
            "Région": region,
            "Année": annee,
            "Entrées": total_entrees,
            "Taux de fréquentation par fauteuils": round(sum(taux_freq_fauteuils) / len(taux_freq_fauteuils), 2) if taux_freq_fauteuils else 0,
            "Taux de rotation des fauteuils": round(sum(rotation_fauteuils) / len(rotation_fauteuils), 2) if rotation_fauteuils else 0,
            "Entrées par séance": round(sum(entrees_par_seance) / len(entrees_par_seance), 2) if entrees_par_seance else 0,
            "Entrées par habitant": round(sum(entree_par_habitant) / len(entree_par_habitant), 4) if entree_par_habitant else 0
        })

    return resultats
  

# def tableau_frequentation_par_dep(data, annee):
#     colonne_entrees = f"entrées {annee}"
#     deps_vues = []
#     resultats = []

#     for cinema in data:
#         dep = cinema.get("DEP", "Inconnu")
#         if dep in deps_vues:
#             continue
#         deps_vues.append(dep)

#         total_entrees = 0
#         for c in data:
#             if c.get("DEP", "Inconnu") == dep:
#                 total_entrees += to_float(c.get(colonne_entrees, 0))

#         taux_freq_fauteuils = taux_frequentation_par_fauteuil_select(data, annee, **{"DEP": dep})
#         entree_par_habitant = entrees_par_habitant_commune_select(data, annee, **{"DEP": dep})
#         rotation_fauteuils = taux_rotation_fauteuils_select(data, annee, **{"DEP": dep})
#         entrees_par_seance = entrees_par_seance_select(data, annee, **{"DEP": dep})

#         resultats.append({
#             "Département": dep,
#             "Année": annee,
#             "Entrées": total_entrees,
#             "Taux de fréquentation par fauteuils": round(sum(taux_freq_fauteuils) / len(taux_freq_fauteuils), 2) if taux_freq_fauteuils else 0,
#             "Taux de rotation des fauteuils": round(sum(rotation_fauteuils) / len(rotation_fauteuils), 2) if rotation_fauteuils else 0,
#             "Entrées par séance": round(sum(entrees_par_seance) / len(entrees_par_seance), 2) if entrees_par_seance else 0,
#             "Entrées par habitant": round(sum(entree_par_habitant) / len(entree_par_habitant), 4) if entree_par_habitant else 0
#         })

#     return resultats


# def tableau_frequentation_par_zone(data, annee):
#     colonne_entrees = f"entrées {annee}"
#     zones_vues = []
#     resultats = []

#     for cinema in data:
#         zone = cinema.get("zone de la commune", "Inconnu")
#         if zone in zones_vues:
#             continue
#         zones_vues.append(zone)

#         total_entrees = 0
#         for c in data:
#             if c.get("zone de la commune", "Inconnu") == zone:
#                 total_entrees += to_float(c.get(colonne_entrees, 0))

#         taux_freq_fauteuils = taux_frequentation_par_fauteuil_select(data, annee, **{"zone de la commune": zone})
#         entree_par_habitant = entrees_par_habitant_commune_select(data, annee, **{"zone de la commune": zone})
#         rotation_fauteuils = taux_rotation_fauteuils_select(data, annee, **{"zone de la commune": zone})
#         entrees_par_seance = entrees_par_seance_select(data, annee, **{"zone de la commune": zone})

#         resultats.append({
#             "Zone de la commune": zone,
#             "Année": annee,
#             "Entrées": total_entrees,
#             "Taux de fréquentation par fauteuils": round(sum(taux_freq_fauteuils) / len(taux_freq_fauteuils), 2) if taux_freq_fauteuils else 0,
#             "Taux de rotation des fauteuils": round(sum(rotation_fauteuils) / len(rotation_fauteuils), 2) if rotation_fauteuils else 0,
#             "Entrées par séance": round(sum(entrees_par_seance) / len(entrees_par_seance), 2) if entrees_par_seance else 0,
#             "Entrées par habitant": round(sum(entree_par_habitant) / len(entree_par_habitant), 4) if entree_par_habitant else 0
#         })

#     return resultats

# def classer_list_dict(list_of_lists):
#     # Aplatir la liste de listes
#     liste_flat = [d for sublist in list_of_lists for d in sublist]
    
#     # Trier par 'annee' puis 'Territoire'
#     liste_triee = sorted(liste_flat, key=lambda x: (x.get('annee'), x.get('Territoire')))
    
#     return liste_triee

def fusionner_et_trier(donnees_liste, regroupement): 
    # Fusionner les sous-listes en une seule
    liste_fusionnee = [d for sous_liste in donnees_liste for d in sous_liste]

    # Clés de tri secondaires selon le type de regroupement
    cles_tri = {
        "region": lambda d: d.get("Region") or d.get("Région") or d.get("Territoire"),
        "commune": lambda d: d.get("Commune") or d.get("Territoire"),
        "departement": lambda d: d.get("Departement") or d.get("Département") or d.get("Territoire"),
        "zone": lambda d: (
            d.get("Zone de la commune", ""),
            d.get("Région", ""),
            d.get("Département", ""),
            d.get("Commune", "")
        ),
    }

    # Récupérer la clé de tri principale
    key_fonction = cles_tri.get(regroupement.lower(), lambda d: d.get("Territoire", ""))

    # Trier : d'abord par région (ou regroupement), puis par année
    liste_triee = sorted(liste_fusionnee, key=lambda d: (key_fonction(d), d["Année"]))

    return liste_triee




    
# #Test des fonctions :


file = "DATA/Donnéescartographie"
data_2020 = charger_donnees(file + "2020.csv")
data_2021= charger_donnees(file + "2021.csv")
data_2018= charger_donnees_2018(file + "2018.csv")
data_2019= charger_donnees(file + "2019.csv")
data_2022= charger_donnees(file + "2022.csv")

donnees_par_annee = {
    2018: data_2018,
    2019: data_2019,
    2020: data_2020,
    2021: data_2021,2022: data_2022
}
TM_region=[]

TP_region=[]

TF_region=[]

for annee, data in donnees_par_annee.items():
    # MATERIEL
    total_materiel_region = tableau_materiel_par_region(data, annee)
    afficher(total_materiel_region)
    TM_region.append(total_materiel_region)
    exporter_resultats_dict_csv(total_materiel_region, f"C:/Users/Nya Devas/Desktop/SAE_Cinema/APPLICATION/EXPORT/STATISTIQUES/materiel_cinema_region_{annee}.csv")

   
    # PROGRAMMATION
   
    total_prog_region = tableau_programmation_par_region(data, annee)
    afficher(total_prog_region)
    TP_region.append(total_prog_region)
    exporter_resultats_dict_csv(total_prog_region, f"C:/Users/Nya Devas/Desktop/SAE_Cinema/APPLICATION/EXPORT/STATISTIQUES/programmation_cinema_region_{annee}.csv")

   
    # FREQUENTATION
   
    total_freq_region = tableau_frequentation_par_region(data, annee)
    afficher(total_freq_region)
    TF_region.append(total_freq_region)
    exporter_resultats_dict_csv(total_freq_region, f"C:/Users/Nya Devas/Desktop/SAE_Cinema/APPLICATION/EXPORT/STATISTIQUES/Fréquentation_cinema_region_{annee}.csv")

# Fusionner, trier et exporter les listes TM_*
TM_region_trie = fusionner_et_trier(TM_region, "region")

# Afficher
afficher(TM_region_trie)

# Exporter
exporter_resultats_dict_csv(TM_region_trie, "C:/Users/Nya Devas/Desktop/SAE_Cinema/APPLICATION/EXPORT/STATISTIQUES/tout_materiel_par_region.csv")

# --- Fusionner, trier et exporter ---

# Programmation
TP_region_trie = fusionner_et_trier(TP_region, "region")

afficher(TP_region_trie)

exporter_resultats_dict_csv(TP_region_trie, "C:/Users/Nya Devas/Desktop/SAE_Cinema/APPLICATION/EXPORT/STATISTIQUES/tout_programmation_par_region.csv")

# Fréquentation

TF_region_trie = fusionner_et_trier(TF_region, "region")


afficher(TF_region_trie)

exporter_resultats_dict_csv(TF_region_trie, "C:/Users/Nya Devas/Desktop/SAE_Cinema/APPLICATION/EXPORT/STATISTIQUES/tout_frequentation_par_region.csv")   
# 1. charger_donnees
# data_simple = charger_donnees(file + "2020.csv", debut=0, fin=10)
# afficher(data_simple)

# # 2. charger_fileS
# data_multi = charger_fileS(file + "2020.csv", file + "2021.csv", debut=0, fin=5)
# for d in data_multi:
#     afficher(d, limite=3)

# # 3. charger_donnees_var
# data_vars = charger_donnees_var(file + "2020.csv", "nom", "fauteuils")
# afficher(data_vars)

# # 4. charger_donnees_selection
# data_filtre = charger_donnees_selection(file + "2020.csv", DEP="75")
# afficher(data_filtre, limite=5)

# # 5. selection_donnees
# data_selection = selection_donnees(data_2020, DEP="75")
# afficher(data_selection, limite=5)

# # 6. renommer_variable
# renommer_variable(data_2020, "code INSEE","INSEE")
# afficher(data_2020, limite=3)

# # 7. renommer_variables
# renommer_variables(data_2020, ["fauteuils", "écrans"], ["nb_fauteuils", "nb_ecrans"])
# afficher(data_2020, limite=3)

# # 8. keep
# data_keep = keep(data_2020, "nom", "fauteuils")
# afficher(data_keep)

# # 9. drop
# data_drop = drop(data_2020, "nb_fauteuils", "nb_ecrans")
# afficher(data_drop, limite=3)

# # 10. modalités
# mods = modalités(data_2020, "région administrative")
# print("Modalités région :", mods)

# # 11. nombre_NA
# na_count = nombre_NA(data_2020, "nom")
# print("Nombre de NA pour 'nom':", na_count)

# # 12. taux_na
# na_rate = taux_na(data_2020, "nom")
# print("Taux de NA pour 'nom':", na_rate)

# # 13. description_variable 
# # à mettre dans un fichier excell
# desc = description_variable(data_2020, "nom", "région administrative","commune", "fauteuils","séances","genre")
# for ligne in desc:
#     print(ligne)
# # exporter_list(desc,"C:/Users/Nya Devas/Desktop/SAE_Cinema/APPLICATION/EXPORT/EXTRACTIONS/description_variables_2020.csv")

# # 14. verification_identifiant
# lignes_pb, valeurs_pb = verification_identifiant(data_2020, "commune")
# print("Lignes en erreur ID :", lignes_pb)

# # # 15. valeur_aberrante_limite
# # lignes_aberr, val_aberr = valeur_aberrante_limite(data_2020, "semaines d'activité", 1, 52)
# # print("Valeurs aberrantes (semaines d'activité) :", lignes_aberr)

# #16. verfication_calcul
# #Supposons une variable calculée 'evolution' entre "entrées 2020" et "entrées 2021"
# #Appel si ces colonnes existent
# lignes_calc, val_calc = verfication_calcul(data_2020, "évolution entrées", "entrées 2019", "entrées 2020")

# # 17. verification_type
# erreurs_type = verification_type(data_2020, "fauteuils", float)
# print("Erreurs de type sur nb_fauteuils :", erreurs_type)

# # 18. corriger_anomalies
# data_corrigee = corriger_anomalies(data_2020, "fauteuils","région administrative")
# afficher(data_corrigee, limite=3)

# # 19. taux_frequentation_par_fauteuil
# taux_freq = taux_frequentation_par_fauteuil(data_2020, 2020,DEP="75")
# afficher(taux_freq, limite=5)
# exporter_resultats_dict_csv(taux_freq,"C:/Users/Nya Devas/Desktop/SAE_Cinema/APPLICATION/EXPORT/STATISTIQUES/taux_freq_fauteuils_dep_75_2020.csv")

# # # 20. entrees_par_seance
# entree_seance = entrees_par_seance(data_2020, 2020, DEP="75")
# afficher(entree_seance, limite=5)
# exporter_resultats_dict_csv(entree_seance,"C:/Users/Nya Devas/Desktop/SAE_Cinema/APPLICATION/EXPORT/STATISTIQUES/entrée_par_seances_dep_75_2020.csv")

# # # # 21. taux_rotation_fauteuils
# rotation_fauteuils = taux_rotation_fauteuils(data_2020, 2020,DEP="75")
# afficher(rotation_fauteuils, limite=5)
# exporter_resultats_dict_csv(rotation_fauteuils,"C:/Users/Nya Devas/Desktop/SAE_Cinema/APPLICATION/EXPORT/STATISTIQUES/taux_rotations_fauteuils_par_semaines_dep_75_2020.csv")

# # # # 22. entrees_par_habitant_commune
# entree_pop = entrees_par_habitant_commune(data_2020, 2020, DEP="75")
# afficher(entree_pop, limite=5)
# exporter_resultats_dict_csv(entree_pop,"C:/Users/Nya Devas/Desktop/SAE_Cinema/APPLICATION/EXPORT/STATISTIQUES/nombre_d'entrées_par_habitant_dep_75_2020.csv")
 

# # 23. taux_rotation_films_inédits
# rotation_inedits = taux_rotation_films_inédits(data_2020,DEP="75")
# afficher(rotation_inedits, limite=5)
# exporter_resultats_dict_csv(rotation_inedits,"C:/Users/Nya Devas/Desktop/SAE_Cinema/APPLICATION/EXPORT/STATISTIQUES/rotations_films_inedits_par_ecran_dep_75_2020.csv")


# # # 24. taux_rotation_films_programmés
# rotation_programmes = taux_rotation_films_programmés(data_2020,DEP="75")
# afficher(rotation_programmes, limite=5)
# exporter_resultats_dict_csv(rotation_programmes,"C:/Users/Nya Devas/Desktop/SAE_Cinema/APPLICATION/EXPORT/STATISTIQUES/rotations_films_programmés_par_ecran_dep_75_2020.csv")
# # #25. total d'indicateur

# # total_indicateur=total_indicateurs(data_2021,2021,DEP="75")+total_indicateurs(data_2020,2020,DEP="75")+total_indicateurs(data_2019,2019,DEP="75")+total_indicateurs(data_2018,2018,DEP="75")
# # afficher(total_indicateur)
# # exporter_resultats_dict_csv(total_indicateur,"C:/Users/Nya Devas/Desktop/SAE_Cinema/APPLICATION/EXPORT/STATISTIQUES/indicateurs_cinema_dep_75.csv")

#MATERIEL REGION 
#------------------nombre de cinema--------------------------------#
import pandas as pd
import matplotlib.pyplot as plt

# 📄 Chemin du fichier CSV
chemin_fichier = "C:/Users/Nya Devas/Desktop/SAE_Cinema/APPLICATION/EXPORT/STATISTIQUES/tout_materiel_par_region.csv"

# 📊 Lecture du fichier CSV avec le bon séparateur
df = pd.read_csv(chemin_fichier, sep=';')

# 🧹 Nettoyage des noms de colonnes
df.columns = df.columns.str.strip()

# 🔍 Affichage pour vérifier les colonnes
print("Colonnes du fichier :", df.columns)

# 🎨 Préparation du graphique
plt.figure(figsize=(15, 12))

# 🔁 Tracer une ligne pour chaque région
regions = df["Région"].unique()
for region in regions:
    sous_df = df[df["Région"] == region].sort_values("Année")
    plt.plot(sous_df["Année"], sous_df["Nombre de cinémas"], marker='o', label=region)

# 🖼 Mise en forme du graphique
plt.title("🎬 Évolution du nombre de cinémas par région", fontsize=16)
plt.xlabel("Année", fontsize=12)
plt.ylabel("Nombre de cinémas", fontsize=12)
plt.legend(title="Régions", fontsize=10)
plt.grid(True)
plt.tight_layout()

# 💾 Sauvegarde du graphique dans un fichier PNG
chemin_sortie = "C:/Users/Nya Devas/Desktop/SAE_Cinema/APPLICATION/Graphique/cinemas_par_region.png"
plt.savefig(chemin_sortie, dpi=300)
print(f"✅ Graphique enregistré ici : {chemin_sortie}")

# 📺 Affichage du graphique (optionnel si tu l'insères ensuite dans RMarkdown)
plt.show()


#----------------------nombre d'ecrans---------------------------------#




import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

chemin_fichier = "C:/Users/Nya Devas/Desktop/SAE_Cinema/APPLICATION/EXPORT/STATISTIQUES/tout_materiel_par_region.csv"

# Lisez le CSV en spécifiant le séparateur décimal
df = pd.read_csv(chemin_fichier, sep=';', decimal=',')

# Nettoyage et conversion en numérique (plus robuste si nécessaire)
# Assurez-vous qu'il n'y a pas d'espaces blancs ou d'autres caractères invisibles
df["Nombre d'écrans"] = df["Nombre d'écrans"].astype(str).str.strip()
# Optionnel: Si vous avez des valeurs bizarres comme 'nan' en chaîne de caractères, remplacez-les
df["Nombre d'écrans"] = df["Nombre d'écrans"].replace('nan', pd.NA)
df["Nombre d'écrans"] = pd.to_numeric(df["Nombre d'écrans"], errors='coerce')


# --- Étape de vérification CRUCIALE ---
print("\n--- Débogage Type de Données ---")
print("Type de la colonne 'Nombre d'écrans' APRES toutes les conversions :", df["Nombre d'écrans"].dtype)
print("Nombre de valeurs manquantes (NaN) dans 'Nombre d'écrans' :", df["Nombre d'écrans"].isna().sum())
if df["Nombre d'écrans"].isna().sum() > 0:
    print("Lignes avec des valeurs NaN dans 'Nombre d'écrans' :")
    print(df[df["Nombre d'écrans"].isna()])
print("--- Fin Débogage ---")
# --- Fin Étape de vérification ---


plt.figure(figsize=(15, 12))

regions = df["Région"].unique()

for region in regions:
    sous_df = df[df["Région"] == region]

    # TRÈS IMPORTANT : S'assurer que les données sont triées par année pour le tracé
    # Puis, trier par le nombre d'écrans pour l'axe Y si on soupçonne un problème de tri d'axe Y
    # Bien que normalement Matplotlib gère ça si la colonne est numérique
    sous_df = sous_df.sort_values(by=["Année", "Nombre d'écrans"]) # Tri par Année puis par Nombre d'écrans


    # Re-vérification du type juste avant le tracé
    # Si le dtype est toujours 'object' ici, c'est la cause du problème
    if sous_df["Nombre d'écrans"].dtype == 'object':
        print(f"ATTENTION: La colonne 'Nombre d'écrans' pour la région {region} est toujours de type 'object' lors du tracé !")


    plt.plot(sous_df["Année"], sous_df["Nombre d'écrans"], marker='o', label=region)

plt.title("🎬 Évolution du Nombre d'écrans par région", fontsize=16)
plt.xlabel("Année", fontsize=12)
plt.ylabel("Nombre d'écrans", fontsize=12)
plt.legend(title="Régions", fontsize=10)
plt.grid(True)

# Configuration de l'échelle Y
plt.ylim(0, 1000)
plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(100))
plt.gca().yaxis.set_major_formatter(ticker.FormatStrFormatter('%d'))

plt.tight_layout()

chemin_sortie = "C:/Users/Nya Devas/Desktop/SAE_Cinema/APPLICATION/Graphique/nombre_ecrans_par_region.png"
plt.savefig(chemin_sortie, dpi=300)
print(f"✅ Graphique enregistré ici : {chemin_sortie}")


#----------------------------------------------------nombre de fauteuils -------------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

chemin_fichier = "C:/Users/Nya Devas/Desktop/SAE_Cinema/APPLICATION/EXPORT/STATISTIQUES/tout_materiel_par_region.csv"

df = pd.read_csv(chemin_fichier, sep=';', decimal=',')

df.columns = df.columns.str.strip() # Assure que les noms de colonnes sont propres

# Nettoyage et conversion en numérique pour 'Nombre de fauteuils'
df["Nombre de fauteuils"] = pd.to_numeric(df["Nombre de fauteuils"], errors='coerce')

# Harmonisation des noms de région
# Assurez-vous qu'il n'y a pas de caractères invisibles ou d'erreurs ici.
df["Région"] = df["Région"].astype(str).str.replace(" / ", "-").str.strip()


# --- NOUVELLE ÉTAPE DE DÉBOGAGE POUR LES RÉGIONS ---
print("\n--- Débogage des Noms de Régions ---")
print("Noms de régions uniques APRES harmonisation :")
print(df["Région"].unique())
print("Nombre de valeurs vides ou nulles dans 'Région' :", df["Région"].isnull().sum())
print("--- Fin Débogage des Régions ---")
# --- Fin NOUVELLE ÉTAPE DE DÉBOGAGE ---


plt.figure(figsize=(15, 12))

regions = df["Région"].unique()

# Assurez-vous qu'il n'y a pas de chaîne vide ou de NaN dans 'regions'
regions = [r for r in regions if pd.notna(r) and r != '']

if not regions:
    print("ATTENTION: Aucune région valide trouvée pour le tracé. Vérifiez la colonne 'Région'.")


for region in regions:
    sous_df = df[df["Région"] == region]

    # --- DÉBOGAGE POUR VÉRIFIER LES SOUS-DATAFRAMES ---
    # print(f"Taille du sous-DataFrame pour la région '{region}' : {len(sous_df)} lignes")
    # if len(sous_df) == 0:
    #     print(f"ATTENTION: Le sous-DataFrame pour la région '{region}' est vide. Le nom de la région pourrait être incorrect.")
    # --- FIN DÉBOGAGE POUR VÉRIFIER LES SOUS-DATAFRAMES ---

    # Tri par Année puis par Nombre de fauteuils
    sous_df = sous_df.sort_values(by=["Année", "Nombre de fauteuils"])

    # Vérification du type juste avant le tracé (Débogage)
    if sous_df["Nombre de fauteuils"].dtype == 'object':
        print(f"ATTENTION: La colonne 'Nombre de fauteuils' pour la région {region} est toujours de type 'object' lors du tracé !")

    plt.plot(sous_df["Année"], sous_df["Nombre de fauteuils"], marker='o', label=region)


plt.title("🎬 Évolution du Nombre de fauteuils par région", fontsize=16)
plt.xlabel("Année", fontsize=12)
plt.ylabel("Nombre de fauteuils", fontsize=12)
plt.legend(title="Régions", fontsize=10)
plt.grid(True)

plt.ylim(bottom=0, top=250000)
plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(25000))
plt.gca().yaxis.set_major_formatter(ticker.FormatStrFormatter('%d'))

plt.tight_layout()

chemin_sortie = "C:/Users/Nya Devas/Desktop/SAE_Cinema/APPLICATION/Graphique/nombre_fauteuils_par_region_final.png"
plt.savefig(chemin_sortie, dpi=300)
print(f"✅ Graphique enregistré ici : {chemin_sortie}")








#---------------------nombre de séance --------------------------------------

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

chemin_fichier = "C:/Users/Nya Devas/Desktop/SAE_Cinema/APPLICATION/EXPORT/STATISTIQUES/tout_materiel_par_region.csv"

# Lisez le CSV en spécifiant le séparateur décimal comme la virgule (',')
df = pd.read_csv(chemin_fichier, sep=';', decimal=',')

# Nettoyage des noms de colonnes
df.columns = df.columns.str.strip()

print("Colonnes du fichier :", df.columns)

# Correction: Convertir explicitement la colonne 'Nombre de séances' en numérique
df["Nombre de séances"] = pd.to_numeric(df["Nombre de séances"], errors='coerce')

# Harmonisation des noms de région
df["Région"] = df["Région"].astype(str).str.replace(" / ", "-").str.strip()


# --- ÉTAPE DE DÉBOGAGE POUR LES RÉGIONS ---
print("\n--- Débogage des Noms de Régions ---")
print("Noms de régions uniques APRES harmonisation :")
print(df["Région"].unique())
print("Nombre de valeurs vides ou nulles dans 'Région' :", df["Région"].isnull().sum())
print("--- Fin Débogage des Régions ---")

plt.figure(figsize=(15, 12))

regions = df["Région"].unique()
# Assurez-vous qu'il n'y a pas de chaîne vide ou de NaN dans 'regions'
regions = [r for r in regions if pd.notna(r) and r != '']

if not regions:
    print("ATTENTION: Aucune région valide trouvée pour le tracé. Vérifiez la colonne 'Région'.")


for region in regions:
    sous_df = df[df["Région"] == region]
    # Tri par Année puis par Nombre de séances (pour le débogage si un problème de tri persiste sur l'axe Y)
    sous_df = sous_df.sort_values(by=["Année", "Nombre de séances"])

    # Re-vérification du type juste avant le tracé (Débogage)
    if sous_df["Nombre de séances"].dtype == 'object':
        print(f"ATTENTION: La colonne 'Nombre de séances' pour la région {region} est toujours de type 'object' lors du tracé !")

    plt.plot(sous_df["Année"], sous_df["Nombre de séances"], marker='o', label=region)

# Correction: Titre adapté au contenu
plt.title("🎬 Évolution du Nombre de séances par région", fontsize=16)
plt.xlabel("Année", fontsize=12)
plt.ylabel("Nombre de séances", fontsize=12)
plt.legend(title="Régions", fontsize=10)
plt.grid(True)

# Correction: Configuration de l'axe Y pour le nombre de séances
# Plage de 0 à 2 000 000 avec un pas de 200 000
plt.ylim(bottom=0, top=2_000_000)
plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(200_000))
# Formater les étiquettes avec des séparateurs de milliers
plt.gca().yaxis.set_major_formatter(ticker.FormatStrFormatter('%d')) # Affiche comme des entiers

plt.tight_layout()

# Correction: Nom du fichier de sortie adapté
chemin_sortie = "C:/Users/Nya Devas/Desktop/SAE_Cinema/APPLICATION/Graphique/nombre_seances_par_region_final.png"
plt.savefig(chemin_sortie, dpi=300)
print(f"✅ Graphique enregistré ici : {chemin_sortie}")




#-----------------------nombre d'entrées--------------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

chemin_fichier = "C:/Users/Nya Devas/Desktop/SAE_Cinema/APPLICATION/EXPORT/STATISTIQUES/tout_materiel_par_region.csv"

# Lisez le CSV en spécifiant le séparateur décimal comme la virgule (',')
df = pd.read_csv(chemin_fichier, sep=';', decimal=',')

# Nettoyage des noms de colonnes
df.columns = df.columns.str.strip()

print("Colonnes du fichier :", df.columns)

# Correction: Convertir explicitement la colonne 'Nombre d'entrées' en numérique
df["Nombre d'entrées"] = pd.to_numeric(df["Nombre d'entrées"], errors='coerce')

# Harmonisation des noms de région
df["Région"] = df["Région"].astype(str).str.replace(" / ", "-").str.strip()


# --- ÉTAPE DE DÉBOGAGE POUR LES RÉGIONS ---
print("\n--- Débogage des Noms de Régions ---")
print("Noms de régions uniques APRES harmonisation :")
print(df["Région"].unique())
print("Nombre de valeurs vides ou nulles dans 'Région' :", df["Région"].isnull().sum())
print("--- Fin Débogage des Régions ---")

plt.figure(figsize=(15, 12))

regions = df["Région"].unique()
# Assurez-vous qu'il n'y a pas de chaîne vide ou de NaN dans 'regions'
regions = [r for r in regions if pd.notna(r) and r != '']

if not regions:
    print("ATTENTION: Aucune région valide trouvée pour le tracé. Vérifiez la colonne 'Région'.")


for region in regions:
    sous_df = df[df["Région"] == region]
    # Tri par Année puis par Nombre d'entrées (pour le débogage si un problème de tri persiste sur l'axe Y)
    sous_df = sous_df.sort_values(by=["Année", "Nombre d'entrées"])

    # Re-vérification du type juste avant le tracé (Débogage)
    if sous_df["Nombre d'entrées"].dtype == 'object':
        print(f"ATTENTION: La colonne 'Nombre d'entrées' pour la région {region} est toujours de type 'object' lors du tracé !")

    plt.plot(sous_df["Année"], sous_df["Nombre d'entrées"], marker='o', label=region)

# Correction: Titre adapté au contenu
plt.title("🎬 Évolution du Nombre d'entrées par région", fontsize=16)
plt.xlabel("Année", fontsize=12)
plt.ylabel("Nombre d'entrées", fontsize=12)
plt.legend(title="Régions", fontsize=10)
plt.grid(True)

# Correction: Configuration de l'axe Y pour le nombre d'entrées
# Plage de 0 à 70 000 000 (70 millions) avec un pas de 5 000 000 (5 millions)
plt.ylim(bottom=0, top=70_000_000)
plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(5_000_000))
# Formater les étiquettes avec des séparateurs de milliers
plt.gca().yaxis.set_major_formatter(ticker.FormatStrFormatter('%d')) # Affiche comme des entiers

plt.tight_layout()

# Correction: Nom du fichier de sortie adapté
chemin_sortie = "C:/Users/Nya Devas/Desktop/SAE_Cinema/APPLICATION/Graphique/nombre_entrees_par_region_final.png"
plt.savefig(chemin_sortie, dpi=300)
print(f"✅ Graphique enregistré ici : {chemin_sortie}")

#________________multiplexe------------------------------------------------
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/Nya Devas/Desktop/SAE_Cinema/APPLICATION/EXPORT/STATISTIQUES/tout_materiel_par_region.csv", sep=';')
df.columns = df.columns.str.strip()
df["Année"] = pd.to_numeric(df["Année"], errors="coerce")

plt.figure(figsize=(15, 12))
for region in df["Région"].unique():
    sous_df = df[df["Région"] == region]
    plt.plot(sous_df["Année"], sous_df["Nombre de multiplexes"], marker='o', label=region)

plt.title("🏢 Évolution du nombre de multiplexes par région")
plt.xlabel("Année")
plt.ylabel("Nombre de multiplexes")
plt.legend(title="Région", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig("C:/Users/Nya Devas/Desktop/SAE_Cinema/APPLICATION/Graphique/nombre_multiplexes_par_region.png", dpi=300)
plt.close()

#---------------------------------taux de fauteuils par habitant -----------------------------------------------
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

chemin_fichier = "C:/Users/Nya Devas/Desktop/SAE_Cinema/APPLICATION/EXPORT/STATISTIQUES/tout_materiel_par_region.csv"

df = pd.read_csv(chemin_fichier, sep=';', decimal=',')
df.columns = df.columns.str.strip()

# Conversion de la colonne cible en numérique
df["Taux de fauteuils par habitant"] = pd.to_numeric(df["Taux de fauteuils par habitant"], errors='coerce')

# Harmonisation des noms de région
df["Région"] = df["Région"].astype(str).str.replace(" / ", "-").str.strip()

# --- Débogage Type de Données ---
print("\n--- Débogage Type de Données 'Taux de fauteuils par habitant' ---")
print("Type de la colonne 'Taux de fauteuils par habitant' après conversion :", df["Taux de fauteuils par habitant"].dtype)
print("Nombre de valeurs manquantes (NaN) :", df["Taux de fauteuils par habitant"].isna().sum())
print("--- Fin Débogage ---")

plt.figure(figsize=(15, 12))

regions = df["Région"].unique()
regions = [r for r in regions if pd.notna(r) and r != '']

if not regions:
    print("ATTENTION: Aucune région valide trouvée pour le tracé. Vérifiez la colonne 'Région'.")

for region in regions:
    sous_df = df[df["Région"] == region]
    sous_df = sous_df.sort_values(by=["Année", "Taux de fauteuils par habitant"])

    if sous_df["Taux de fauteuils par habitant"].dtype == 'object':
        print(f"ATTENTION: La colonne 'Taux de fauteuils par habitant' pour la région {region} est toujours de type 'object' lors du tracé !")

    plt.plot(sous_df["Année"], sous_df["Taux de fauteuils par habitant"], marker='o', label=region)

plt.title("🎬 Évolution du Taux de fauteuils par habitant par région", fontsize=16)
plt.xlabel("Année", fontsize=12)
plt.ylabel("Taux de fauteuils par habitant", fontsize=12)
plt.legend(title="Régions", fontsize=10)
plt.grid(True)

# Configuration de l'axe Y (0 à 3, pas de 0.5)
plt.ylim(bottom=0, top=3)
plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(0.5))
plt.gca().yaxis.set_major_formatter(ticker.FormatStrFormatter('%.1f')) # Affichage avec une décimale

plt.tight_layout()

chemin_sortie = "C:/Users/Nya Devas/Desktop/SAE_Cinema/APPLICATION/Graphique/taux_fauteuils_par_habitant_final.png"
plt.savefig(chemin_sortie, dpi=300)
print(f"✅ Graphique enregistré ici : {chemin_sortie}")

#programmation REGION

#-------------------------nombre de fil programmés------------------------------------------------
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

chemin_fichier = "C:/Users/Nya Devas/Desktop/SAE_Cinema/APPLICATION/EXPORT/STATISTIQUES/tout_programmation_par_region.csv"

df = pd.read_csv(chemin_fichier, sep=';', decimal=',')
df.columns = df.columns.str.strip()

df["Nombre de films programmés"] = pd.to_numeric(df["Nombre de films programmés"], errors='coerce')

df["Région"] = df["Région"].astype(str).str.replace(" / ", "-").str.strip()

print("\n--- Débogage Type de Données 'Nombre de films programmés' ---")
print("Type de la colonne 'Nombre de films programmés' après conversion :", df["Nombre de films programmés"].dtype)
print("Nombre de valeurs manquantes (NaN) :", df["Nombre de films programmés"].isna().sum())
print("--- Fin Débogage ---")

plt.figure(figsize=(15, 12))

regions = df["Région"].unique()
regions = [r for r in regions if pd.notna(r) and r != '']

if not regions:
    print("ATTENTION: Aucune région valide trouvée pour le tracé. Vérifiez la colonne 'Région'.")

for region in regions:
    sous_df = df[df["Région"] == region]
    sous_df = sous_df.sort_values(by=["Année", "Nombre de films programmés"])

    if sous_df["Nombre de films programmés"].dtype == 'object':
        print(f"ATTENTION: La colonne 'Nombre de films programmés' pour la région {region} est toujours de type 'object' lors du tracé !")

    plt.plot(sous_df["Année"], sous_df["Nombre de films programmés"], marker='o', label=region)

plt.title("🎬 Évolution du Nombre de films programmés par région", fontsize=16)
plt.xlabel("Année", fontsize=12)
plt.ylabel("Nombre de films programmés", fontsize=12)
plt.legend(title="Régions", fontsize=10)
plt.grid(True)

# Configuration de l'axe Y (0 à 70000, pas de 5000)
plt.ylim(bottom=0, top=70000)
plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(5000))
plt.gca().yaxis.set_major_formatter(ticker.FormatStrFormatter('%d'))

plt.tight_layout()

chemin_sortie = "C:/Users/Nya Devas/Desktop/SAE_Cinema/APPLICATION/Graphique/nombre_films_programmes_final.png"
plt.savefig(chemin_sortie, dpi=300)
print(f"✅ Graphique enregistré ici : {chemin_sortie}")

#---------------------film inedits ----------
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

chemin_fichier = "C:/Users/Nya Devas/Desktop/SAE_Cinema/APPLICATION/EXPORT/STATISTIQUES/tout_programmation_par_region.csv"

df = pd.read_csv(chemin_fichier, sep=';', decimal=',')
df.columns = df.columns.str.strip()

df["Nombre de films inédits"] = pd.to_numeric(df["Nombre de films inédits"], errors='coerce')

df["Région"] = df["Région"].astype(str).str.replace(" / ", "-").str.strip()

print("\n--- Débogage Type de Données 'Nombre de films inédits' ---")
print("Type de la colonne 'Nombre de films inédits' après conversion :", df["Nombre de films inédits"].dtype)
print("Nombre de valeurs manquantes (NaN) :", df["Nombre de films inédits"].isna().sum())
print("--- Fin Débogage ---")

plt.figure(figsize=(15, 12))

regions = df["Région"].unique()
regions = [r for r in regions if pd.notna(r) and r != '']

if not regions:
    print("ATTENTION: Aucune région valide trouvée pour le tracé. Vérifiez la colonne 'Région'.")

for region in regions:
    sous_df = df[df["Région"] == region]
    sous_df = sous_df.sort_values(by=["Année", "Nombre de films inédits"])

    if sous_df["Nombre de films inédits"].dtype == 'object':
        print(f"ATTENTION: La colonne 'Nombre de films inédits' pour la région {region} est toujours de type 'object' lors du tracé !")

    plt.plot(sous_df["Année"], sous_df["Nombre de films inédits"], marker='o', label=region)

plt.title("🎬 Évolution du Nombre de films inédits par région", fontsize=16)
plt.xlabel("Année", fontsize=12)
plt.ylabel("Nombre de films inédits", fontsize=12)
plt.legend(title="Régions", fontsize=10)
plt.grid(True)

# Configuration de l'axe Y (0 à 50000, pas de 5000)
plt.ylim(bottom=0, top=50000)
plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(5000))
plt.gca().yaxis.set_major_formatter(ticker.FormatStrFormatter('%d'))

plt.tight_layout()

chemin_sortie = "C:/Users/Nya Devas/Desktop/SAE_Cinema/APPLICATION/Graphique/nombre_films_inedits_final.png"
plt.savefig(chemin_sortie, dpi=300)
print(f"✅ Graphique enregistré ici : {chemin_sortie}")


#--------------------------------Taux de rotation de film inédit sur écran---------------------------------#


import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

chemin_fichier = "C:/Users/Nya Devas/Desktop/SAE_Cinema/APPLICATION/EXPORT/STATISTIQUES/tout_programmation_par_region.csv"

df = pd.read_csv(chemin_fichier, sep=';', decimal=',')
df.columns = df.columns.str.strip()

df["Taux de rotation de film inédit sur écran"] = pd.to_numeric(df["Taux de rotation de film inédit sur écran"], errors='coerce')

df["Région"] = df["Région"].astype(str).str.replace(" / ", "-").str.strip()

print("\n--- Débogage Type de Données 'Taux de rotation de film inédit sur écran' ---")
print("Type de la colonne 'Taux de rotation de film inédit sur écran' après conversion :", df["Taux de rotation de film inédit sur écran"].dtype)
print("Nombre de valeurs manquantes (NaN) :", df["Taux de rotation de film inédit sur écran"].isna().sum())
print("--- Fin Débogage ---")

plt.figure(figsize=(15, 12))

regions = df["Région"].unique()
regions = [r for r in regions if pd.notna(r) and r != '']

if not regions:
    print("ATTENTION: Aucune région valide trouvée pour le tracé. Vérifiez la colonne 'Région'.")

for region in regions:
    sous_df = df[df["Région"] == region]
    sous_df = sous_df.sort_values(by=["Année", "Taux de rotation de film inédit sur écran"])

    if sous_df["Taux de rotation de film inédit sur écran"].dtype == 'object':
        print(f"ATTENTION: La colonne 'Taux de rotation de film inédit sur écran' pour la région {region} est toujours de type 'object' lors du tracé !")

    plt.plot(sous_df["Année"], sous_df["Taux de rotation de film inédit sur écran"], marker='o', label=region)

plt.title("🎬 Évolution du Taux de rotation de film inédit sur écran par région", fontsize=16)
plt.xlabel("Année", fontsize=12)
plt.ylabel("Taux de rotation de film inédit sur écran", fontsize=12)
plt.legend(title="Régions", fontsize=10)
plt.grid(True)

# Configuration de l'axe Y (0 à 130, pas de 10)
plt.ylim(bottom=0, top=130)
plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(10))
plt.gca().yaxis.set_major_formatter(ticker.FormatStrFormatter('%d'))

plt.tight_layout()

chemin_sortie = "C:/Users/Nya Devas/Desktop/SAE_Cinema/APPLICATION/Graphique/taux_rotation_film_inedit_final.png"
plt.savefig(chemin_sortie, dpi=300)
print(f"✅ Graphique enregistré ici : {chemin_sortie}")



#fréquentation 


#-------------------------------Taux de fréquentation par fauteuils
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

chemin_fichier = "C:/Users/Nya Devas/Desktop/SAE_Cinema/APPLICATION/EXPORT/STATISTIQUES/tout_frequentation_par_region.csv"

df = pd.read_csv(chemin_fichier, sep=';', decimal=',')
df.columns = df.columns.str.strip()

df["Taux de fréquentation par fauteuils"] = pd.to_numeric(df["Taux de fréquentation par fauteuils"], errors='coerce')

df["Région"] = df["Région"].astype(str).str.replace(" / ", "-").str.strip()

print("\n--- Débogage Type de Données 'Taux de fréquentation par fauteuils' ---")
print("Type de la colonne 'Taux de fréquentation par fauteuils' après conversion :", df["Taux de fréquentation par fauteuils"].dtype)
print("Nombre de valeurs manquantes (NaN) :", df["Taux de fréquentation par fauteuils"].isna().sum())
print("--- Fin Débogage ---")

plt.figure(figsize=(15, 12))

regions = df["Région"].unique()
regions = [r for r in regions if pd.notna(r) and r != '']

if not regions:
    print("ATTENTION: Aucune région valide trouvée pour le tracé. Vérifiez la colonne 'Région'.")

for region in regions:
    sous_df = df[df["Région"] == region]
    sous_df = sous_df.sort_values(by=["Année", "Taux de fréquentation par fauteuils"])

    if sous_df["Taux de fréquentation par fauteuils"].dtype == 'object':
        print(f"ATTENTION: La colonne 'Taux de fréquentation par fauteuils' pour la région {region} est toujours de type 'object' lors du tracé !")

    plt.plot(sous_df["Année"], sous_df["Taux de fréquentation par fauteuils"], marker='o', label=region)

plt.title("🎬 Évolution du Taux de fréquentation par fauteuils par région", fontsize=16)
plt.xlabel("Année", fontsize=12)
plt.ylabel("Taux de fréquentation par fauteuils", fontsize=12)
plt.legend(title="Régions", fontsize=10)
plt.grid(True)

# Configuration de l'axe Y (0 à 200, pas de 20)
plt.ylim(bottom=0, top=200)
plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(20))
plt.gca().yaxis.set_major_formatter(ticker.FormatStrFormatter('%d'))

plt.tight_layout()

chemin_sortie = "C:/Users/Nya Devas/Desktop/SAE_Cinema/APPLICATION/Graphique/taux_frequentation_fauteuils_final.png"
plt.savefig(chemin_sortie, dpi=300)
print(f"✅ Graphique enregistré ici : {chemin_sortie}")

#---------------------------Taux de rotation des fauteuils------------------------------------

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

chemin_fichier = "C:/Users/Nya Devas/Desktop/SAE_Cinema/APPLICATION/EXPORT/STATISTIQUES/tout_frequentation_par_region.csv"

df = pd.read_csv(chemin_fichier, sep=';', decimal=',')
df.columns = df.columns.str.strip()

df["Taux de rotation des fauteuils"] = pd.to_numeric(df["Taux de rotation des fauteuils"], errors='coerce')

df["Région"] = df["Région"].astype(str).str.replace(" / ", "-").str.strip()

print("\n--- Débogage Type de Données 'Taux de rotation des fauteuils' ---")
print("Type de la colonne 'Taux de rotation des fauteuils' après conversion :", df["Taux de rotation des fauteuils"].dtype)
print("Nombre de valeurs manquantes (NaN) :", df["Taux de rotation des fauteuils"].isna().sum())
print("--- Fin Débogage ---")

plt.figure(figsize=(15, 12))

regions = df["Région"].unique()
regions = [r for r in regions if pd.notna(r) and r != '']

if not regions:
    print("ATTENTION: Aucune région valide trouvée pour le tracé. Vérifiez la colonne 'Région'.")

for region in regions:
    sous_df = df[df["Région"] == region]
    sous_df = sous_df.sort_values(by=["Année", "Taux de rotation des fauteuils"])

    if sous_df["Taux de rotation des fauteuils"].dtype == 'object':
        print(f"ATTENTION: La colonne 'Taux de rotation des fauteuils' pour la région {region} est toujours de type 'object' lors du tracé !")

    plt.plot(sous_df["Année"], sous_df["Taux de rotation des fauteuils"], marker='o', label=region)

plt.title("🎬 Évolution du Taux de rotation des fauteuils par région", fontsize=16)
plt.xlabel("Année", fontsize=12)
plt.ylabel("Taux de rotation des fauteuils", fontsize=12)
plt.legend(title="Régions", fontsize=10)
plt.grid(True)

# Configuration de l'axe Y (0 à 3, pas de 0.5)
plt.ylim(bottom=0, top=3)
plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(0.5))
plt.gca().yaxis.set_major_formatter(ticker.FormatStrFormatter('%.1f')) # Affichage avec une décimale

plt.tight_layout()

chemin_sortie = "C:/Users/Nya Devas/Desktop/SAE_Cinema/APPLICATION/Graphique/taux_rotation_fauteuils_final.png"
plt.savefig(chemin_sortie, dpi=300)
print(f"✅ Graphique enregistré ici : {chemin_sortie}")

#------------------------------entrées par seance 
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

chemin_fichier = "C:/Users/Nya Devas/Desktop/SAE_Cinema/APPLICATION/EXPORT/STATISTIQUES/tout_frequentation_par_region.csv"

df = pd.read_csv(chemin_fichier, sep=';', decimal=',')
df.columns = df.columns.str.strip()

df["Entrées par séance"] = pd.to_numeric(df["Entrées par séance"], errors='coerce')

df["Région"] = df["Région"].astype(str).str.replace(" / ", "-").str.strip()

print("\n--- Débogage Type de Données 'Entrées par séance' ---")
print("Type de la colonne 'Entrées par séance' après conversion :", df["Entrées par séance"].dtype)
print("Nombre de valeurs manquantes (NaN) :", df["Entrées par séance"].isna().sum())
print("--- Fin Débogage ---")

plt.figure(figsize=(15, 12))

regions = df["Région"].unique()
regions = [r for r in regions if pd.notna(r) and r != '']

if not regions:
    print("ATTENTION: Aucune région valide trouvée pour le tracé. Vérifiez la colonne 'Région'.")

for region in regions:
    sous_df = df[df["Région"] == region]
    sous_df = sous_df.sort_values(by=["Année", "Entrées par séance"])

    if sous_df["Entrées par séance"].dtype == 'object':
        print(f"ATTENTION: La colonne 'Entrées par séance' pour la région {region} est toujours de type 'object' lors du tracé !")

    plt.plot(sous_df["Année"], sous_df["Entrées par séance"], marker='o', label=region)

plt.title("🎬 Évolution des Entrées par séance par région", fontsize=16)
plt.xlabel("Année", fontsize=12)
plt.ylabel("Entrées par séance", fontsize=12)
plt.legend(title="Régions", fontsize=10)
plt.grid(True)

# Configuration de l'axe Y (0 à 50, pas de 5)
plt.ylim(bottom=0, top=50)
plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(5))
plt.gca().yaxis.set_major_formatter(ticker.FormatStrFormatter('%d'))

plt.tight_layout()

chemin_sortie = "C:/Users/Nya Devas/Desktop/SAE_Cinema/APPLICATION/Graphique/entrees_par_seance_final.png"
plt.savefig(chemin_sortie, dpi=300)
print(f"✅ Graphique enregistré ici : {chemin_sortie}")

#-------------------entrée par habitant

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

chemin_fichier = "C:/Users/Nya Devas/Desktop/SAE_Cinema/APPLICATION/EXPORT/STATISTIQUES/tout_frequentation_par_region.csv"

df = pd.read_csv(chemin_fichier, sep=';', decimal=',')
df.columns = df.columns.str.strip()

df["Entrées par habitant"] = pd.to_numeric(df["Entrées par habitant"], errors='coerce')

df["Région"] = df["Région"].astype(str).str.replace(" / ", "-").str.strip()

print("\n--- Débogage Type de Données 'Entrées par habitant' ---")
print("Type de la colonne 'Entrées par habitant' après conversion :", df["Entrées par habitant"].dtype)
print("Nombre de valeurs manquantes (NaN) :", df["Entrées par habitant"].isna().sum())
print("--- Fin Débogage ---")

plt.figure(figsize=(15, 12))

regions = df["Région"].unique()
regions = [r for r in regions if pd.notna(r) and r != '']

if not regions:
    print("ATTENTION: Aucune région valide trouvée pour le tracé. Vérifiez la colonne 'Région'.")

for region in regions:
    sous_df = df[df["Région"] == region]
    sous_df = sous_df.sort_values(by=["Année", "Entrées par habitant"])

    if sous_df["Entrées par habitant"].dtype == 'object':
        print(f"ATTENTION: La colonne 'Entrées par habitant' pour la région {region} est toujours de type 'object' lors du tracé !")

    plt.plot(sous_df["Année"], sous_df["Entrées par habitant"], marker='o', label=region)

plt.title("🎬 Évolution des Entrées par habitant par région", fontsize=16)
plt.xlabel("Année", fontsize=12)
plt.ylabel("Entrées par habitant", fontsize=12)
plt.legend(title="Régions", fontsize=10)
plt.grid(True)

# Configuration de l'axe Y (0 à 30, pas de 5)
plt.ylim(bottom=0, top=30)
plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(5))
plt.gca().yaxis.set_major_formatter(ticker.FormatStrFormatter('%d'))

plt.tight_layout()

chemin_sortie = "C:/Users/Nya Devas/Desktop/SAE_Cinema/APPLICATION/Graphique/entrees_par_habitant_final.png"
plt.savefig(chemin_sortie, dpi=300)
print(f"✅ Graphique enregistré ici : {chemin_sortie}")




























import pandas as pd
import matplotlib.pyplot as plt

# 📄 Lecture des données
df = pd.read_csv("C:/Users/Nya Devas/Desktop/SAE_Cinema/APPLICATION/EXPORT/STATISTIQUES/tout_materiel_par_region.csv", sep=';')
df.columns = df.columns.str.strip()
df["Année"] = pd.to_numeric(df["Année"], errors="coerce")

# 🎯 Filtrage sur l'année la plus récente
annee_cible = 2021
df_2021 = df[df["Année"] == annee_cible]

# Dossier de sortie
chemin_graph = "C:/Users/Nya Devas/Desktop/SAE_Cinema/APPLICATION/Graphique/"

# 1️⃣ Top 10 régions – Nombre de cinémas
top_cinemas = df_2021.groupby("Région")["Nombre de cinémas"].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(15, 12))
top_cinemas.plot(kind="barh", color="skyblue")
plt.title("🎬 Top 10 régions par nombre de cinémas en 2022")
plt.xlabel("Nombre de cinémas")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig(chemin_graph + "top10_cinemas_2022.png", dpi=300)
plt.close()

# 2️⃣ Top 10 régions – Entrées par habitant


chemin_graph = "C:/Users/Nya Devas/Desktop/SAE_Cinema/APPLICATION/Graphique/"

# Chargement du fichier CSV
df = pd.read_csv("C:/Users/Nya Devas/Desktop/SAE_Cinema/APPLICATION/EXPORT/STATISTIQUES/tout_frequentation_par_region.csv", sep=';')
df.columns = df.columns.str.strip()

# Conversion des colonnes nécessaires
df["Année"] = pd.to_numeric(df["Année"], errors="coerce")

# Nettoyage de la colonne "Entrées par habitant"
df["Entrées par habitant"] = (
    df["Entrées par habitant"]
    .astype(str)
    .str.replace(",", ".")
    .str.replace(" ", "")
)

# Conversion en float
df["Entrées par habitant"] = pd.to_numeric(df["Entrées par habitant"], errors="coerce")

# Filtrage pour l'année cible
annee_cible = 2021
df_2021 = df[df["Année"] == annee_cible]

# Calcul des moyennes
top_entrees = (
    df_2021.groupby("Région")["Entrées par habitant"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

# Création du graphique
plt.figure(figsize=(15, 12))
top_entrees.plot(kind="barh", color="lightgreen")
plt.title(f"👥 Top 10 régions par entrées par habitant en 2022")
plt.xlabel("Entrées par habitant")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig(chemin_graph + f"top10_entrees_par_habitant_2022.png", dpi=300)
plt.close()


# 3️⃣ Tableau : Top 5 rotation de films inédits

df = pd.read_csv("C:/Users/Nya Devas/Desktop/SAE_Cinema/APPLICATION/EXPORT/STATISTIQUES/tout_programmation_par_region.csv", sep=';')
df.columns = df.columns.str.strip()
df["Année"] = pd.to_numeric(df["Année"], errors="coerce")
annee_cible = 2021
df_2021 = df[df["Année"]]== annee_cible
top_rotation = df_2021[["Région", "Taux de rotation de film inédit sur écran"]].dropna()
top_rotation = top_rotation.sort_values(by="Taux de rotation de film inédit sur écran", ascending=False).head(5)
top_rotation.to_csv(chemin_graph + "top5_rotation_films_inedits.csv", index=False)



