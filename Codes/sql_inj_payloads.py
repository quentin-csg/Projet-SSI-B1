import requests

url = input("Choose url: ")

# Initialiser la liste des résultats
results = []

# Ouvrir le fichier des payloads
with open('./wordlists/payloads.txt', 'r') as userfile:
    users = userfile.readlines()

# Pour chaque payload, envoyer une requête POST à l'URL
for user in users:
    payload = user.strip()
    passwd = "whatever"
    r = requests.post(url, data={'username': payload, 'password': payload})
    
    # Vérifier si l'injection SQL a réussi
    if "Nom d'utilisateur ou mot de passe incorrect" not in r.text:
        
        # Vérifier si le résultat est nouveau
        if user not in results:
            results.append(user)
            results.append('\n')
            print("Possible SQL injection vulnerability")
            print(user)
            