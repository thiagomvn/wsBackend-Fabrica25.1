import requests
from django.shortcuts import render
from django.conf import settings

def currency_checker(request):
    api_key = settings.FIXER_API_KEY
    url = f"http://data.fixer.io/api/latest?access_key={10eb0b501ced17c6f45688bf64dd567e}"
    
    response = requests.get(url)
    data = response.json()

    if data.get('success'):
        currencies = data['rates']
        return render(request, 'currency_checker/index.html', {'currencies': currencies})
    else:
        return render(request, 'currency_checker/error.html', {'error': data.get('error', {})})