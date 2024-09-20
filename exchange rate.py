import requests
url='https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/usd.json'
from_country=input("From which country: ")
to_country=input("To which country: ")
amount=int(input("Enter amount: "))
response=requests.get(url)
rate= response.json()["usd"][from_country]
amount_usd= amount/rate
amount=amount_usd*(response.json()["usd"][to_country])
print(round(amount,2))

