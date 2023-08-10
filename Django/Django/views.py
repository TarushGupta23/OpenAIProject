from django.shortcuts import render
import requests
url = "http://127.0.0.1:5555/Old/home.html"

def button(request):
    return render(request, 'home.html')

def output(request):
    data  = requests.get(url)
    print("hello**")
    data = data.text
    return render(request, 'home.html', {'data' : data})