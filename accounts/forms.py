from django import forms
from django.contrib.auth import (
	authenticate,
	get_user_model,
	login,
	logout,
	)


User = get_user_model()

class UserLoginForm(forms.Form):
    username = forms.CharField(label='Your Username', max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
    	username = self.cleaned_data.get('username')
    	password = self.cleaned_data.get('password')
    	if username and password:
    		user = authenticate(username=username, password=password)
	    	if not user:
	    		raise forms.ValidationError("এই ইউজার নিবন্ধিত নয়। ")
	    	if not user.check_password(password):
	    		raise forms.ValidationError("পাসওয়ার্ড ভুল !!!")
	    	if not user.is_active:
	    		raise forms.ValidationError("আপনি অনুমোদিত নন. চাকরি চলে গিয়েছে কি না জানার জন্য মানব সম্পদ উন্নয়ন HR বিভাগে যোগাযোগ করুন :D ")
    	return super(UserLoginForm, self).clean(*args, **kwargs)


class UserRegisterForm(forms.ModelForm):
	email = forms.EmailField(label = 'Email address')
	email2 = forms.EmailField(label='Confirm Email')
	password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = User
		fields = [
		'username', 
		'email', 
		'email2', 
		'password'
		]

	def clean_email2(self):
		email = self.cleaned_data.get('email')
		email2 = self.cleaned_data.get('email2')
		if email != email2:
			raise forms.ValidationError("Emails Must Match")

		email_qs = User.objects.filter(email=email)
		if email_qs.exists():
			raise forms.ValidationError("This email has already been registered")
		return email