from django.contrib import admin
from .models import Employee
# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['empname','empemail','empcontact','empcity','empsal']
    search_fields=['empname']
    exclude = ["empsal"]
    ordering=['empsal']
    sortable_by=["empsal"]
    


