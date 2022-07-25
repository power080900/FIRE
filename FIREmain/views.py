from django.shortcuts import render
import datetime

# Create your views here.

def main(request):
    num = 1
    context = {
        'num':num
    }
    return render(request, 'main.html', context)

def calculator(request):
    num = 1
    context = {
        'num':num
    }
    return render(request, 'calculator.html', context)

def financialledger(request):
    i = datetime.date.today().month
    j = list(range(1, 13))
    k = request.GET.get("monthly")
    print(k)
    context = {
        'i': i,
        'j': j,
        'k': k
    }
    return render(request, 'financialledger.html', context)