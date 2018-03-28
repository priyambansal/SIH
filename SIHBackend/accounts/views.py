from django.shortcuts import render, redirect
from accounts.forms import SignupForm
from accounts.forms import CommonForm
from accounts.forms import JeeForm
from accounts.forms import GateForm

# Create your views here.

def signup(request):
	if request.method == 'POST':
		form = SignupForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/account/register')
	else:
		form = SignupForm()

		args = {'form':form}
		return render(request, 'accounts/signup_form.html', args)
def register(request):
	if request.method == 'POST':
	    form = CommonForm(request.POST)
	    if form.is_valid():
	    	form.save()
	    	return redirect('/account/exam/gate')
	else:
		form = CommonForm()

	return render(request, 'accounts/commonForm.html',{'form':form})

def jee(request):
      if request.method == 'POST':
      	form=JeeForm(request.POST)
      	if form.is_valid():
      	    form.save()
      	    return redirect('/account')
      else:
     	  form=JeeForm()

      return render(request,'accounts/jee.html',{'form':form})

def gate(request):
      if request.method == 'POST':
      	form=GateForm(request.POST)
      	if form.is_valid():
      	    form.save()
      	    return redirect('/account')
      else:
     	  form=GateForm()

      return render(request,'accounts/gate.html',{'form':form})