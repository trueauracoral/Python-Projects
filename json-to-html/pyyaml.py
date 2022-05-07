import yaml

with open('software.yaml') as f:
    data = yaml.load(f, Loader=yaml.FullLoader)
    print(data)

for key, item in data["software"].items():
    print(key+" - "+item)
