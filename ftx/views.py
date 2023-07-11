from django.shortcuts import render
from .models import Stock, Transaction

# Create your views here.

def home(request):
    stocks = Stock.objects.filter()[0:5]
    context = {'stocks':stocks}
    return render(request, ('home.html'), context)


def dashboard(request):
    items = Transaction.objects.all()
    context = {'items':items}
    return render(request, ('portfolio.html'), context)


def transaction_history(request):
    return render(request, ('transaction_history.html'))

def stock(request):
    stocks = Stock.objects.all()
    context = {'stocks':stocks}
    return render(request, ('stock.html'), context)



# def get_data(request):
#     stocks = Stock.objects.all()
#     stocks1 = Stock.objects.get(pk=1)

#     context = {
#     'stocks': stocks,
#     'stock': stocks1,
#     }
#     return render(request, ('get_data.html'), context)