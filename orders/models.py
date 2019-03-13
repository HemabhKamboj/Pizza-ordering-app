from django.db import models
from django.contrib.auth.models import User


class PizzaTopping(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name}'


class SubExtra(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name}'


class MenuItem(models.Model):
    category = models.CharField(max_length=20)
    kind = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    size = models.CharField(max_length=5, blank=True)
    extra = models.BooleanField(default=False)

    def __str__(self):
        if self.extra:
            return f'+ {self.kind} (Rs{self.price})'
        else:
            return f'{self.category} / {self.size} {self.kind} (Rs{self.price})'


class Order(models.Model):
    customer = models.ForeignKey(
        User, 
        null=True, 
        on_delete=models.CASCADE, 
        related_name='orders'
    )
    timestamp = models.DateTimeField(auto_now=True)
    total = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    in_cart = models.BooleanField(default=True)
    placed = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f'Order #{self.id} by {self.customer.first_name}'


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, 
        on_delete=models.CASCADE, 
        null=True, 
        related_name='items'
    )
    category = models.CharField(max_length=20)
    kind = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    size = models.CharField(max_length=5, blank=True)
    toppings = models.ManyToManyField(
        PizzaTopping, 
        blank=True, 
        related_name='pizza'
    )
    extra = models.BooleanField(default=False)
    extras = models.ManyToManyField(SubExtra, blank=True, related_name='sub')

    def __str__(self):
        if self.extra:
            return f'+ {self.kind}'
        if self.toppings:
            return f'{self.category} / {self.size} {self.kind}'
        else:
            return f'{self.category} / {self.size} {self.kind}'


