import requests

data = requests.get("https://randomuser.me/api/").json()
data = data["results"][0]

print(f'''I am {data["name"]["title"]}. {data["name"]["first"]} {data["name"]["last"]}. I live at {data["location"]["street"]["number"]} {data["location"]["street"]["name"]}. My city is {data["location"]["city"]}. My state is {data["location"]["state"]}. My country is {data["location"]["country"]}. In case your curious my postcode is {data["location"]["postcode"]}. My EXACT coordinates is latitude: {data["location"]["coordinates"]["latitude"]} and longitude: {data["location"]["coordinates"]["longitude"]}. I am {data["dob"]["age"]} years old. Here is a photo of me:
<img src="{data["picture"]["large"]}">''')