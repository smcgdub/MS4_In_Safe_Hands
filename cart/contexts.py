from decimal import Decimal
from django.conf import settings

def cart_contents(request):

    cart_items = []
    total = 0
    product_count = 0

    if total < settings.FREE_DELIVERY_THRESHOLD:
        # Always use DecimalField for money. Even simple operations like addition and subtraction are not immune to float rounding issues. https://stackoverflow.com/questions/2569015/django-floatfield-or-decimalfield-for-currency
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_point = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_point = 0
    
    grand_total = delivery + total
    
    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_point': free_delivery_point,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context