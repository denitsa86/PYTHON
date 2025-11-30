import requests
#requests is library, which is used to make HTTP requests (like GET or POST) to web APIs.

# Replace with your actual API key
#⚠️ Note: In real projects, you should never hardcode API keys in your code. Store them in
# environment variables or config files.
API_KEY = "84f03bfb0f0e1571369440b1539af564"
BASE_URL = "http://data.fixer.io/api/latest" #The endpoint for getting the latest exchange rates.

# Request latest exchange rates. This dictionary holds query parameters that will be sent to the API.
params = {
    "access_key": API_KEY,
    "symbols": "USD",   # Which currency rates you want (here, only USD).
    "base": "EUR"       # The base currency (EUR). (Fixer free plan defaults to EUR)
}

#Makes a GET request to the API endpoint.params=params attaches the dictionary as query string parameters
response = requests.get(BASE_URL, params=params)
#The API responds with JSON data.
#Converts the response body (JSON text) into a Python dictionary.
data = response.json()


# response.status_code == 200: Confirms the HTTP request succeeded.
# data.get("success"): Confirms the API itself says the request was valid.
# Both must be true before continuing.
if response.status_code == 200 and data.get("success"):
    eur_to_usd = data["rates"]["USD"] #The exchange rate from EUR → USD.
    amount_eur = int(input("Insert amount in eur:"))#3 #Example amount (1 EUR).
    converted = amount_eur * eur_to_usd  #Multiply by the rate to get USD equivalent.
    print(f"{amount_eur} EUR = {converted:.2f} USD")
else:
    print("Error:", data)
#If the request fails (bad key, network issue, or API error), it prints the error response.