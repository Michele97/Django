from django.contrib import admin

from .models import Cliente 
from .models import Contratto 
from .models import Pagamento 

# Register your models here.
from django.contrib import admin





admin.site.register(Cliente)
admin.site.register(Contratto)
admin.site.register(Pagamento)