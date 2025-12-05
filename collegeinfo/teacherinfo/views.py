from django.shortcuts import render
def landing(request):
    return render(request, 'landing.html')
<<<<<<< HEAD
<<<<<<< HEAD
def registration(request):
    return render(request, 'registration.html')
=======
def dashboard(request):
    return render(request,'dashboard.html')
>>>>>>> dashboard

=======
def login(request):
    return render(request, 'login.html')
>>>>>>> login
# Create your views here.
