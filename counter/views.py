from django.shortcuts import render
from django.template.loader import get_template
import requests
# Create your views here.
def home(request):
    response = requests.get('https://api.covidtracking.com/v1/us/current.json')
    info = response.json()
    datadict = info[0]
    
    return render(request, 'core/home.html', {
        'deaths': datadict['death']
    })