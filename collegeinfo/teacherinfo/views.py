from django.shortcuts import render
def landing(request):
    return render(request, 'landing.html')
def registration(request):
    return render(request, 'registration.html')

# Create your views here.
