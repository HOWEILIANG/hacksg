from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(PriceData)
admin.site.register(Company)
admin.site.register(Dividend)
admin.site.register(TreasuryYield)
admin.site.register(Reit)
admin.site.register(Inflation)