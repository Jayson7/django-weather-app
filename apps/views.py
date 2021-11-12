from django.shortcuts import render
import json
from urllib.error import HTTPError
import urllib
# Create your views here.


def homepage(request):
    if request.method == 'POST':

        city = request.POST['city']
        try:
            url = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&appid=979c31c159d536fafdc155c66bd467eb').read()
            list_data = json.loads(url)
            # print(url)
            data = {
                "country_code": str(list_data['sys']['country']),
                "main_weather": str(list_data['weather'][0]['main'] ),
                "coordinate": str(list_data['coord']['lon'] ) + ', ' + str(list_data['coord']['lat']),
                "temp": str(list_data['main']['temp'] ) + ' °C' , 
                "pressure": str(list_data['main']['pressure'] ),
                "humidity": str(list_data['main']['humidity'] ),
                "description": str(list_data['weather'][0]['description'] ),
                "icon":str(list_data['weather'][0]['icon']) ,
                "name":str(list_data["name"] )}
            
        except HTTPError:
            data = {}

            print("none")
        


            
        
    else:
        data = {}
    return render(request, 'index.html', data )