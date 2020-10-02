from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, BuyingForm, UserUpdateForm, ProfileUpdateForm

# Create your views here.
def register(request):
	if request.user.is_authenticated:
		messages.info(request, f'Logout first.')
		return redirect('home')
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Your account has been created! You are now able to log in')
			return redirect('login')
	else:
		form = RegisterForm()

	return render(request, 'register/register.html', {'form': form})

def logout(request):
	return render(request, 'register/logout.html', {})

@login_required
def buying_books(request, name):
    if name == '':
        return HttpResponseRedirect("/")

    form = BuyingForm()
    context = {
        'form': form,
        'book_name': name
    }
    return render(request, "register/buy_book.html", context)

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'register/profile.html', context)
