from django.contrib import admin

from .models import Vehicle, Driver, MaintenanceTicket

admin.site.register(Vehicle)
admin.site.register(Driver)
admin.site.register(MaintenanceTicket)