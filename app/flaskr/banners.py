import requests

URL = "https://fortnite-api.com/v2/cosmetics/br"



print("Search username: ")
user = input("> ")
queryURL = URL + f"?username={user}"
response=requests.get(URL)

print(response.text) 
