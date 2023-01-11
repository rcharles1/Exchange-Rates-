#importing the requests library
import requests

from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")
targetCurrency = os.getenv("targetCurrency")

#getting baseCurrency and amount
baseCurrency = input('Enter a three-letter base currency code\n')
print('The target currency is', targetCurrency, 'by default')
Amount = input('Enter a Amount to be converted\n')

#api endpoint
URL = 'https://v6.exchangerate-api.com/v6/{}/pair/{}/{}/{}'.format(API_KEY,baseCurrency,targetCurrency,Amount)

#sending request response as response object
r = requests.get(url = URL)

if r.status_code == 200:
	data = r.json()

	#extracting conversion result
	results = data['conversion_result']

	#displaying results
	print('The equivalent of', Amount, baseCurrency ,'is',results,'TZS')

else:
	print('ERROR!!!')