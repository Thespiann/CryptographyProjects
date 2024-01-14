import requests, json, sys

target = 'cryptohack.org'
req = requests.get("https://crt.sh/?q=%.{d}&output=json".format(d=target))

json_data = json.loads(req.text)
for (index, certificate) in enumerate(json_data):
    url = str(certificate['name_value'])
    if url.endswith(target):
        try:
            response_req = requests.get('https://' + url).text

            if (response_req.startswith('crypto')):
                print('flag : ' + response_req)
                break
        except:
            continue