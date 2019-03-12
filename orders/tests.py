from django.test import TestCase
from django.contrib.auth.models import User
from .models import PizzaTopping, SubExtra, MenuItem, Order, OrderItem 

# Create your tests here.
class OrderItemTestCase(TestCase):

    def setUp(self):
        customer1 = User.objects.create(username='hemabh')
        order1 = Order.objects.create(customer=customer1)

        customer2 = User.objects.create(username='hemabh1')
        order2 = Order.objects.create(customer=customer2)
        
        chickensm = OrderItem.objects.create(
                category='Dinner Platters',
                kind='Chicken Parm',
                price=60.00,
                size='Small'
        )
        chickenlg = OrderItem.objects.create(
                category='Dinner Platters',
                kind='Chicken Parm',
                price=80.00,
                size='Large'
        )
        
        bzchicken = OrderItem.objects.create(
                category='Pasta',
                kind='Baked Ziti w/Chicken',
                price=9.75
        )
            
    def test_order_count(self):
        c1 = User.objects.get(username='kylepw')
        o1 = Order.objects.get(customer=c1)

        c2 = User.objects.get(username='jimmy')
        o2 = Order.objects.get(customer=c2)

        chickensm = OrderItem.objects.get(kind='Chicken Parm', size='Small')
        chickenlg = OrderItem.objects.get(kind='Chicken Parm', size='Large')
        bzchicken = OrderItem.objects.get(kind='Baked Ziti w/Chicken')

        o1.items.add(chickenlg)
        o1.items.add(bzchicken)
        o2.items.add(chickensm)

        self.assertEqual(o1.items.count(), 2)
        self.assertEqual(o2.items.count(), 1)
