from django.shortcuts import render
import json
import urllib
# Create your views here.

def homepage(request):
    if request.method == 'POST':
        city = request.POST['city']
        url = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&appid=979c31c159d536fafdc155c66bd467eb').read()
        list_data = json.loads(url)
        print(url)
        
    return render(request, 'index.html')