import uuid
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Stock(models.Model):
    symbol = models.CharField(max_length=10)
    company_name = models.CharField(max_length=100)
    current_price = models.DecimalField(max_digits=10, decimal_places=2)
    icon = models.ImageField(upload_to='stocks/')

    # @classmethod
    # def get_single_instance(cls):
    #     return cls.objects.earliest('symbol')

    class Meta:
        verbose_name_plural = 'Stocks'

    def __str__(self) -> str:
        return self.symbol

class Portfolio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    stocks = models.ManyToManyField(Stock)
    quantity = models.IntegerField()

    def __str__(self) -> str:
        return self.name

# class Order(models.Model):
#     order_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
#     order_type = models.CharField(max_length=10)
#     quantity = models.IntegerField()
#     price = models.DecimalField(max_digits=10, decimal_places=2)

#     def __str__(self) -> str:
#         return self.order_id

class Transaction(models.Model):
    transaction_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=10)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    # Add other relevant fields as needed

    class meta:
        verbose_name_plural = 'Transactions'

    def __str__(self) -> str:
        return self.transaction_type
