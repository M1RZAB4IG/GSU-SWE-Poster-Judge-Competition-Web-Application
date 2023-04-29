from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

def home(request):
    return render(request, 'page1.html')


@csrf_exempt
def my_func(request):
    pass



    
    
    






    