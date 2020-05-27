from django.contrib import admin
from .models import Breakfast
from .models import Lunch
from .models import Dinner
from .models import Special


admin.site.register(Breakfast)
admin.site.register(Lunch)
admin.site.register(Dinner)
admin.site.register(Special)
