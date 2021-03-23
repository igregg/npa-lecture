from django.shortcuts import render

# Create your views here.

def device_connect(request):
    return render(request, 'frontend/device_connect.html')