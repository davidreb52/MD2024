from django.shortcuts import redirect, render
from django.contrib.auth import logout # import des fonctions login et authenticate

def logout_user(request):
    logout(request)
    return redirect('login')
