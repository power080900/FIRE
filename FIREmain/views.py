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
    i = 1
    context = {
        'i': i
    }
    return render(request, 'calculator.html', context)

def financialledger(request):
    i = datetime.date.today().month
    j = list(range(1, 13))
    k = request.GET.get("month")
    print(k)
    context = {
        'i': i,
        'j': j,
        'k': k
    }
    return render(request, 'financialledger.html', context)

def result(request):
    liveage = request.GET.get('liveage')
    save = request.GET.get('save')
    use = request.GET.get('use')
    profit = request.GET.get('profit')
    retire = request.GET.get('retire')
    goal = request.GET.get('goal')
    if profit is not None:
        print("있는 값")
        print(profit)
    context = {
        'liveage': liveage,
        'save': save,
        'use': use,
        'profit': profit,
        'retire': retire,
        'goal': goal
    }
    return render(request, 'result.html', context)