from django.shortcuts import render
from .models import Registration
from .forms import RegistrationForm

def index(request):
    return render(request, 'index.html')



def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'index.html')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})




def view_data(request):
    ism_query = request.GET.get('ism')
    it_query = request.GET.get('it')

    registrations = Registration.objects.all()
    
    if ism_query:
        registrations = registrations.filter(ism__icontains=ism_query)
    if it_query:
        registrations = registrations.filter(it__icontains=it_query)
        
    return render(request, 'view_data.html', {'registrations': registrations})


def card(request):
    return render(request, 'card.html')

def python(request):
    return render(request, 'python.html')

def front(request):
    return render(request, 'front.html')

def teachers(request):
    return render(request, 'teachers.html')


def base(request):
    return render(request, 'base.html')