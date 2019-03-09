from django import forms

class ProductCreateForm(forms.Form):
	title = forms.CharField(label='')
	description = forms.CharField(widget=forms.Textarea(
						attrs= {
						"placeholder":'hello world',
						}
					))
	price 		= forms.DecimalField()
	summary 	= forms.CharField()
	email       = forms.EmailField()

	def clean_email(self):
		email = self.cleaned_data.get('email')
		name,domain = email.split("@")
		list_mail = ['gmail.com',"yahoo.com"]
		if domain not in list_mail:
			raise forms.ValidationError("this not yahoo or gmail")
		return email
