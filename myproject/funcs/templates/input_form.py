from django import forms

class InputForm(forms.Form):
    factorial = forms.CharField(label='factorial of number', max_length=3)
    fibonacci = forms.CharField(label='fibonacci of n numbers', max_length=3)
    armstrong = forms.CharField(label='is number armstrong?', max_length=10)
    palindrome = forms.CharField(label='is input palindrome?', max_length=100)
