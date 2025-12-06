from django.shortcuts import render
def landing(request):
    return render(request, 'landing.html')
<<<<<<< HEAD
def dashboard(request):
    return render(request,'dashboard.html')
def register(request):
    return render(request,'register.html')
def registerinfo(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        date = request.POST.get('date')
        context = {
            'name': name,
            'email': email,
            'date_of_joining': date
        }
        return render(request, 'registerinfo.html', context)
=======
<<<<<<< HEAD
<<<<<<< HEAD
def registration(request):
    return render(request, 'registration.html')
=======
def dashboard(request):
    return render(request,'dashboard.html')
>>>>>>> dashboard
>>>>>>> 349b643d65a5e6f0ab2f65bd4902ca701b7a9315



=======
def login(request):
    return render(request, 'login.html')
>>>>>>> login
# Create your views here.

