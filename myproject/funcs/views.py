from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

#Create your views here.
def homePageView(request):
  return HttpResponse("Hello! It's a test app which processes user input based on functions chosen and renders output")

def index(request):	
  print("====  =====  =====  =====",  "  ", request)

  if request.method == 'GET':	
    print("=================================== GET")
    return render(request, 'my_form.html', {})

  if request.method == 'POST' and request.POST['submit'] == 'submit': 
    print("=================================== POST")
    dict = request.POST
    print(request)
    print(request.POST)
   
    # import sys
    # print(sys.path)
    fact_input = dict['factorial']
    fibo_input = dict['fibonacci']    
    arms_input = dict['armstrong']
    palin_input = dict['palindrome'] 

    import myproject.utils.funcs_bag as funcs_bag
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
    
    print(type(mydict), "   values:   ", result_fact,"    ", result_fibo, "    ",  result_arms, "    ",  result_palin)
    return render(request, 'display.html', {'mydict': mydict}) 

  if request.method == 'POST' and request.POST['submit'] == 'back': 
  	print("================================ POST for BACK")
  	return render(request, 'my_form.html', {})


