import requests
from pprint import pprint

url = "https://randomuser.me/api/"
param = {
    "results": 5,
    "inc": " mail, gender",
    "gender": "male"
}
headers = {}
data = {}
ls = []
res = requests.get(url, params=param, headers=headers, data=data)
db = res.json()
pprint(db)
