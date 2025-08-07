from django.contrib import admin
from .models import Task, Product, Transaction, StockDetail

admin.site.register(Task)
admin.site.register(Product)
admin.site.register(Transaction)
admin.site.register(StockDetail)
