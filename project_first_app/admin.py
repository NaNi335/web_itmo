from django.contrib import admin
from .models import Owner, Vehicle, Licence, Ownership

# Register your models here.
admin.site.register(Owner)
admin.site.register(Vehicle)
admin.site.register(Licence)
admin.site.register(Ownership)
