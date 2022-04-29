from django.shortcuts import render

def main_weather(request):
    return render(request, 'user_weather/main_weather.html', {})
