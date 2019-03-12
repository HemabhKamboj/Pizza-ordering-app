from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.http import HttpResponse, HttpResponseRedirect, Http404 
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from smtplib import SMTPException, SMTPAuthenticationError
from .models import PizzaTopping, SubExtra, MenuItem, OrderItem, Order  


def model_dict(model, cat=None):
    """
        Returns a dictionary based on cat (category) on a model where keys are 
        field names (minus 'id') with all possible, distinct values. If no 
        cat value passed, all categories and values are returned.
    """

    keys = [field.name for field in model._meta.get_fields()]
    new = {}
    if 'id' in keys:
        keys.remove('id')

    if cat is None:
        for k in keys:
            new[k] = model.objects.values_list(k, flat=True).distinct()
    # Remove extras from subs
    elif cat is 'Subs':
        for k in keys:
            new[k] = model.objects.filter(category=cat).exclude(
                extra=True
            ).values_list(k, flat=True).distinct()
    else:
        for k in keys:
            new[k] = model.objects.filter(category=cat).values_list(
                k, 
                flat=True
            ).distinct()

    return new;


def cart(customer):
    """
        Return current cart or make new one
    """
    try:
        cart = Order.objects.get(customer=customer, in_cart=True)
    except Order.DoesNotExist:
        cart = Order(customer=customer) 
        cart.save()
    return cart


def update_total(order):
    """ 
        Updates total price of order.
    """
    if not isinstance(order, Order):
        raise Http404("{} is not an instance of Order.".format(order))
    else:     
        items = order.items.all()
        order.total = 0
        for item in items:
            order.total += item.price
        order.save()


def cart_count(customer):
    """ 
        Return number of items in cart.
    """
    try:
        cart = Order.objects.get(customer=customer, in_cart=True)
    except Order.MultipleObjectsReturned:
        raise Http404("More than one cart found.")
    except Order.DoesNotExist:
        return 0 
    else:
        # Exclude sub extras in count
        return cart.items.exclude(category='Subs', extra=True).count() 





