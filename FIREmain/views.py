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
    age = request.GET.get('age')
    save = request.GET.get('save')
    use = request.GET.get('use')
    profit = request.GET.get('profit')
    retire = request.GET.get('retire')
    goal = request.GET.get('goal')
    if liveage is "":
        case = 1
        result = 1
    elif save is "":
        case = 2
        result = 2
    elif use is "":
        case = 3
        result = 3
    elif profit is "":
        case = 4
        result = 4
    elif retire is "":
        case = 5
        result = 5
    elif goal is "":
        case = 6
        result = 6
    context = {
        'case': case,
        'result': result
    }
    return render(request, 'result.html', context)