from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def home(request):
    return render(request, 'index.html')

def treasure(request):
    return render(request, 'treasure.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
        return render(request,'registration.html', {'form':form})