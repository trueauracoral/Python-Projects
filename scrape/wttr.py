import requests

website = "https://wttr.in/"
city = "texas"

data = requests.get(website+city+"?format=4").text
print(data)
