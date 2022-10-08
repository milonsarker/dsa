import requests

url = "https://api.ultramsg.com/instance19007/messages/chat"

payload = "token=kr48taycx1pca9as&to=%2B18064709458&body=dhur&priority=1&referenceId="
headers = {'content-type': 'application/x-www-form-urlencoded'}

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)