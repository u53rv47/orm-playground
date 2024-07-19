from django.db import models


# Create your models here.
class Salesman(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    commission = models.FloatField()

    class Meta:
        db_table = "inventory_salesman"


class Customer(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    grade = models.IntegerField()
    salesman_id = models.ForeignKey(
        Salesman, on_delete=models.CASCADE, related_name="c_salesmen"
    )

    class Meta:
        db_table = "inventory_customer"


class Order(models.Model):
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    date = models.DateField()
    customer_id = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="customers"
    )
    salesman_id = models.ForeignKey(
        Salesman, on_delete=models.CASCADE, related_name="o_salesmen"
    )

    class Meta:
        db_table = "inventory_order"
