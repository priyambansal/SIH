from django.shortcuts import render, redirect
from accounts.forms import SignupForm
from accounts.forms import CommonForm

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
def register(request):
	if request.method == 'POST':
	    form = CommonForm(request.POST)
	    if form.is_valid():
	    	form_f=form.save(commit=False)
	    	form_f.save()
	else:
		form = CommonForm()

		return render(request, 'accounts/commonForm.html',{'form':form})