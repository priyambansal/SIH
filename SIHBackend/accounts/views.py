from django.shortcuts import render, redirect
from accounts.forms import SignupForm

# Create your views here.
def home(request):
	return render(request, 'accounts/profile.html')

def signup(request):
	if request.method == 'POST':
		form = SignupForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/account')
	else:
		form = SignupForm()

		args = {'form':form}
		return render(request, 'accounts/signup_form.html', args)
