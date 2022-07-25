from django.shortcuts import render

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
    num = 1
    context = {
        'num':num
    }
    return render(request, 'financialledger.html', context)