from django.contrib import admin
from .models import Product, Contact, Orders, OrderUpdate

# Register your models here.
# Register Product (table/database) with admin.
admin.site.register(Product)
# Register contact database with admin.
admin.site.register(Contact)
# Register Orders(table/database) with admin.
admin.site.register(Orders)
# Register OrderUpdate(table/database) with admin.
admin.site.register(OrderUpdate)
