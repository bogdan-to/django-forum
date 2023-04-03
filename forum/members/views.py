from django.shortcuts import render, redirect
from .forms import MemberCreationForm, MemberAuthenticationForm, MemberChangeForm
from .models import Member
from django.contrib.auth import login, logout ,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages



def register(request):
    register_form = MemberCreationForm(request.POST or None)

    if register_form.is_valid():
        member:Member = register_form.save()
        login(request, member)
        messages.success(request, 'Uspešno ste se registrovali. Dobrodošli,'+member.username+'!', extra_tags='alert-success')
        return redirect('index')

    context = {
        'form':register_form
    }
    return render(request, 'register.html', context)

def login_member(request):
    login_form = MemberAuthenticationForm(request=request, data=request.POST or None)

    if login_form.is_valid():
        username = login_form.cleaned_data['username']
        password = login_form.cleaned_data['password']
        member:Member = authenticate(username=username, password=password)
        if member:
            login(request, member)
            messages.success(request, 'Dobrodosli, '+ member.username + '!', extra_tags='alert-success')
            return redirect(request.META.get('HTTP_REFERER', 'forum'))
        
    messages.error(request, 'Pogrešno ime ili lozinka', extra_tags='alert-danger') 
   
    return redirect(request.META.get('HTTP_REFERER', 'forum'))

@login_required(login_url='login')
def logout_member(request):
    logout(request)
    messages.success(request, 'Uspešno ste se odjavili. Dođite nam ponovo!', extra_tags='alert-success')
    return redirect('index')

 
