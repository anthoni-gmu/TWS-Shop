from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from .forms import AccountForm,SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        
        accountform=AccountForm(request.POST)
        
        
        if form.is_valid() and accountform.is_valid():
            user=form.save()
            userprofile=accountform.save(commit=False)
            userprofile.user=user
            userprofile.save()
            
            login(request, user)
            return redirect('frontpage')
    else:
        form=SignUpForm()
        accountform=AccountForm()
    return render(request, 'signup.html',{'form':form,'accountform':accountform})

@login_required
def myaccount(request):
    return render(request, 'acount.html')