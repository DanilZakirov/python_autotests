import requests

response=requests.get("https://petstore.swagger.io/v2/pet/500")

print(response.text)
print(response.status_code)