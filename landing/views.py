#views landing
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .formlogin import LoginForm

#memuat landing
def landing(request):
    return render(request,'index.html')

#memuat about
def about(request):
    return render(request, 'about.html')

#memuat form login yang dari django jg
def custom_login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('services')  # ganti 'home' dengan URL tujuan setelah login
            else:
                messages.error(request, 'Username atau password salah')
    else:
        form = LoginForm()
        
    return render(request, 'login.html', {'form': form})

#memuat halaman transaction

#
