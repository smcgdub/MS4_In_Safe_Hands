from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    '''
    Sets the fields for the admin panel that are used, that are visible, \
    and that are read only
    '''
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date', 'delivery_cost', 'order_total',
                       'grand_total')

    fields = ('order_number', 'user_profile', 'date', 'first_name',
              'last_name', 'email', 'phone_number', 'street_address1',
              'street_address2', 'town_or_city', 'county', 'eircode',
              'country', 'delivery_cost', 'order_total', 'grand_total',)

    list_display = ('order_number', 'date', 'first_name', 'last_name',
                    'order_total', 'delivery_cost', 'grand_total',)

    ordering = ('-date',)

admin.site.register(Order, OrderAdmin)
