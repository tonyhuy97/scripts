import requests
import json

uid = "kjioWiB7k" #for disk-usage
server = "nagios server:3000"
url = server + "/api/dashboards/uid/" + uid
headers = {"Authorization":"Bearer [Put Key Here]"}
r = requests.get(url = url, headers = headers, verify=False)
pretty_r = json.loads(r.text)
#print(json.dumps(pretty_r['panels'][0]['targets'], indent=1))
print (json.dumps(pretty_r['dashboard']['panels'][0]['targets'], indent=1))
