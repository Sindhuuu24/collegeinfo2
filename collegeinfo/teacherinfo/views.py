from django.shortcuts import render
def landing(request):
    return render(request, 'landing.html')
def login(request):
    return render(request, 'login.html')
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
# Create your views here.
