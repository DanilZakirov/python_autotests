import requests

response=requests.put("https://petstore.swagger.io/v2/pet", json=
{
  "id": 500,
  "category": {
    "id": 0,
    "name": "vasya"
  },
  "name": "vasya",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 500,
      "name": "petr"
    }
  ],
  "status": "available"
})
print(response.text)
print(response.status_code)