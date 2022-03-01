import requests
import json
message = "https://codeberg.org/zortazert/python-projects"
query = message.split("/")
codeberg_api = f"https://{query[2]}/api/v1/repos/{query[3]}/{query[4]}"
data = requests.get(codeberg_api)
json_stuff = json.loads(data.text)

mb_size= round(float(json_stuff["size"]) / 1024, 1)
print(f"""
Repo Name: {json_stuff["full_name"]}
Author Name: {json_stuff["name"]}
Size: {mb_size}
Branch: {json_stuff["default_branch"]}
Issues: {json_stuff["open_issues_count"]}
Pull Requests: {json_stuff["open_pr_counter"]}
""")
