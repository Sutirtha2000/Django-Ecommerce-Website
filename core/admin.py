from django.contrib import admin

# Register your models here.
from .models import Item, Order, OrderItem, Payment, Coupon, Address, Refund, UserProfile

def make_refund_accepted(modelAdmin, request, queryset):
    queryset.update(refund_requested=False, refund_granted=True)

make_refund_accepted.short_description = 'Update Orders to refund granted' # This will show in the admin action panel

class ItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('title',)
    }

class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'ordered', 'being_delivered', 'received', 'refund_requested', 'refund_granted', 'user', 'billing_address', 'shipping_address', 'payment', 'coupon']
    list_filter = ['ordered', 'being_delivered', 'received', 'refund_requested', 'refund_granted']
    list_display_links = ['user', 'billing_address', 'shipping_address', 'payment', 'coupon']
    search_fields = ['user__username', 'ref_code']
    actions = [make_refund_accepted]

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('user', 'ordered')

class AddressAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'street_address',
        'apartment_address',
        'country',
        'zip',
        'address_type',
        'default'
    ]
    list_filter = [
        'default',
        'country',
        'address_type'
    ]
    search_fields = [
         'user',
        'street_address',
        'apartment_address',
        'zip'
    ]

admin.site.register(Item, ItemAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Payment)
admin.site.register(Coupon)
admin.site.register(Address, AddressAdmin)
admin.site.register(Refund)
admin.site.register(UserProfile)