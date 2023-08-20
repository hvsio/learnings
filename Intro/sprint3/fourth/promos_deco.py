from decimal import Decimal
from typing import Callable
from designpattern import Order

'''
This solution has several advantages over the others presented before:

The promotion strategy functions don’t have to use special names—no need for the _promo suffix.

The @promotion decorator highlights the purpose of the decorated function, and also makes it easy to temporarily disable a promotion: just comment out the decorator.

Promotional discount strategies may be defined in other modules, anywhere in the system, as long as the @promotion decorator is applied to them.
'''

Promotion = Callable[[Order], Decimal]

#The promos list is a module global, and starts empty.
promos: list[Promotion] = []

#Promotion is a registration decorator: it returns the promo function unchanged, after appending it to the promos list.
def promotion(promo: Promotion) -> Promotion:
    promos.append(promo)
    return promo

def best_promo(order: Order) -> Decimal:
    """Compute the best discount available"""
    return max(promo(order) for promo in promos)


#Any function decorated by @promotion will be added to promos
@promotion
def fidelity(order: Order) -> Decimal:
    """5% discount for customers with 1000 or more fidelity points"""
    if order.customer.fidelity >= 1000:
        return order.total() * Decimal('0.05')
    return Decimal(0)


@promotion
def bulk_item(order: Order) -> Decimal:
    """10% discount for each LineItem with 20 or more units"""
    discount = Decimal(0)
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * Decimal('0.1')
    return discount


@promotion
def large_order(order: Order) -> Decimal:
    """7% discount for orders with 10 or more distinct items"""
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * Decimal('0.07')
    return Decimal(0)