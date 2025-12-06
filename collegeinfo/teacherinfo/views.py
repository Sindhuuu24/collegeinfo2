from django.shortcuts import render
def landing(request):
    return render(request, 'landing.html')
def dashboard(request):
    return render(request,'dashboard.html')

# Create your views here.
