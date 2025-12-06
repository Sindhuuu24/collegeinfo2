from django.shortcuts import render
def landing(request):
    return render(request, 'landing.html')
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

# Create your views here.
