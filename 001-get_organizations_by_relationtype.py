import http.client
import json

# Variables
subdomain = ""
relationtype = ""
authentication_key = ""
authentication_secret = ""

# Initial connection
conn = http.client.HTTPSConnection(subdomain + ".simplicate.nl")

headers = {
    'cookie': "nlbi_1185862=9O4mAOYWQ2Gf0nTn%2FP4j1wAAAAADXRPb9CmukBeBW70faQvG; visid_incap_1185862=cDHbwConT2KOf8X%2F7B6qzNUHc14AAAAAQUIPAAAAAADvKr1sKcGWKGZwdOYw8AOq; incap_ses_942_1185862=%2BqVAWibNAgIjiDB87agSDdYHc14AAAAAqaD2xlW7Q%2FVKVUG%2B6MYosw%3D%3D",
    'authentication-key': authentication_key,
    'authentication-secret': authentication_secret
    }

payload = ""

conn.request("GET", "/api/v2/crm/organization?q%5Brelation_type.id%5D=" + relationtype, payload, headers)
res = conn.getresponse()

# Data wrangling
data = json.loads(res.read().decode("utf-8"))

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)


with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    org_ids = []

    for i in data["data"]:
        org_ids.append(i["id"])
        print(org_ids)

    for i in org_ids:
        print(i)
        conn.request("DELETE", "/api/v2/crm/organization/" + i, payload, headers)
        res = conn.getresponse()
        data = res.read()
        print(data.decode("utf-8"))