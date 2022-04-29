from django.shortcuts import render

def main_weather(request):
    return render(request, 'blog/main_weather.html', {})
