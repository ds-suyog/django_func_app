
from django.forms import ModelForm

class InputForm(ModelForm):
    class Meta:
        model = UserInput
        fields = ['factorial', 'fibonacci', 'armstrong', 'palindrome']

