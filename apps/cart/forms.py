from django import forms

class CheckoutForm(forms.Form):
    first_name = forms.CharField(max_length=255, initial='ana')
    last_name = forms.CharField(max_length=255, initial='cud')
    email = forms.EmailField(max_length=255, initial='anadjango8@gmail.com')
    phone = forms.CharField(max_length=255, initial='123456')
    address = forms.CharField(max_length=255, initial='moscow')
    zipcode = forms.CharField(max_length=255, initial='123456')
    place = forms.CharField(max_length=255, initial='3 street')
    stripe_token = forms.CharField(max_length=255)