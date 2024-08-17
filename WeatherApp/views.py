from django.shortcuts import render
import json
import urllib.request

# Create your views here.
def index(request):
    if request.method == "POST":
        city = request.POST.get("city")
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=bf1f2eba55643fa4690088f863b8b668').read()
        
        data_list = json.loads(source)
        
        data = { 
            "country_code": str(data_list['sys']['country']), 
            "coordinate": str(data_list['coord']['lon']) + ' '+ str(data_list['coord']['lat']), 
            "temp": str(int(data_list['main']['temp']-273)) + '°C', 
            "pressure": str(data_list['main']['pressure']), 
            "humidity": str(data_list['main']['humidity']), 
        } 
        
    else:
        data = {}
    return render(request, 'index.html', data)