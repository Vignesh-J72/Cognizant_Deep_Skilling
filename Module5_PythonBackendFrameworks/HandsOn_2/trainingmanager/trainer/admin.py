from django.contrib import admin

# Register your models here.
from .models import Department, Employee, Instructor, SkillModule, Certification, ModuleSchedule

@admin.register(SkillModule)
class SkillModuleAdmin(admin.ModelAdmin):
    # Updated to reflect new field names
    list_display = ['module_name', 'module_code', 'credits', 'department']
    search_fields = ['module_name', 'module_code']
    list_filter = ['department']

# Register remaining models using standard registration
admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(Instructor)
admin.site.register(Certification)
admin.site.register(ModuleSchedule)