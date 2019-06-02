from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
import myproject.utils.funcs_bag as funcs_bag

from .models import UserInput
from .templates.forms import InputForm 

def homePageView(request):
  if request.method == 'GET':
    return render(request, 'home.html', {})
  elif request.method == 'POST': 	
    return redirect('demo')   # urls.py => name = 'demo'

def demoView(request):	
  if request.method == 'GET':	   
    form = InputForm()
    return render(request, 'my_form.html', {'form': form})

  if request.method == 'POST' and 'submit' not in request.POST:
    form = InputForm(request.POST)    
    if form.is_valid(): 
      print("===    ===", form.cleaned_data)
      fact_input = form.cleaned_data['factorial']
      fibo_input = form.cleaned_data['fibonacci']    
      arms_input = form.cleaned_data['armstrong']
      palin_input = form.cleaned_data['palindrome'] 

      p = UserInput(factorial=fact_input, 
        fibonacci=fibo_input, 
        armstrong=arms_input, 
        palindrome=palin_input)
      p.save()

      if fact_input != '':
        fact_input = int(fact_input)
        result_fact = funcs_bag.fact(fact_input)
      else:
        fact_input = ''
        result_fact = ''

      if fibo_input != '':
        fibo_input = int(fibo_input)    
        result_fibo = funcs_bag.fibo(fibo_input) 
      else:
        result_fibo = ''

      if arms_input != '':
        arms_input = int(arms_input)
        result_arms = funcs_bag.isarmstrong(arms_input)
      else:
        result_arms = ''

      if palin_input != '':
        result_palin = funcs_bag.ispalin(palin_input)
      else:
        result_palin = ''                
      mydict = {'fact_in': fact_input, 'r_fact': result_fact, 'r_fibo': result_fibo, 'r_arms': result_arms, 'r_palin': result_palin}
      return render(request, 'display.html', {'mydict': mydict}) 

  elif 'submit' in request.POST and request.POST['submit'] == 'back': 
    form = InputForm()
    return render(request, 'my_form.html', {'form': form})


