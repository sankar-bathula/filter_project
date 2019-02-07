from django.contrib import admin
from filter_app.models import Employee
class EmployeeAdmin(admin.ModelAdmin):
	list_display= ('id', 'ename', 'esal', 'eaddr')

admin.site.register(Employee, EmployeeAdmin)