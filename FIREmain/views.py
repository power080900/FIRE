from django.shortcuts import render

# Create your views here.

def main(request):
    num = 1
    context = {
        'num':num
    }
    return render(request, 'main.html', context)