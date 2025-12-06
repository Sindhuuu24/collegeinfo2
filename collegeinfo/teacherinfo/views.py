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
<<<<<<< HEAD
def register(request):
    return render(request, 'register.html')
def registerinfo(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        doj = request.POST.get('doj')
        data = {
            'name': name,
            'email': email,
             'doj': doj,
        }
        return render(request, 'registerinfo.html', data)
=======
>>>>>>> login
>>>>>>> 2014a9498c4241ae716d6c176e77ae9738d34f37
# Create your views here.

