from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid() :
            form.save()
            return redirect('acticles:listOfArticles')

    else:
        form = UserCreationForm()
    return render(request , 'accounts/signup.html',{'form' : form})


def login_view(request):
    if request.method == "POST":
        pass
    else:
        form = AuthenticationForm()
    return render(request , 'accounts/login.html' , {'form':form})