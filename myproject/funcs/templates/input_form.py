from django import forms
from django.utils.safestring import mark_safe

class InputForm(forms.Form):
    factorial = forms.CharField(label='factorial of number', max_length=100)
    fibonacci = forms.CharField(label='fibonacci of n numbers', max_length=100)
    armstrong = forms.CharField(label='is number armstrong?', max_length=100)
    palindrome = forms.CharField(label='is input palindrome?', max_length=100)
