from django.contrib import admin
from .models import Stock, Portfolio, Transaction
# Register your models here.


class StockAdmin(admin.ModelAdmin):
  list_display = ("symbol", "company_name", "current_price")
  
admin.site.register(Stock, StockAdmin)
admin.site.register(Portfolio)
admin.site.register(Transaction)