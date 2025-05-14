from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received
from django.dispatch import receiver
from django.conf import settings
import time
from .models import Order

@receiver(valid_ipn_received)
def paypal_payment_received(sender, **kwargs):
    #add 10 seconds delay for paypal to process the payment
    time.sleep(10)
    paypal_obj = sender
    my_invoice = str(paypal_obj.invoice)
    
    my_order = Order.objects.get(invoice=my_invoice)

    #record that the order has been paid
    my_order.paid = True

    #save the order
    my_order.save()