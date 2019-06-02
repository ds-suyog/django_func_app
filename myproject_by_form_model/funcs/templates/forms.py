
from django.forms import ModelForm

# class InputForm(ModelForm):
#     class Meta:
#         model = UserInput
#         fields = ['factorial', 'fibonacci', 'armstrong', 'palindrome']

from django import forms
class InputForm(forms.Form):
    factorial = forms.CharField(label='factorial of number', max_length=3, required=False)
    fibonacci = forms.CharField(label='fibonacci of n numbers', max_length=3, required=False)
    armstrong = forms.CharField(label='is number armstrong?', max_length=10, required=False)
    palindrome = forms.CharField(label='is input palindrome?', max_length=100, required=False)
