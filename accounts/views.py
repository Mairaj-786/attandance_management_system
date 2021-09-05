from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .forms import UserRegisterForm
from django.contrib import messages
# Create your views here.


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Created success')
            return HttpResponseRedirect('/accounts/register')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})
