from django.shortcuts import render
from .models import Task, Product,Transaction, StockDetail
from django.db.models import Sum
from django.http import HttpResponse

def home(request):
    return render(request, 'inventory/home.html')

def task_dashboard(request):
    transactions = Transaction.objects.prefetch_related('stockdetail_set__product')
    transactions = [txn for txn in transactions if txn.stockdetail_set.all()]
    return render(request, 'inventory/task_dashboard.html', {'transactions': transactions})



def product_list(request):
    products = Product.objects.all()
    return render(request, 'inventory/product.html', {'products': products})


def transaction_list(request):
    transactions = Transaction.objects.all()
    return render(request, 'inventory/transaction.html', {'transactions': transactions})


def stock_report(request):
    report = StockDetail.objects.values('product__name').annotate(total_quantity=Sum('quantity'))
    return render(request, 'inventory/stock.html', {'report': report})
