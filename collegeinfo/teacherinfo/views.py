from django.shortcuts import render
def landing(request):
    return render(request, 'landing.html')
<<<<<<< HEAD
def registration(request):
    return render(request, 'registration.html')
=======
def dashboard(request):
    return render(request,'dashboard.html')
>>>>>>> dashboard

# Create your views here.
