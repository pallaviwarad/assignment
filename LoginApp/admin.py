from django.contrib import admin
from .models import QuesModel
# Register your models here.
@admin.register(QuesModel)
class QuesModelAdmin(admin.ModelAdmin):
    list_display = ['id','question','op1','op2','op3','op4','ans']
