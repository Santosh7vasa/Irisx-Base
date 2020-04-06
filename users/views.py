from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            print("Valid Form")
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username} account has been created! Please Login.')
            return redirect('login')
        else:
            print("INVALID FORM!!!")
    else :
        form = UserRegisterForm()
        print("Got into GET Request!!!")
    return render(request, 'users/register.html', {'form':form})

@login_required
def profile(request):
    print("Into Profile View")
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance = request.user)
        p_form = ProfileUpdateForm(request.POST ,request.FILES, instance = request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            username = u_form.cleaned_data.get('username')
            messages.success(request, f'{username} account has been updated!.')
            return redirect('profile')

    else :
        u_form = UserUpdateForm(instance = request.user)
        p_form = ProfileUpdateForm(instance = request.user.profile)


    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)
