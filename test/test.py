import requests

ws_address = "http://127.0.0.1:5000"
# test GET
r = requests.get(ws_address)
print r.status_code, r.text

# test POST
sample_json = {"user_i": "1234"}
r = requests.post(ws_address,
                  json=sample_json)
print r.status_code, r.text

