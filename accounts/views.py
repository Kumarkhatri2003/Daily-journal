from django.shortcuts import render,redirect
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout
# Create your views here.
def register_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return render(request, 'accounts/register.html', {'form': form})
    
    else:
        form= SignUpForm()
        return render(request,'accounts/register.html',{'form':form})
    
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('entry_list')
    else:
        form = AuthenticationForm()
        return render(request,'accounts/login.html',{'form':form})
    

def logout_view(request):
    logout(request)
    return redirect('login')