from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'index.html')

@login_required
def treasure(request):
    return render(request, 'treasure.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            messages.error(request, "Error")
            return render(request,'registration/registration.html', {'form':form})
    else:
        form = UserCreationForm()
        return render(request,'registration/registration.html', {'form':form})