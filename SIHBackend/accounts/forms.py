from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import CommonRegistration
from .models import ExamJee,ExamGate

class SignupForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = (
			'username',
			'first_name',
			'last_name',
			'email',
			'password1',
			'password2',
		)
	def save(self, commit=True):
		user = super(SignupForm, self).save(commit=False)
		user.first_name=self.cleaned_data['first_name']
		user.last_name=self.cleaned_data['last_name']
		user.email=self.cleaned_data['email']
		
		if commit:
			user.save()

		return user

class CommonForm(forms.ModelForm):
	
	class Meta:
		model=CommonRegistration
		fields=('User_name','User_email','Contact',
				'DateOfBirth',
	            'Address',
				'Gender',
	            'Passport_number',
	            'Religion',
	            'Nationality',
	            'School',
	            'University',
	            'Marks_highschool',
	            'Marks_inter',
	            'Marks_university',)
    

def save(self, commit=True):
		form = super(CommonForm,self).save(commit=False)
		form.User_name=self.cleaned_data['User_name']
		form.User_email=self.cleaned_data['User_email']
		form.Contact=self.cleaned_data['Contact']
		form.DateOfBirth=self.cleaned_data['DateOfBirth']
		form.Address=self.cleaned_data['Address']
		form.Gender=self.cleaned_data['Gender']
		form.Passport=self.cleaned_data['Passport']
		form.Religion=self.cleaned_data['Religion']
		form.Nationality=self.cleaned_data['Nationality']
		form.School=self.cleaned_data['School']
		form.University=self.cleaned_data['University']
		form.Marks_highschool=self.cleaned_data['Marks_highschool']
		form.Marks_inter=self.cleaned_data['Marks_inter']
		form.Marks_university=self.cleaned_data['Marks_university']
		
		if commit:
			user.save()

		return user

class JeeForm(forms.ModelForm):
	
	class Meta:
		model=ExamJee
		fields=('Name',
	            'School_12',
	            'Marks_10',
	            'Marks_12',
	            'School_address',
	            'School_board',
	            'Profile_pic')
		def save(self, commit=True):
			form.Name=self.cleaned_data['Name']
			form.School_12=self.cleaned_data['School_12']
			form.Marks_10=self.cleaned_data['Marks_10']
			form.Marks_12=self.cleaned_data['Marks_12']
			form.School_address=self.cleaned_data['School_address']
			form.School_board=self.cleaned_data['School_board']
			form.Profile_pic=self.cleaned_data['Profile_pic']

			if commit:
				jee.save()

			return jee
    
class GateForm(forms.ModelForm):
	
	class Meta:
		model=ExamGate
		fields=('Name',
	            'School_12',
	            'Marks_10',
	            'Marks_12',
	            'School_address',
	            'School_board','University',
	            'Marks_university',
	            'Profile_pic')
		def save(self, commit=True):
			form.Name=self.cleaned_data['Name']
			form.School_12=self.cleaned_data['School_12']
			form.Marks_10=self.cleaned_data['Marks_10']
			form.Marks_12=self.cleaned_data['Marks_12']
			form.School_address=self.cleaned_data['School_address']
			form.School_board=self.cleaned_data['School_board']
			form.University=self.cleaned_data['University']
			form.Marks_university=self.cleaned_data['Marks_university']
			form.Profile_pic=self.cleaned_data['Profile_pic']

			if commit:
				gate.save()

			return gate
    