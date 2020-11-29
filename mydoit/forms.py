from django import forms

class DoitForm(forms.Form):
	mydoit_text = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Add Your Doit!'}))