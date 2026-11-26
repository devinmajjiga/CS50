import json
import requests
import sys

if len(sys.argv) < 2:
    print("Missing command-line argument")
    sys.exit()
elif len(sys.argv) > 2:
    print("Too many command-line arguments ")
    sys.exit()
elif float(sys.argv[1]) < 0:
    print("Command-line argument is negative")
try:
    bitcoin = float(sys.argv[1])
except ValueError:
    print("Command-line argument is not a number")
    sys.exit()

response = requests.get(url="https://rest.coincap.io/v3/assets/bitcoin?apiKey=543587f8371fa1f91463c62643572f64c4bd0303e551a23997d80ee44495bf5b")

o = response.json()
response = o["data"]
price = response["priceUsd"]
bitcoin_price = float(price) * float(sys.argv[1])
print(f"{bitcoin_price:,.4f}")
