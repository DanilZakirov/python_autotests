import requests

response=requests.post("https://petstore.swagger.io/v2/pet", json=
{
  "id": 500,
  "category": {
    "id": 500,
    "name": "string"
  },
  "name": "vasya",
  "photoUrls": [
    "petr"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
})
print(response.text)
print(response.status_code)


