import requests
import json
message = "https://github.com/LukeSmithxyz/voidrice"
query = message.split("/")
if query[2] == "github.com":
    github_api = f"https://api.github.com/repos/{query[3]}/{query[4]}"
    data = requests.get(github_api)
    json_stuff = json.loads(data.text)
    mb_size= round(float(json_stuff["size"]) / 1024, 1)
    print(f"""
Repo Name: {json_stuff["name"]}
Author Name: {json_stuff["owner"]["login"]}
Size: {mb_size} mb
Branch: {json_stuff["default_branch"]}
Issues: {json_stuff["open_issues"]}
""")
else:
    codeberg_api = f"https://{query[2]}/api/v1/repos/{query[3]}/{query[4]}"
    data = requests.get(codeberg_api)
    json_stuff = json.loads(data.text)

    mb_size= round(float(json_stuff["size"]) / 1024, 1)
    print(f"""Repo Name: {json_stuff["full_name"]}
Author Name: {json_stuff["owner"]["name"]}
Size: {mb_size} mb
Branch: {json_stuff["default_branch"]}
Issues: {json_stuff["open_issues_count"]}
Pull Requests: {json_stuff["open_pr_counter"]}""")
